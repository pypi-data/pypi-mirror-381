# -*- coding: utf-8 -*-
# Copyright (C) European Gravitational Observatory (2022) and
#               California Institute of Technology (2023)
#
# Author list: Rhys Poulton <poulton@ego-gw.it>
#              Patrick Godwin <patrick.godwin@ligo.org>
#
# This file is part of igwn-lldd-common.
#
# igwn-lldd-common is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# igwn-lldd-common is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with igwn-lldd-common.  If not, see <http://www.gnu.org/licenses/>.

from collections import deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
import logging
import os
import re
import sys
import time

import configargparse

from . import cli
from .crc import can_check_crc
from .framelen import frame_length
from .framekafkaconsumer import FrameKafkaConsumer
from .io import clean_old_frames, write_frame
from .log import configure_logger
from .utils import (
    create_pid_file,
    GracefulKiller,
    str2bool,
)


logger = logging.getLogger(__name__)


def main(args=None):

    parser = configargparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        is_config_file=True,
        help="config file path"
    )
    parser.add_argument(
        "-dw",
        "--debug-wait",
        type=float,
        default=0.0,
        help="wait x seconds between gwf files (used to \
 intentionally break things for debugging)",
    )
    parser.add_argument(
        "-maxt",
        "--max-runtime",
        type=float,
        help="Maximum time to run before exiting (undef=Infinity)",
    )
    parser.add_argument(
        "-b",
        "--bootstrap-servers",
        type=str,
        default="localhost:9092",
        help="specify the Kafka cluster bootstrap servers",
    )
    parser.add_argument(
        "-x",
        "--exit-if-missing-topics",
        action="store_const",
        const=True,
        default=False,
        help="exit if any topics are missing",
    )
    parser.add_argument(
        "-s",
        "--ssl",
        action="store_const",
        const=True,
        default=False,
        help="use ssl"
    )
    parser.add_argument("-p", "--ssl-password", type=str, help="ssl password")
    parser.add_argument(
        "-ca",
        "--ssl-cafile",
        type=str,
        help="location of ca-cert"
    )
    parser.add_argument(
        "-cf",
        "--ssl-certfile",
        type=str,
        help="location of signed certificate"
    )
    parser.add_argument(
        "-kf", "--ssl-keyfile", type=str, help="location of personal keyfile"
    )
    parser.add_argument("-g", "--group-id", type=str, help="Kafka group ID")
    parser.add_argument(
        "-ff",
        "--fast-forward",
        type=str2bool,
        default=True,
        help="fast forward if fall behind",
    )
    parser.add_argument(
        "-lkp",
        "--load-kafka-python",
        action="store_const",
        const=True,
        default=False,
        help="load kafka-python rather than confluent-kafka",
    )
    parser.add_argument(
        "--tmpdir",
        type=str,
        metavar="path",
        help=(
            "path where temporary files will be written. "
            "defaults to same directory as output frames"
        ),
    )
    parser.add_argument(
        "--write-unsafe",
        type=str2bool,
        default=False,
        help=(
            "directly write frames to disk, without writing to a temporary "
            "location first. NOTE: writes are not atomic and do not ensure "
            "all data is on disk"
        ),
    )
    parser.add_argument(
        "-rn",
        "--ringn",
        type=int,
        default=None,
        help="Maximum mumber of frame files to retain",
    )
    parser.add_argument(
        "--retention-time",
        type=int,
        help=(
            "Retention time for frame files in seconds."
        ),
    )
    parser.add_argument(
        "--clean-interval",
        type=int,
        default=300,
        help=(
            "Interval at which frames in directories "
            "that don't meet retention policy are cleared out, "
            "in seconds. Default: 5 minutes."
        ),
    )
    parser.add_argument(
        "-pt",
        "--poll-timeout",
        type=int,
        default=1000,
        help="Timeout when doing consumer.poll() [in ms]. Default: 1000.",
    )
    parser.add_argument(
        "-pr",
        "--poll-max-records",
        type=int,
        default=1,
        help="Max records returned when doing consumer.poll(). Default: 1.",
    )
    parser.add_argument(
        "-pif",
        "--pid-file",
        type=str,
        default=None,
        help="File in which to store PID of main process.",
    )
    cli.add_status_update_options(parser)
    cli.add_topic_partition_options(parser)
    cli.add_logging_options(parser)

    # Parse the arguments from the command line
    args = parser.parse_args(args)

    # Sanity check input options
    if args.crc_check and not can_check_crc:
        raise ValueError("framel needs to be installed for CRC checks")

    # configure logger
    configure_logger("kafka2frame", log_level=cli.get_log_level(args))

    # Create the PID file if requested
    if args.pid_file is not None:
        create_pid_file(args.pid_file)

    # Get the topics from the topic partition
    tp_info = cli.extract_topic_partition_info(args, key_by_topic=True)

    # Startup the frame kafka consumer
    frameconsumer = FrameKafkaConsumer(args, tp_info)

    ringn_topic = {}
    dyn_frame_len = {}
    file_name_dq = {}
    filename_pattern = {}
    check_dir = {}
    tmpdirs = {}
    last_cleanup = {ifo: 0 for ifo in args.ifo}

    # Setup each of the topic
    for topic in tp_info:
        # Set the filename
        frame_filename_pattern = os.path.join(
            tp_info[topic]["frame_dir"],
            "%obs%-%tag%-%timestamp%-%delta_t%.gwf",
        )

        # Check if topic has ringn
        if "ringn" in tp_info[topic] and tp_info[topic]["ringn"]:
            ringn_topic[topic] = int(tp_info[topic]["ringn"])
            file_name_dq[topic] = deque([], ringn_topic[topic])
        else:
            if args.ringn:
                ringn_topic[topic] = int(args.ringn)
                file_name_dq[topic] = deque([], ringn_topic[topic])
            else:
                ringn_topic[topic] = None
                file_name_dq[topic] = deque([], ringn_topic[topic])

        # do we have to dynamically calculate frame length?
        dyn_frame_len[topic] = False
        if not ("delta_t" in tp_info[topic]) or not tp_info[topic]["delta_t"]:
            if (
                "delta_t_fallback" in tp_info[topic]
                and tp_info[topic]["delta_t_fallback"]
            ):
                dyn_frame_len[topic] = True
        else:
            frame_filename_pattern = re.sub(
                "%delta_t%",
                str(tp_info[topic]["delta_t"]),
                frame_filename_pattern
            )

        # set filename/directory properties
        frame_filename_pattern = re.sub(
            "%obs%",
            tp_info[topic]["observatory"],
            frame_filename_pattern
        )
        filename_pattern[topic] = frame_filename_pattern
        if args.tmpdir:
            tmpdirs[topic] = os.path.join(args.tmpdir, tp_info[topic]["ifo"])
        else:
            tmpdirs[topic] = tp_info[topic]["frame_dir"]
        check_dir[topic] = False

        if dyn_frame_len[topic]:
            logger.debug(
                "Dynamically calculating frame lengths for topic [%s]", topic
            )
        else:
            logger.debug(
                "Will NOT be dynamically calculating frame lengths for topic [%s]",
                topic
            )

    # Capture signals in the main thread
    killer = GracefulKiller()

    # Mark start time
    start_time = time.time()

    # start thread pool for frame writing
    futures = []
    num_threads = len(tp_info)
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        while not killer.kill_now:
            # Check if the runtime has gone above the max runtime
            current_time = time.time()
            runtime = current_time - start_time
            if args.max_runtime and runtime > args.max_runtime:
                logger.info("Have run for %f seconds stopping", runtime)
                break

            for frame_buffer, payload_info in frameconsumer.poll_and_extract(
                tp_info
            ):
                # continue if the full frame has not been assembled
                if not frame_buffer:
                    continue

                # come up with a filename
                topic = payload_info["topic"]
                frame_filename = re.sub(
                    "%timestamp%",
                    "%0.10d" % (payload_info["data_gps_timestamp"]),
                    filename_pattern[topic],
                )
                frame_filename = re.sub(
                    "%tag%",
                    tp_info[topic]["tag"],
                    frame_filename,
                )

                # do we have to calculate dynamically the length of the frame?
                if dyn_frame_len[topic]:
                    _, _, frame_duration = frame_length(frame_buffer)
                    frame_filename = re.sub(
                        "%delta_t%", str(int(frame_duration)), frame_filename
                    )

                # create directory if needed
                if not check_dir[topic]:
                    os.makedirs(os.path.dirname(frame_filename), exist_ok=True)
                    os.makedirs(tmpdirs[topic], exist_ok=True)
                    check_dir[topic] = True

                # write frame, clear tracked files according to retention
                future = executor.submit(
                    write_frame,
                    frame_filename,
                    frame_buffer,
                    ringn_topic[topic],
                    file_name_dq[topic],
                    tmpdir=tmpdirs[topic],
                    retention_time=args.retention_time,
                    unsafe=args.write_unsafe,
                )
                futures.append(future)

                # add cleanup task per cleaning interval for untracked files
                ifo = tp_info[topic]["ifo"]
                if (current_time - last_cleanup[ifo]) >= args.clean_interval:
                    frame_dir = os.path.dirname(frame_filename)
                    if args.retention_time:
                        # give padding to untracked time to avoid cleaning
                        # frames which are tracked by this process
                        untracked_retention_time = 2 * args.retention_time
                        logger.info(
                            "cleaning untracked files in %s",
                            frame_dir,
                        )
                        future = executor.submit(
                            clean_old_frames,
                            frame_dir,
                            untracked_retention_time,
                        )
                        futures.append(future)
                    last_cleanup[ifo] = current_time

                # evaluate futures and consume any finished tasks
                if len(futures) >= num_threads:
                    done, not_done = wait(
                        futures,
                        timeout=1,
                        return_when=FIRST_COMPLETED,
                    )

                    # consume finished tasks, keep unfinished
                    [future.result() for future in done]
                    futures = list(not_done)

                # check for keyboard interrupt
                if killer.kill_now:
                    logger.info("main: ^C while processing messages")
                    wait(futures)
                    break

                # wait if requested
                if args.debug_wait > 0.0:
                    logger.info("WAITING...")
                    time.sleep(args.debug_wait)

    # and close the Kafka connection
    frameconsumer.close()

    if args.pid_file is not None:
        logger.info("Removing old pid file [%s]", args.pid_file)
        os.unlink(args.pid_file)

    # did we exit out on a signal?
    # if so, we've reset the signal handlers, so call the signal
    # again to get the default handling.
    # (If we don't do this, then killing the parent by using "kill"
    # and not "kill -9" will just keep the parent around waiting
    # for the child to terminate, for example.)
    if killer.kill_now:
        os.kill(os.getpid(), killer.signum)


if __name__ == "__main__":
    sys.exit(main())

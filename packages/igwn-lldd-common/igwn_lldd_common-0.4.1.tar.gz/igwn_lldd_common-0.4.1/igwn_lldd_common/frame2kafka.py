# -*- coding: utf-8 -*-
# Copyright (C) European Gravitational Observatory (2022)
#
# Author: Rhys Poulton <poulton@ego-gw.it>
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

import sys
import configargparse
import queue
import logging
import ntpath
import time
import os
import gpstime
try:
    from watchdog.observers import Observer
    from .io import FrameFileEventHandler
    watchdog_found = True
except ImportError:
    from .io import monitor_dir_inotify
    import threading
    watchdog_found = False
from . import cli
from .crc import check_crc, can_check_crc
from .framekafkaproducer import FrameKafkaProducer
from .log import configure_logger
from .utils import str2bool


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
        help="Specify the Kafka cluster bootstrap servers",
    )
    parser.add_argument(
        "-fd",
        "--frame-directory",
        type=str,
        help="The directory where the frames are written to"
    )
    parser.add_argument("-g", "--group-id", type=str, help="Kafka group ID")
    parser.add_argument(
        "-S",
        "--split-bytes",
        type=int,
        default=100000,
        help="Split messages into this many bytes when adding to Kafka",
    )
    parser.add_argument(
        "-t",
        "--topic",
        type=str,
        required=True,
        help="Kafka topic to write to"
    )
    parser.add_argument(
        "--crc-check",
        type=str2bool,
        default=False,
        help="Run a CRC check for each frame",
    )
    parser.add_argument(
        "-bs",
        "--batch-size",
        type=int,
        help="Change the batch.size for the producer [default: 16384]",
    )
    parser.add_argument(
        "-bm",
        "--buffer-memory",
        type=int,
        help="Change the buffer.memory for the producer \
[default: 33554432B=32MB]",
    )
    parser.add_argument(
        "-lm",
        "--linger-ms",
        type=int,
        help="Change the linger.ms for the producer [default: 0]",
    )
    parser.add_argument(
        "-a",
        "--acks",
        default=1,
        type=int,
        help="Change the acks for the producer"
    )
    parser.add_argument(
        "-mi",
        "--min-interval",
        default=-1,
        type=float,
        help="Enforce a minimum interval between gwf files",
    )
    parser.add_argument(
        "-dt",
        "--delta-t",
        default=1,
        type=int,
        help="Make sure each frame comes in at delta_t seconds",
    )
    # custom libraries
    parser.add_argument(
        "-lkp",
        "--load-kafka-python",
        action="store_const",
        const=True,
        default=False,
        help="load kafka-python rather than confluent-kafka",
    )
    cli.add_status_update_options(parser)
    cli.add_logging_options(parser)

    # Parse the arguments from the command line
    args, _ = parser.parse_known_args(args)

    # configure logger
    configure_logger("frame2kafka", log_level=cli.get_log_level(args))

    logger.debug(f"topic: [{args.topic}]")
    logger.debug(f"crc_check: [{args.crc_check}]")
    logger.debug(f"bootstrap_servers: [{args.bootstrap_servers}]")
    logger.debug(f"split_bytes: [{args.split_bytes}]")
    logger.debug(f"batch_size: [{args.batch_size}]")
    logger.debug(f"linger_ms: [{args.linger_ms}]")
    logger.debug(f"min_interval: [{args.min_interval}]")
    logger.debug(f"delta_t: [{args.delta_t}]")

    framekafkaproducer = FrameKafkaProducer(args)

    # Sanity check input options
    if not os.path.exists(args.frame_directory):
        raise ValueError(
            "The frame directory does not exist.\
             Please provide a directory that exists."
        )

    if args.crc_check and not can_check_crc:
        raise ValueError("framel needs to be installed for CRC checks")

    # Setup queue to talk to the observer
    filenamequeue = queue.Queue()

    # Check if the watchdog module was found
    if watchdog_found:

        # Create the event handler
        event_handler = FrameFileEventHandler(filenamequeue)

        # Setup the observer to watch for new frame files
        observer = Observer()
        observer.schedule(
            event_handler,
            path=args.frame_directory,
        )
        observer.daemon = True
        observer.start()
    else:

        # Create the inotify handler
        observer = threading.Thread(
            target=monitor_dir_inotify,
            args=(filenamequeue, args.frame_directory)
        )

        # Start the observer and set the stop attribute
        observer.stop = False
        observer.start()

    # Mark start time
    start_time = time.time()

    while True:

        # Check if the runtime has gone above the max runtime
        runtime = time.time() - start_time
        if args.max_runtime and runtime > args.max_runtime:
            logger.info(
                "Have run for %f seconds stopping" % runtime
            )
            break

        # Get the next filename from the queue
        try:
            framefilename = filenamequeue.get(timeout=1)
        except queue.Empty:
            continue

        # Get the contents of the frame
        with open(framefilename, "rb") as f:
            frame_buffer = f.read()

        # Extract timestamp from the filename
        basefilename = ntpath.basename(framefilename)

        # If this is filename is correctly formatted the 3rd part when
        # split by "-" should be the timestamp
        tmp = basefilename.split("-")
        if len(tmp) != 4:
            raise IOError(
                "The frame filename is not correctly formatted"
                "the correct format is: \n"
                "\t <obs>-<tag>-<gps>-<dur>.[gwf,hdf5,h5]"
            )
        try:
            timestamp = int(tmp[2])
        except ValueError:
            raise IOError(
                "Could not turn the gps time in the frame is \
                it correctly formatted. The correct format is: \
                \t <obs>-<tag>-<gps>-<dur>.[gwf,hdf5,h5]"
            )

        # Do the crc check to confirm that this is a frame
        if args.crc_check:
            returncode = check_crc(frame_buffer)
            if returncode == 1:
                logger.warn(
                    "Topic:[%s] %d get %d %d CRC NOT FOUND. Dropping.",
                    args.topic,
                    gpstime.unix2gps(time.time()),
                    timestamp,
                    len(frame_buffer),
                )
            elif returncode == 2:
                logger.warn(
                    "Topic: [%s] %d get %d %d CRC FAILED. Dropping.",
                    args.topic,
                    gpstime.unix2gps(time.time()),
                    timestamp,
                    len(frame_buffer),
                )
        else:
            returncode = 0

        if returncode == 0:
            framekafkaproducer.send_frame(frame_buffer, timestamp)

        logger.debug(
            "gps:%i "
            "file timestamp %d "
            "latency:%0.3f "
            "unix:%0.3f "
            "send:%0.3f "
            "flush:%0.3f "
            "send+flush:%0.3f "
            "avg_rate_30s_MBs:%0.3f "
            "data_n:%d",
            framekafkaproducer.time_after_flush_gps,
            timestamp,
            framekafkaproducer.time_after_flush_gps - timestamp,
            framekafkaproducer.time_after_flush_unix,
            framekafkaproducer.time_before_flush_unix
            - framekafkaproducer.time_before_send_unix,
            framekafkaproducer.time_after_flush_unix
            - framekafkaproducer.time_before_flush_unix,
            framekafkaproducer.time_during_send_flush,
            framekafkaproducer.data_rate,
            framekafkaproducer.data_n,
        )

    # close
    framekafkaproducer.close()

    # Stop the observer
    if watchdog_found:
        observer.unschedule_all()
        observer.stop()
    else:
        observer.stop = True

    # Join the observer thread and wait for it to finish
    observer.join()


if __name__ == "__main__":
    sys.exit(main())

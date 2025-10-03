# -*- coding: utf-8 -*-
# Copyright (C) European Gravitational Observatory (EGO) (2022) and
# Laser Interferometer Gravitational-Wave Observatory (LIGO) (2022)
#
# Author list: Rhys Poulton <poulton@ego-gw.it>
#              Brockill <brockill@uwm.edu>
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

import argparse
from collections import defaultdict
import logging

from .utils import str2bool


def add_logging_options(parser):
    """Add logging client options to an argument parser."""
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="If set, only display warnings and errors.",
    )
    group.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="If set, display additional logging messages.",
    )


def add_status_update_options(parser):
    """Add parser arguments related to status updates."""
    parser.add_argument(
        "-su",
        "--status-updates",
        action="store_const",
        const=True,
        default=False,
        help="store status updates",
    )
    parser.add_argument(
        "-st",
        "--status-topic",
        type=str,
        help="topic name for status updates"
    )
    parser.add_argument(
        "-sb",
        "--status-bootstrap",
        type=str,
        help="specify the kafka cluster for status updates",
    )
    parser.add_argument(
        "-si",
        "--status-interval",
        type=int,
        default=60,
        help="interval in seconds between status updates",
    )
    parser.add_argument(
        "--status-timeout",
        type=float,
        default=0.05,
        help="maximum time to wait for status messages to be published",
    )
    parser.add_argument(
        "-sn",
        "--status-nodename",
        type=str,
        help="specify the node name used in status updates",
    )


def add_topic_partition_options(parser):
    """Add parser arguments related to topic partitions."""
    parser.add_argument(
        "-i",
        "--detector",
        "--ifo",
        dest="ifo",
        action="append",
        type=str,
        required=True,
        help="Detector (IFO) to process (e.g L1, V1, K1)",
    )
    parser.add_argument(
        "-t",
        "--topic",
        action=KeyValueParseAction,
        value_type=str,
        required=True,
        help="The topic",
    )
    parser.add_argument(
        "--delta-t",
        action=KeyValueParseAction,
        value_type=int,
        help="Make sure each frame comes in at delta_t seconds",
    )
    parser.add_argument(
        "--delta-t-fallback",
        action=KeyValueParseAction,
        value_type=int,
        help="Dynamically calculate frame length, use this value if cannot be \
found",
    )
    parser.add_argument(
        "--tag",
        action=KeyValueParseAction,
        value_type=str,
        help="The tag for the filename: <obs>-<tag>-<gps>-<dt>.gwf",
    )
    parser.add_argument(
        "-fd",
        "--frame-dir",
        action=KeyValueParseAction,
        value_type=str,
        required=True,
        help="Directory where the frames are written out to",
    )
    parser.add_argument(
        "--crc-check",
        action=KeyValueParseAction,
        value_type=str2bool,
        default=False,
        help="Run a CRC check for each frame",
    )
    parser.add_argument(
        "--max-latency",
        action=KeyValueParseAction,
        value_type=float,
        default=-1,
        help="maximum tolerated latency of data (s) (-1 for infinite)",
    )
    parser.add_argument(
        "--acceptable-latency",
        action=KeyValueParseAction,
        value_type=float,
        default=-1.0,
        help="when fast forwarding, first try to see if we can seek to data \
with this latency first before seek_to_end (-1 to ignore).",
    )
    parser.add_argument(
        "--fast-forward-buffer",
        action=KeyValueParseAction,
        value_type=float,
        default=5.0,
        help="amount to pause before seek_to_end when stream is behind \
max-latency",
    )
    parser.add_argument(
        "--max-kafka-latency",
        action=KeyValueParseAction,
        value_type=float,
        default=-1,
        help="maximum tolerated latency of data through Kafka broker (s) \
(-1 for infinite)",
    )


def get_log_level(args):
    """Determine the log level from logging options."""
    if args.quiet:
        return logging.WARNING
    elif args.verbose:
        return logging.DEBUG
    else:
        return logging.INFO


def extract_topic_partition_info(args, key_by_topic=False):
    """Extract topic-partition info from parser arguments."""
    # create parser with topic-partition args to determine which
    # arguments to iterate over
    parser = argparse.ArgumentParser()
    add_topic_partition_options(parser)
    tp_keys = [
        action.dest for action in parser._actions if action.dest != "help"
    ]

    # iterate through arguments
    tp_info = {}
    ifos = args.ifo
    keyed_args = vars(args)
    for key in tp_keys:
        tp_info[key] = keyed_args[key]

    # fill in extra info
    tp_info["extra_info"] = {ifo: {} for ifo in ifos}
    tp_info["extra_info_str"] = {ifo: [] for ifo in ifos}

    # fill in defaults
    # add tag, defaulting to topic
    for ifo in ifos:
        if tp_info["tag"][ifo] is None:
            tp_info["tag"][ifo] = tp_info["topic"][ifo]
    # add ifo key based on observatory
    tp_info["observatory"] = {ifo: ifo[0] for ifo in ifos}

    # rotate keys if requested
    if key_by_topic:
        tp_info_by_topic = {}
        topics = tp_info.pop("topic")
        tp_info.pop("ifo")
        for ifo in ifos:
            topic = topics[ifo]
            tp_info_by_topic[topic] = {
                key: opts[ifo] for key, opts in tp_info.items()
            }
            tp_info_by_topic[topic]["ifo"] = ifo
        tp_info = tp_info_by_topic

    return tp_info


class KeyValueParseAction(argparse.Action):
    """Argparse action to parse delimited key-value pairs."""

    def __init__(
        self,
        option_strings,
        dest,
        *,
        value_type,
        key_type=str,
        item_delimiter=",",
        key_delimiter="=",
        default=None,
        **kwargs,
    ):
        self._key_type = key_type
        self._value_type = value_type
        self._key_delimiter = key_delimiter
        self._item_delimiter = item_delimiter
        super().__init__(option_strings, dest, **kwargs)
        self.default = defaultdict(lambda: default)

    def __call__(self, parser, namespace, maybe_kv, option_string=None):
        # initialize
        items = getattr(namespace, self.dest, None)
        if items is None:
            items = {}

        # nothing to store
        if maybe_kv is None:
            pass
        # multiple key-value pairs
        elif self._item_delimiter in maybe_kv:
            for kv in maybe_kv.split(self._item_delimiter):
                k, v = kv.split(self._key_delimiter)
                items[self._key_type(k)] = self._value_type(v)
        # key-value pair
        elif self._key_delimiter in maybe_kv:
            k, v = maybe_kv.split(self._key_delimiter)
            items[self._key_type(k)] = self._value_type(v)
        # default value
        else:
            current = items.copy()
            items = defaultdict(lambda: self._value_type(maybe_kv))
            for k, v in current.items():
                items[k] = v
        setattr(namespace, self.dest, items)

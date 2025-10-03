import argparse

import pytest

from igwn_lldd_common import cli


@pytest.mark.parametrize(
    "input_cmd,expected",
    [
        ("--pairs 3", {"H1": 3, "L1": 3}),
        ("--pairs H1=2 --pairs L1=3", {"H1": 2, "L1": 3}),
        ("--pairs H1=2,L1=3", {"H1": 2, "L1": 3}),
    ],
)
def test_key_value_parse_action(input_cmd, expected):
    # set up parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pairs", action=cli.KeyValueParseAction, value_type=int
    )

    # parse and compare
    args = parser.parse_args(input_cmd.split())
    for input_k, input_v in args.pairs.items():
        assert input_k in expected, "extra key not found in expected result"
        expected_v = expected[input_k]
        assert input_v == expected_v, \
            "input value does not match expected result"


def test_extract_topic_partition_info():
    # Set the test topics
    topic1 = "test1"
    topic2 = "test2"

    # Create the topic dictionary
    topic_dict = {topic1: {}, topic2: {}}

    # Populate the first topic with relevant values
    topic_dict[topic2]["observatory"] = "V"
    topic_dict[topic2]["ifo"] = "V1"
    topic_dict[topic1]["delta_t"] = 1
    topic_dict[topic1]["delta_t_fallback"] = 2
    topic_dict[topic1]["crc_check"] = False
    topic_dict[topic1]["max_latency"] = 4.5
    topic_dict[topic1]["acceptable_latency"] = 3.6
    topic_dict[topic2]["frame_dir"] = "/tmp/kafka"

    # Populate the second topic with relevant values
    topic_dict[topic2]["observatory"] = "L"
    topic_dict[topic2]["ifo"] = "L1"
    topic_dict[topic2]["delta_t"] = 1
    topic_dict[topic2]["delta_t_fallback"] = 4
    topic_dict[topic2]["crc_check"] = False
    topic_dict[topic2]["max_latency"] = 6.5
    topic_dict[topic2]["acceptable_latency"] = 4.5
    topic_dict[topic2]["frame_dir"] = "/tmp/kafka"

    # add parser with relevant arguments
    parser = argparse.ArgumentParser()
    cli.add_topic_partition_options(parser)

    # define arguments and parse
    args = [
        "--detector", "L1",
        "--detector", "V1",
        "--topic", f"V1={topic1},L1={topic2}",
        "--delta-t", "1",
        "--delta-t-fallback", "V1=2,L1=4",
        "--crc-check", "false",
        "--max-latency", "V1=4.5,L1=6.5",
        "--acceptable-latency", "V1=3.6,L1=4.5",
        "--frame-dir", "/tmp/kafka",
    ]
    args = parser.parse_args(args)

    # extract topic-partition info and validate
    tp_info = cli.extract_topic_partition_info(args, key_by_topic=True)
    for topic in topic_dict.keys():
        for key in topic_dict[topic].keys():

            # First check this key exists in tp_info
            if key not in tp_info[topic].keys():
                raise AssertionError(
                    f"The key {key} is not in the topic info "
                    "from parse_topics"
                )

            assert topic_dict[topic][key] == tp_info[topic][key], (
                f"The value for {key} does not match the value in "
                "the topic info from parse_topics:\n"
                f"\t{topic_dict[topic][key]} != {tp_info[topic][key]}"
            )

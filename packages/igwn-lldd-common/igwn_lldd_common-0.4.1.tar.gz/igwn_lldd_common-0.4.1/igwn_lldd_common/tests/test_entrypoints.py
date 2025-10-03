import pytest
import sys

pytest.importorskip("pytest_console_scripts")


@pytest.mark.skipif(
    sys.version_info < (3, 7),
    reason="script runner requires python3.7 or higher",
)
def test_frame2kafka_help(script_runner):
    ret = script_runner.run(["frame2kafka", "--help"])
    assert ret.success


@pytest.mark.skipif(
    sys.version_info < (3, 7),
    reason="script runner requires python3.7 or higher",
)
def test_kafka2frame_help(script_runner):
    ret = script_runner.run(["kafka2frame", "--help"])
    assert ret.success

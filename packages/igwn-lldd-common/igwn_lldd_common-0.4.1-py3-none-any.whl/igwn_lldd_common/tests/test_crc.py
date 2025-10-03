from igwn_lldd_common.crc import check_crc
import pytest
from pathlib import Path

framel = pytest.importorskip("framel")

TEST_DATA_DIR = Path(__file__).parent / 'data'
TEST_GWF_FILE = 'Z-igwn_lldd_common_test-1000000000-1.gwf'


def test_check_crc():
    with open(TEST_DATA_DIR / TEST_GWF_FILE, "rb") as f:
        frame_buffer = f.read()
    returncode = check_crc(frame_buffer)
    assert returncode == 0

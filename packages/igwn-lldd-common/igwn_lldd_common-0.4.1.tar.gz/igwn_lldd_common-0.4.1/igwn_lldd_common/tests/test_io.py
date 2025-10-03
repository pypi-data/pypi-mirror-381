from collections import deque
import filecmp
import os
from pathlib import Path
import time

import pytest

from igwn_lldd_common.io import clean_old_frames, write_frame


TEST_DATA_DIR = Path(__file__).parent / "data"
TEST_GWF_FILE1 = "Z-igwn_lldd_common_test-1000000001-1.gwf"
TEST_GWF_FILE2 = "Z-igwn_lldd_common_test-1000000002-1.gwf"
TEST_GWF_OLD_FILE = "Z-igwn_lldd_common_test-1000000000-1.gwf"

# Read the data from the frame files
with open(TEST_DATA_DIR / TEST_GWF_FILE1, "rb") as f:
    FRAME_DATA1 = f.read()
with open(TEST_DATA_DIR / TEST_GWF_FILE2, "rb") as f:
    FRAME_DATA2 = f.read()


@pytest.mark.parametrize("use_tmpdir", [True, False])
def test_write_frame(tmp_path, use_tmpdir):
    # set up directories
    tmpdirname = tmp_path / "scratch"
    tmpdirname.mkdir()
    outdirname = tmp_path / "out"
    outdirname.mkdir()

    # write the frame
    tmpdir = tmpdirname if use_tmpdir else None
    filename = os.path.join(outdirname, TEST_GWF_FILE1)
    write_frame(filename, FRAME_DATA1, 300, deque(), tmpdir=tmpdir)

    # Check that output frame exists
    assert os.path.exists(
        filename
    ), f"Frame {filename} was not written to disk"

    # Compare the contents of the generated files
    assert filecmp.cmp(
        filename, TEST_DATA_DIR / TEST_GWF_FILE1
    ), f"The contents for {filename} does not match expected data"


def test_write_frame_with_length_retention(tmp_path):
    # frame writing directory
    outdirname = tmp_path / "out"
    outdirname.mkdir()

    # track frames for retention
    retention_length = 1
    frame_log = deque(maxlen=retention_length)

    # write the first frame
    filename1 = outdirname / TEST_GWF_FILE1
    write_frame(
        filename1,
        FRAME_DATA1,
        retention_length,
        frame_log,
    )

    # check that output frame exists and contents match
    assert os.path.exists(
        filename1
    ), f"Frame {filename1} was not written to disk"
    assert filecmp.cmp(
        filename1, TEST_DATA_DIR / TEST_GWF_FILE1
    ), f"The contents for {filename1} does not match expected data"

    # write a second frame
    filename2 = outdirname / TEST_GWF_FILE2
    write_frame(
        filename2,
        FRAME_DATA2,
        retention_length,
        frame_log,
    )

    # check that output frame exists and contents match
    assert os.path.exists(
        filename2
    ), f"Frame {filename2} was not written to disk"
    assert filecmp.cmp(
        filename2, TEST_DATA_DIR / TEST_GWF_FILE2
    ), f"The contents for {filename2} does not match expected data"

    # check that the first frame has been cleared out
    assert not os.path.exists(
        filename1
    ), f"Initial frame {filename1} was not cleaned"


def test_write_frame_with_time_retention(tmp_path):
    # frame writing directory
    outdirname = tmp_path / "out"
    outdirname.mkdir()

    # track frames for retention
    retention_length = None  # disable
    retention_time = 300  # 5 minutes
    frame_log = deque(maxlen=retention_length)

    # write the first frame
    filename1 = outdirname / TEST_GWF_FILE1
    write_frame(
        filename1,
        FRAME_DATA1,
        retention_length,
        frame_log,
        retention_time=retention_time,
    )

    # check that output frame exists and contents match
    assert os.path.exists(
        filename1
    ), f"Frame {filename1} was not written to disk"
    assert filecmp.cmp(
        filename1, TEST_DATA_DIR / TEST_GWF_FILE1
    ), f"The contents for {filename1} does not match expected data"

    # modify time of first frame outside of the time retention
    mod_time = int(time.time()) - 600  # 10 mins old
    os.utime(filename1, (mod_time, mod_time))

    # write a second frame
    filename2 = outdirname / TEST_GWF_FILE2
    write_frame(
        filename2,
        FRAME_DATA2,
        retention_length,
        frame_log,
        retention_time=retention_time,
    )

    # check that output frame exists and contents match
    assert os.path.exists(
        filename2
    ), f"Frame {filename2} was not written to disk"
    assert filecmp.cmp(
        filename2, TEST_DATA_DIR / TEST_GWF_FILE2
    ), f"The contents for {filename2} does not match expected data"

    # check that the first frame has been cleared out
    assert not os.path.exists(
        filename1
    ), f"Old frame {filename1} was not cleaned"


def test_clean_old_frames(tmp_path):
    # frame writing directory
    outdirname = tmp_path / "out"
    outdirname.mkdir()

    # frame tracking
    retention_length = None  # disable
    frame_log = deque()

    # write the first frame
    filename1 = outdirname / TEST_GWF_FILE1
    write_frame(
        filename1,
        FRAME_DATA1,
        retention_length,
        frame_log,
    )

    # modify time of first frame outside of the time retention
    mod_time = int(time.time()) - 600  # 10 mins old
    os.utime(filename1, (mod_time, mod_time))

    # write a second frame
    filename2 = outdirname / TEST_GWF_FILE2
    write_frame(
        filename2,
        FRAME_DATA2,
        retention_length,
        frame_log,
    )

    retention_time = 300  # 5 minutes
    clean_old_frames(outdirname, retention_time)

    # check that the first frame has been cleared out
    assert not os.path.exists(
        filename1
    ), f"Old frame {filename1} was not cleaned"

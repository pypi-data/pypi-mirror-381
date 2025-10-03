import multiprocessing as mp
import os
from igwn_lldd_common.frame2kafka import main as frame2kafka
from igwn_lldd_common.kafka2frame import main as kafka2frame
from pathlib import Path
import tempfile
import shutil
import time
import filecmp
import pytest


KAFKA_TOPIC1 = "TestTopic1"
KAFKA_TOPIC2 = "TestTopic2"
TEST_DATA_DIR = Path(__file__).parent / 'data'
TEST_GWF_FILES = [
    'Z-igwn_lldd_common_test-1000000000-1.gwf',
    'Z-igwn_lldd_common_test-1000000001-1.gwf',
    'Z-igwn_lldd_common_test-1000000002-1.gwf'
]
OLD_GWF_FILENAME = 'Z-igwn_lldd_common_test-999999999-1.gwf'
PRODUCER_RUNTIME = 5
RETENTION_TIME = 300  # 5 minutes
IFO1 = "Z1"
IFO2 = "X1"


@pytest.mark.skipif(
    os.getenv("KAFKA_BROKER") is None,
    reason="There is not a active Kafka Broker"
)
@pytest.mark.parametrize(
    "kafka_library",
    [["--load-kafka-python"], []],
)
def test_frame2kafka(kafka_library):
    with tempfile.TemporaryDirectory() as indirname:
        with tempfile.TemporaryDirectory() as outdirname:

            # add an old frame out of band to the output directory
            old_frame_file = Path(outdirname) / OLD_GWF_FILENAME
            shutil.copy(TEST_DATA_DIR / TEST_GWF_FILES[0], old_frame_file)
            mod_time = int(time.time()) - 2 * RETENTION_TIME
            os.utime(old_frame_file, (mod_time, mod_time))

            consumer_args = [
                "--bootstrap-servers", os.getenv("KAFKA_BROKER"),
                "--ifo", IFO1,
                "--ifo", IFO2,
                "--frame-dir", outdirname,
                "--topic", f"{IFO1}={KAFKA_TOPIC1}",
                "--topic", f"{IFO2}={KAFKA_TOPIC2}",
                "--delta-t", "1",
                "--debug", "1",
                "--max-runtime", "30",
                "--retention-time", str(RETENTION_TIME),
                *kafka_library,
            ]

            # Setup the consumer using the frame2kafka script
            consumer = mp.Process(target=kafka2frame, args=(consumer_args,))

            # Start the consumer
            consumer.start()

            time.sleep(5)

            producer1_args = [
                "--bootstrap-servers", os.getenv("KAFKA_BROKER"),
                "--frame-directory", indirname,
                "--topic", KAFKA_TOPIC1,
                "--verbose", "True",
                "--max-runtime", "20",
                *kafka_library,
            ]

            # Setup the producer using the frame2kafka script
            producer1 = mp.Process(target=frame2kafka, args=(producer1_args,))

            # Start the producer
            producer1.start()

            producer2_args = [
                "--bootstrap-servers", os.getenv("KAFKA_BROKER"),
                "--frame-directory", indirname,
                "--topic", KAFKA_TOPIC2,
                "--verbose", "True",
                "--max-runtime", "20",
                *kafka_library,
            ]

            # Setup the producer using the frame2kafka script
            producer2 = mp.Process(target=frame2kafka, args=(producer2_args,))

            # Start the producer
            producer2.start()

            # Allow the producer to startup before writing frames
            time.sleep(5)

            # Loop over each of the test files reading them and
            # writing them to the tmp directory so they can be picked
            # up by the frame2kafka process
            for ifile in TEST_GWF_FILES:

                # Copy the file to the dest directory so it can be picked
                # up by the producer
                inputfile = TEST_DATA_DIR / ifile
                destfile = os.path.join(indirname, ifile)

                # Copy the file
                shutil.copyfile(inputfile, destfile)

                # Wait 1 second so the file comes in every 1 second
                time.sleep(1)

            # Wait for the producers to stop
            producer1.join()
            producer2.join()

            # Wait for the consumer to stop
            consumer.join()

            print(os.listdir(indirname))
            print(os.listdir(outdirname))

            # check frames produced
            for ifile in TEST_GWF_FILES:

                # Set the filenames to check the file contents
                infile = os.path.join(indirname, ifile)
                ofile1 = ifile.replace(
                    "Z-igwn_lldd_common_test",
                    f"{IFO1[0]}-{KAFKA_TOPIC1}"
                )
                outfile1 = os.path.join(outdirname, ofile1)
                ofile2 = ifile.replace(
                    "Z-igwn_lldd_common_test",
                    f"{IFO2[0]}-{KAFKA_TOPIC2}"
                )
                outfile2 = os.path.join(outdirname, ofile2)

                # Check that the infile and outfile
                assert os.path.exists(infile), f"The copy of {infile} failed"
                assert os.path.exists(outfile1), "The consumer did not " \
                    f"write {outfile1}"
                assert os.path.exists(outfile2), "The consumer did not " \
                    f"write {outfile2}"

                # Compare the contents of the generated files
                assert filecmp.cmp(infile, outfile1), "The contents for " \
                    f"the {infile} and {outfile1} do not match"
                assert filecmp.cmp(infile, outfile2), "The contents for " \
                    f"the {infile} and {outfile2} do not match"

            # check that old frame was cleaned out
            assert not os.path.exists(
                old_frame_file
            ), f"Old frame {old_frame_file} was not cleaned"

import os
import logging
import shutil
import time

logger = logging.getLogger(__name__)

DEFAULT_EXTENSIONS = {".gwf", ".hdf5", ".h5"}

try:
    from watchdog.events import PatternMatchingEventHandler

    class FrameFileEventHandler(PatternMatchingEventHandler):
        def __init__(self, queue):
            super().__init__(patterns=["*.gwf", "*.hdf5", "*.h5"])
            self.queue = queue

        def on_closed(self, event):
            if event.is_directory:
                return
            self._handle_event(event.src_path)

        def on_moved(self, event):
            if event.is_directory:
                return
            self._handle_event(event.dest_path)

        def _handle_event(self, path):
            extension = os.path.splitext(path)[1]
            if extension not in DEFAULT_EXTENSIONS:
                return
            self.queue.put(path)

except ImportError:
    import threading
    from inotify_simple import INotify, flags

    # Thread to watch over watch_dir
    def monitor_dir_inotify(queue, watch_dir):
        # create a watcher thread watching for write or moved events
        i = INotify()
        i.add_watch(watch_dir, flags.CLOSE_WRITE | flags.MOVED_TO)

        # Get the current thread
        t = threading.currentThread()

        # Check if this thread should stop
        while not t.stop:
            # Loop over the events and check when a file has been created
            for event in i.read(timeout=1):
                # directory was removed, so the corresponding watch was
                # also removed
                if flags.IGNORED in flags.from_mask(event.mask):
                    break

                # ignore temporary files
                filename = event.name
                extension = os.path.splitext(filename)[1]
                if extension not in DEFAULT_EXTENSIONS:
                    continue

                # Add the filename to the queue
                queue.put(os.path.join(watch_dir, filename))

        # Remove the watch
        i.rm_watch(watch_dir)


def clean_old_frames(frame_dir, retention_time):
    """Remove frames in directory older than retention time specified."""
    # no-op if retention policy not set
    if not retention_time:
        return

    current_time = time.time()
    with os.scandir(frame_dir) as it:
        for entry in it:
            extension = os.path.splitext(entry.name)[1]
            if extension == ".gwf":
                remove_old_file(entry.path, current_time, retention_time)


def write_frame(
    file_name,
    frame_data,
    fl_ringn,
    file_name_dq,
    tmpdir=None,
    retention_time=None,
    unsafe=None,
):
    if unsafe is None:
        unsafe = os.getenv("LLDD_WRITE_UNSAFE", False)

    # write frame to disk
    if unsafe:
        with open(file_name, "wb") as f:
            f.write(frame_data)
    else:
        # determine temporary filename/directory
        if tmpdir:
            file = os.path.basename(file_name)
        elif "LLDD_TMPDIR" in os.environ:
            tmpdir = os.getenv("LLDD_TMPDIR")
            file = os.path.basename(file_name)
        else:
            tmpdir, file = os.path.split(file_name)
        tmp_file_name = os.path.join(tmpdir, f".{file}.tmp")

        # write frame
        # NOTE: this is atomic if on the same filesystem
        with open(tmp_file_name, "wb") as f:
            f.write(frame_data)
            # ensure all data is on disk
            f.flush()
            os.fsync(f.fileno())
        shutil.move(tmp_file_name, file_name)

    # length-based (ringn) retention
    if fl_ringn:
        #
        # name queue full?
        if len(file_name_dq) == fl_ringn:
            old_file = file_name_dq.popleft()
            try:
                os.unlink(old_file)
            except OSError:
                logger.error(f"Error: could not delete file [{old_file}]")

    # time-based retention
    if retention_time:
        current = time.time()
        while len(file_name_dq) and (
            remove_old_file(file_name_dq[0], current, retention_time)
        ):
            file_name_dq.popleft()

    # add this file to queue if needed
    if fl_ringn or retention_time:
        file_name_dq.append(file_name)


def remove_old_file(file_, current_time, retention_time):
    """Removes file if it meets criteria for removal according to retention.

    Also returns whether this file matched the criteria for removal.
    """
    try:
        mod_time = os.path.getmtime(file_)
    except FileNotFoundError:
        return True
    else:
        is_old = retention_time and (current_time - mod_time) > retention_time
        if is_old:
            try:
                os.unlink(file_)
            except FileNotFoundError:
                pass
            except OSError:
                logger.error(f"Error: could not delete file [{file_}]")
        return is_old

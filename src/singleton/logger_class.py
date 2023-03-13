import errno
import os
import pathlib


def if_dir_exists():
    parent_f = pathlib.Path(__file__).parent.resolve()
    filename = str(parent_f) + "/log/filename.log"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


class Logger(object):
    """A file-based message logger with the following properties
      Attributes:
        file_name: a string representing the full path of the log file to which
    this logger will write its messages
      """
    def __init__(self, file_name):
        """Return a Logger object whose file_name is *file_name*"""
        self.file_name = file_name

    def _write_log(self, level, msg):
        """Writes a message to the file_name for a specific Logger instance"""
        if_dir_exists()
        with open(self.file_name, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, level, msg):
        self._write_log("CRITICAL", msg)

    def error(self, level, msg): self._write_log("ERROR", msg)

    def warn(self, level, msg): self._write_log("WARN", msg)

    def info(self, level, msg): self._write_log("INFO", msg)

    def debug(self, level, msg): self._write_log("DEBUG", msg)

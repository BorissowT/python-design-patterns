import errno
import os
import pathlib


class LoggerSingleton(object):
    """

    we have only one class instance. if we create another class we rewrite
    a previous instance.
    """

    instance = None

    class __LoggerSingleton:

        parent_f = pathlib.Path(__file__).parent.resolve()

        def __init__(self, file_name):
            self.file_name = file_name

        def __str__(self):
            return f"logger with storage at {self.file_name}"

        def if_dir_exists(self):

            filename = str(self.parent_f) + "/log/"+self.file_name
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

        def _write_log(self, level, msg):
            """Writes a message to the file_name for a specific Logger
            instance"""
            self.if_dir_exists()
            with open(
                    str(self.parent_f)+"/log/"+self.file_name, "a"
            ) as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg): self._write_log("ERROR", msg)

        def warn(self, msg): self._write_log("WARN", msg)

        def info(self, msg): self._write_log("INFO", msg)

        def debug(self, msg): self._write_log("DEBUG", msg)

    def __new__(cls, file_name):
        if not LoggerSingleton.instance:
            LoggerSingleton.instance = \
                LoggerSingleton.__LoggerSingleton(file_name)
        return LoggerSingleton.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

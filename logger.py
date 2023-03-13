import errno
import os
import pathlib


parent_f = pathlib.Path(__file__).parent.resolve()


def locate_log_dir(func):

    def wrapper_func(*args, **kwargs):
        parent_f = pathlib.Path(__file__).parent.resolve()
        filename = str(parent_f) + "/log/filename.log"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        func(*args, **kwargs)
    return wrapper_func


@locate_log_dir
def log_message(msg):
    with open(str(parent_f) + "/log/filename.log", "a") as log_file:
        log_file.write("{0}\n".format(msg))

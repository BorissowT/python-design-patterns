import errno
import os
import pathlib
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    parent_f = pathlib.Path(__file__).parent.resolve()

    @abstractmethod
    def clone(self):
        pass

    def if_dir_exists(self, filename):
        filename = str(self.parent_f) + "/data/" + filename
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    def read_from_file(self, filename):
        self.if_dir_exists(filename)
        with open(str(self.parent_f) + "/data/" + filename, 'r')\
                as parameter_file:
            return parameter_file.read().split("\n")
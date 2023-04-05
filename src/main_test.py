from typing import Type


class ClassInstance:
    def __init__(self, input_msg):
        print(input_msg)


class TestClass:
    matcher = ClassInstance


t = TestClass()


def func(t):
    matcher = t.matcher("ggg")

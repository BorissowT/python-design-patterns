"""
Facade pattern.
"""


class SubSystemClassA:
    @staticmethod
    def method():
        return 'A'


class SubSystemClassB:
    @staticmethod
    def method():
        return 'B'


class SubSystemClassC:
    @staticmethod
    def method():
        return 'C'


class Facade:
    def __init__(self):
        self.sub_system_class_a = SubSystemClassA()
        self.sub_system_class_b = SubSystemClassB()
        self.sub_system_class_c = SubSystemClassC()

    def create(self):
        return self.sub_system_class_a.method() + \
               self.sub_system_class_b.method() + \
               self.sub_system_class_c.method()


FACADE = Facade()
RESULT = FACADE.create()
print(RESULT)

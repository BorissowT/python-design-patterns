from prototype_1 import Prototype
from copy import deepcopy


""" prototype pattern is useful when you have to create multiple the same 
instances with the same data. So whenever you need a new object you don't have 
to initiate a new object you just call "clone" to already initiated object

    1. define prototypeBase class with copy() method
    2. inherit prototype. overwrite clone() method
    
"""

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"
        filename = "{}_{}.dat".format(self.unit_type, level)
        lines = self.read_from_file(filename)
        self.life = lines[0]
        self.speed = lines[1]
        self.attack_power = lines[2]
        self.attack_range = lines[3]
        self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
                    "Life: {1}\n" \
                    "Speed: {2}\n" \
                    "Attack Power: {3}\n" \
                    "Attack Range: {4}\n" \
                    "Weapon: {5}".format(
               self.unit_type,
               self.life,
               self.speed,
               self.attack_power,
               self.attack_range,
               self.weapon
        )

    def clone(self):
        return deepcopy(self)


class Archer(Prototype):

    def __init__(self, level):
        self.unit_type = "Archer"
        filename = "{}_{}.dat".format(self.unit_type, level)
        lines = self.read_from_file(filename)
        self.life = lines[0]
        self.speed = lines[1]
        self.attack_power = lines[2]
        self.attack_range = lines[3]
        self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
                "Life: {1}\n" \
                "Speed: {2}\n" \
                "Attack Power: {3}\n" \
                "Attack Range: {4}\n" \
                "Weapon: {5}".format(
        self.unit_type,
        self.life,
        self.speed,
        self.attack_power,
        self.attack_range,
        self.weapon
    )

    def clone(self):
        return deepcopy(self)


class Barracks(object):
    def __init__(self):
        self.units = {
            "knight": {1: Knight(1), 2: Knight(2)},
            "archer": {1: Archer(1), 2: Archer(2)}
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 2)
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))

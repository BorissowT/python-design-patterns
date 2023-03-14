class Knight(object):
    def __init__(self, life, speed, attack_range, attack_power, weapon):
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return "Life: {0}\n" \
               "Speed: {1}\n" \
               "Attack Power: {2}\n" \
               "Attack Range: {3}\n" \
               "Weapon: {4}".format(
            self.life,
            self.speed,
            self.attack_power,
            self.attack_range,
            self.weapon
        )


class Archer(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Archer"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return "Type: {0}\n Life: {1}\n" \
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


class Barracks(object):

    @staticmethod
    def generate_knight():
        return Knight(400, 5, 3, 1, "short sword")

    @staticmethod
    def generate_archer():
        return Archer(200, 7, 1, 5, "short bow")




if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    archer1 = barracks.generate_archer()
    print("[knight1] {}".format(knight1))
    print("[archer1] {}".format(archer1))

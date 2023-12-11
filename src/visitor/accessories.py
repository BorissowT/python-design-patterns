import random


class Light(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.get_status() != -1

    def boot_up(self):
        self.status = 0


class Thermostat(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        temp_range = [x for x in range(-10, 31)]
        temp_range.append(None)
        return random.choice(temp_range)

    def is_online(self):
        return self.get_status() is not None

    def boot_up(self):
        pass


class TemperatureRegulator(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(['heating', 'cooling', 'on', 'off', 'error'])

    def is_online(self):
        return self.get_status() != 'error'

    def boot_up(self):
        self.status = 'on'


class DoorLock(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.get_status() != -1

    def boot_up(self):
        pass


class CoffeeMachine(object):
    def __init__(self, name: object):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 5))

    def is_online(self):
        return self.get_status() != -1

    def boot_up(self):
        self.status = 1


class Clock(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return "{}:{}".format(random.randrange(24), random.randrange(60))

    def is_online(self):
        return True

    def boot_up(self):
        self.status = "00:00"


def main():
    device_network = [
        Thermostat("General Thermostat"),
        TemperatureRegulator("Thermal Regulator"),
        DoorLock("Front Door Lock"),
        CoffeeMachine("Coffee Machine"),
        Light("Bedroom Light"),
        Light("Kitchen Light"),
        Clock("System Clock"),
    ]

    for device in device_network:
        print("{} is online: \t{}".format(device.name, device.is_online()))


if __name__ == "__main__":
    main()

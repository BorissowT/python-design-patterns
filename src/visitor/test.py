import unittest

from src.visitor.accessories import Thermostat, TemperatureRegulator, \
    CoffeeMachine, DoorLock, Light, Clock


class HomeAutomationBootTests(unittest.TestCase):
    def setUp(self):
        self.thermostat = Thermostat("General Thermostat")
        self.thermal_regulator = TemperatureRegulator("Thermal Regulator")
        self.front_door_lock = DoorLock("Front Door Lock")
        self.coffee_machine = CoffeeMachine("Coffee Machine")
        self.bedroom_light = Light("Bedroom Light")
        self.system_clock = Clock("System Clock")

    def test_boot_thermostat_does_nothing_to_state(self):
        state_before = self.thermostat.status
        self.thermostat.boot_up()
        self.assertEqual(state_before, self.thermostat.status)

    def test_boot_thermal_regulator_turns_it_on(self):
        self.thermal_regulator.boot_up()
        self.assertEqual(self.thermal_regulator.status, 'on')

    def test_boot_front_door_lock_does_nothing_to_state(self):
        state_before = self.front_door_lock.status
        self.front_door_lock.boot_up()
        self.assertEqual(state_before, self.front_door_lock.status)

    def test_boot_coffee_machine_turns_it_on(self):
        self.coffee_machine.boot_up()
        self.assertEqual(self.coffee_machine.status, 1)

    def test_boot_light_turns_it_off(self):
        self.bedroom_light.boot_up()
        self.assertEqual(self.bedroom_light.status, 0)

    def test_boot_system_clock_zeros_it(self):
        self.system_clock.boot_up()
        self.assertEqual(self.system_clock.status, "00:00")


if __name__ == "__main__":
    unittest.main()

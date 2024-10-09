import unittest
from air_conditioner import AirConditioner

class TestAirConditioner(unittest.TestCase):
    def setUp(self):
        ac = AirConditioner()

    def test_AC_can_turn_on(self):
        ac = AirConditioner()
        ac.turn_off()
        self.assertFalse(ac.turn_off())
        ac.turn_on()
        self.assertTrue(ac.turn_on())

    def test_AC_can_turn_off(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.turn_on())
        ac.turn_off()
        self.assertFalse(ac.turn_off())

    def test_ac_can_increase_temperature(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.turn_on())
        ac.get_temperature()
        self.assertEqual(ac.get_temperature(), 16)
        ac.increase_temperature()
        self.assertEqual(ac.get_temperature(), 17)

    def test_ac_can_decrease_temperature(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.turn_on())
        ac.get_temperature()
        self.assertEqual(ac.get_temperature(), 16)
        for _ in range(4):
            ac.increase_temperature()
        self.assertEqual(ac.get_temperature(), 20)
        ac.decrease_temperature()
        self.assertEqual(ac.get_temperature(), 19)

    def test_ac_temperature_cannot_go_beyond_30(self):
        ac = AirConditioner()
        self.assertTrue(ac.turn_on())
        self.assertEqual(ac.get_temperature(), 16)
        for _ in range(14):
            ac.increase_temperature()
        self.assertEqual(ac.get_temperature(), 30)
        ac.increase_temperature()
        self.assertEqual(ac.get_temperature(), 30)

    def test_ac_temperature_cannot_go_below_16(self):
        ac = AirConditioner()
        self.assertTrue(ac.turn_on())
        self.assertEqual(ac.get_temperature(), 16)
        ac.decrease_temperature()
        self.assertEqual(ac.get_temperature(), 16)
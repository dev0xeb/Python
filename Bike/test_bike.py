import unittest
from Bike import Bike

class TestBike(unittest.TestCase):
    def test_bike_can_turn_on(self):
        bike = Bike()
        expected = bike.turn_on()
        self.assertTrue(expected)

    def test_bike_can_turn_off(self):
        bike = Bike()
        bike.turn_on()
        bike.turn_off()
        self.assertFalse(bike.turn_off())

    def test_accerlerate_in_gear_one(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 1)

    def test_bike_can_change_to_gear_2(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)

    def test_accelerate_in_gear_2(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 23)

    def test_bike_can_change_to_gear_3_and_accelerate_by_3(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        for _ in range(5):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 31)
        self.assertEqual(bike.get_gear(), 3)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 34)

    def test_bike_can_change_to_gear_4_and_accelerate_by_4(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        for _ in range(5):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 31)
        self.assertEqual(bike.get_gear(), 3)
        for _ in range(4):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 43)
        self.assertEqual(bike.get_gear(), 4)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 47)

    def test_bike_can_deccelerate_in_gear_one(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(16):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 16)
        self.assertEqual(bike.get_gear(), 1)
        bike.decelerate()
        self.assertEqual(bike.get_speed(), 15)

    def test_bike_can_decelerate_in_gear_2(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        for _ in range(3):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 27)
        bike.decelerate()
        self.assertEqual(bike.get_speed(), 25)

    def test_bike_can_decelerate_in_gear_3(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        for _ in range(5):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 31)
        self.assertEqual(bike.get_gear(), 3)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 34)
        bike.decelerate()
        self.assertEqual(bike.get_speed(), 31)

    def test_bike_can_decelerate_in_gear_4(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        for _ in range(5):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 31)
        self.assertEqual(bike.get_gear(), 3)
        for _ in range(4):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 43)
        self.assertEqual(bike.get_gear(), 4)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 47)
        bike.decelerate()
        self.assertEqual(bike.get_speed(), 43)

    def test_speed_cannot_go_below_0_while_decelerating(self):
        bike = Bike()
        self.assertTrue(bike.turn_on())
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        for _ in range(22):
            bike.decelerate()
        self.assertEqual(bike.get_speed(), 0)

    def test_speed_cannot_go_beyond_80_while_accelerating(self):
        bike = Bike()
        bike.turn_on()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        for _ in range(5):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 31)
        self.assertEqual(bike.get_gear(), 3)
        for _ in range(4):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 43)
        self.assertEqual(bike.get_gear(), 4)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 47)
        for _ in range(8):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 79)
        self.assertEqual(bike.get_gear(), 4)
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 79)

    def test_gear_changes_during_deceleration(self):
        bike = Bike()
        self.assertTrue(bike.turn_on())
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 1)
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 21)
        self.assertEqual(bike.get_gear(), 2)
        for _ in range(5):
            bike.decelerate()
        self.assertEqual(bike.get_speed(), 15)
        self.assertEqual(bike.get_gear(), 1)
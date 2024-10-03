import unittest
from imghdr import tests

from television_app.television import Television

class TestTelevision(unittest.TestCase):

    def test_television_can_turn_on(self):
        television = Television()
        expected = television.turn_on()
        self.assertTrue(expected)

    def test_television_is_off(self):
        television = Television()
        television.turn_on()
        television.turn_off()
        self.assertFalse(television.turn_off())

    def test_television_is_on_channel_is_1(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())

    def test_television_channel_can_increase(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        self.assertEqual(2, television.set_channel(2))

    def test_television_channel_can_decrease(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        television.set_channel(2)
        television.channel_down()
        self.assertEqual(1, television.get_channel())

    def test_television_channel_cannot_go_below_1(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        self.assertRaises(ValueError, television.set_channel, 0)

    def test_television_channel_cannot_go_above_100(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        self.assertRaises(ValueError, television.set_channel, 101)

    def test_television_volume_when_on(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        self.assertEqual(1, television.get_volume())

    def test_television_volume_can_increase(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        television.set_volume(10)
        self.assertEqual(10, television.get_volume())

    def test_television_volume_can_decrease(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        television.set_volume(0)
        self.assertEqual(0, television.get_volume())

    def test_television_volume_cannot_go_above_100(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        self.assertRaises(ValueError, television.set_volume, 101)

    def test_television_volume_cannot_go_below_0(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        self.assertRaises(ValueError, television.set_volume, -1)

    def test_television_cannot_display_channel_when_off(self):
        television = Television()
        television.turn_on()
        television.turn_off()
        self.assertFalse(television.turn_off())
        self.assertRaises(ValueError, television.set_channel, 2)

    def test_television_cannot_produce_sound_when_off(self):
        television = Television()
        television.turn_on()
        self.assertTrue(television.turn_on())
        television.turn_off()
        self.assertFalse(television.turn_off())
        self.assertRaises(ValueError, television.set_volume, 57)

    def test_television_mute_volume_when_on(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        television.set_volume(75)
        self.assertTrue(True, television.is_mute())

    def test_television_can_unmute(self):
        television = Television()
        television.turn_on()
        television.get_channel()
        self.assertEqual(1, television.get_channel())
        television.set_volume(45)
        self.assertFalse(False, television.unmute())

if __name__ == '__main__':
    unittest.main()

import unittest

from pythonclasswork import task28


class TestTask28(unittest.TestCase):
    def test_28_function(self):
        task28.listortuple("34,67,55,33,12,98")

    def test_task28_returns_list(self):
        expected = task28.listortuple("34,67,55,33,12,98")
        self.assertEqual(expected, "['34', '67', '55', '33', '12', '98']('34', '67', '55', '33', '12', '98')")
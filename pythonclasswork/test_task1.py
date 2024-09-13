import unittest
import task1
class TestTask1(unittest.TestCase):

    def test_task1_function(self):
        task1.concatonate_2_strings("abc", "xyz")

    def test_task1_concatonate_2_strings(self):
        expected = task1.concatonate_2_strings('abc', 'xyz')
        self.assertEqual(expected, 'xyc abz')

    def test_task1_function2(self):
      task1.add_ce_to_string('talk', 'ce')

    def test_task1_add_ce_to_middle_if_length_is_divisible_equally(self):
        expected = task1.add_ce_to_string('talk', 'ce')
        self.assertEqual(expected, 'tacelk')

    def test_task1_add_ce_to_end_if_length_cant_be_divisible_equally(self):
        expected = task1.add_ce_to_string('tin', 'ce')
        self.assertEqual(expected, 'tince')

    def test_task1_function4(self):
        task1.number_of_occurence_in_a_tuple('Clinton', 'n')

    def test_task1_number_of_occurence_in_a_tuple(self):
        expected = task1.number_of_occurence_in_a_tuple('Clinton', 'n')
        self.assertEqual(expected, ('n', '2'))

    def test_task1_number_of_occurence_of_more_2(self):
        expected = task1.number_of_occurence_in_a_tuple('cookor', 'o')
        self.assertEqual(expected, ('o', '3'))

    def test_task1_function5(self):
        task1.remove_special_character("he,ll.o")

    def test_function6_removes_special_character(self):
        expected = task1.remove_special_character("he,ll.o")
        self.assertEqual(expected, "hello")
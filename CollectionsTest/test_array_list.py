from unittest import TestCase

from Collections.array_list import ArrayList
class TestArrayList(TestCase):
    def setUp(self):
        self.list = ArrayList()

    def testIfListIsEmpty(self):
        self.assertTrue(self.list.is_empty())

    def testAddACheckListIsNotEmpty(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.assertFalse(self.list.is_empty())

    def testAddAnElementAtTheEndOfTheList(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.assertTrue(self.list.add_at_end("Peter"))

    def testAddABCRemoveElementAtIndex1CheckListSize(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.list.remove_by_index(1)
        self.assertEqual(2, self.list.get_size())

    def testAddABCRemoveElementByContentCheckListSize(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.assertTrue(self.list.remove_by_element("David"))

    def testRemoveByIndexWheListIsEmpty(self):
        self.assertTrue(self.list.is_empty())
        self.assertRaises(ValueError, lambda: self.list.remove_by_index(1))

    def testRemoveByElementWhenListIsEmpty(self):
        self.assertTrue(self.list.is_empty())
        self.assertRaises(ValueError, lambda: self.list.remove_by_element("Peter"))

    def testIfListContainsAnElement(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.assertTrue(self.list.contains("David"))

    def testContainsOnEmptyList(self):
        self.assertTrue(self.list.is_empty())
        self.assertRaises(ValueError, lambda: self.list.contains("Peter"))

    def testAddMoreThanListCapacity(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.assertRaises(IndexError, lambda: self.list.add(3, "Peter"))

    def testGetElementByIndex(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.assertEqual("Jim", self.list.get(2))

    def testCheckGetOnEmptyList(self):
        self.assertTrue(self.list.is_empty())
        self.assertRaises(ValueError, self.list.get, 0)

    def testRemoveAnElementThatDoesNotExist(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.assertFalse(self.list.remove_by_element("Faith"))

    def testClearAllElements(self):
        self.assertTrue(self.list.is_empty())
        self.list.add(0, "Clinton")
        self.list.add(1, "David")
        self.list.add(2, "Jim")
        self.list.clear()
        self.assertTrue(self.list.is_empty())
        self.assertEqual(0, self.list.get_size())

    def testGetAnElementAtNegativeIndex(self):
        self.assertTrue(self.list.is_empty())
        self.assertRaises(ValueError, self.list.get, -1)
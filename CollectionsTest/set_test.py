import unittest

from Collections.set import Set

class SetTest(unittest.TestCase):
    def setUp(self):
        self.set = Set(3)

    def testSetIsEmpty(self):
        self.assertTrue(self.set.is_empty())

    def testAddACheckSetIsNotEmpty(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertFalse(self.set.is_empty())

    def testAddARemoveACheckSetIsEmpty(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.remove("Clinton"))
        self.assertTrue(self.set.is_empty())

    def testAddABRemoveBCheckSetIsEmpty(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.remove("David"))
        self.assertFalse(self.set.is_empty())

    def testAddUntilSetIsFull(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.add("Emily"))
        self.assertTrue(self.set.is_full())

    def testAddElementToAFullSet(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.add("Emily"))
        self.assertTrue(self.set.is_full())
        self.assertRaises(ValueError, self.set.add, "Ayoade")

    def testRemoveFromEmptySet(self):
        self.assertTrue(self.set.is_empty())
        self.assertRaises(ValueError, self.set.remove, "Clinton")

    def testCheckIfRemovedElementsNoLongerExists(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.add("Emily"))
        self.assertTrue(self.set.remove("Emily"))
        self.assertFalse(self.set.contains("Emily"))
        self.assertTrue(self.set.remove("Clinton"))
        self.assertFalse(self.set.contains("Clinton"))

    def testRemoveElementsThatDoesNoteExistInSet(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertFalse(self.set.remove("Peter"))

    def testCheckIfSetCanTakeInDuplicateElements(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertRaises(ValueError, self.set.add, "Clinton")

    def testCheckIfSetCanAddMoreThanCapacity(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.add("Emily"))
        self.assertRaises(ValueError, self.set.add, "Peter")

    def testCheckSetCurrentSize(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.add("Emily"))
        self.assertEqual(3, self.set.get_size())

    def testSetContainsAParticularElement(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.add("Emily"))
        self.assertTrue(self.set.contains("David"))

    def testCheckIfSetContainsAnElementWhwnEmpty(self):
        self.assertTrue(self.set.is_empty())
        self.assertRaises(ValueError, self.set.contains, "Clinton")

    def testCheckIfSetDoesNotContainAParticularElement(self):
        self.assertTrue(self.set.is_empty())
        self.set.add("Clinton")
        self.set.add("David")
        self.set.add("Emily")
        self.assertFalse(self.set.contains("Peter"))

    def testClearAllElementsInASet(self):
        self.assertTrue(self.set.is_empty())
        self.assertTrue(self.set.add("Clinton"))
        self.assertTrue(self.set.add("David"))
        self.assertTrue(self.set.add("Emily"))
        self.assertTrue(self.set.is_full())
        self.set.clear()
        self.assertTrue(self.set.is_empty())
        self.assertEqual(0, self.set.get_size())

    def testClearOnEmptySet(self):
        self.assertTrue(self.set.is_empty())
        self.set.clear()
        self.assertTrue(self.set.is_empty())
        self.assertEqual(0, self.set.get_size())
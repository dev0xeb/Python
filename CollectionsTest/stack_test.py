import unittest

from Collections.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def testIfStackIsEmpty(self):
        self.assertTrue(self.stack.is_empty())

    def testPushXCheckIfStackIsEmpty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.assertFalse(self.stack.is_empty())

    def testPushYPopYCheckIfStackIsEmpty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def testPushXYPopYCheckIfStackIsNotEmpty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.stack.pop()
        self.assertFalse(self.stack.is_empty())

    def testPushXYZCheckStackIsFull(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.stack.push("David")
        self.assertEqual(3, self.stack.get_size())
        self.assertTrue(self.stack.is_full())

    def testPushXYCheckStackIsNotFull(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.assertFalse(self.stack.is_full())

    def testPushMoreThanStackCapacity(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.stack.push("David")
        self.assertRaises(ValueError,self.stack.push, "Clinton")

    def testPopAnEmptyStack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertRaises(ValueError, self.stack.pop)

    def testPushXGetStackSize(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.assertEqual(1, self.stack.get_size())

    def testPopAllElementsToCheckIfStackIsEmpty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.stack.push("David")
        self.assertEqual(3, self.stack.get_size())
        self.assertTrue(self.stack.is_full())
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def testStackCapacityIsConstant(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(3, self.stack.capacity)
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.assertEqual(2, self.stack.get_size())
        self.assertEqual(3, self.stack.capacity)

    def testPushXYPopYPushZAndSizeIs2(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.stack.pop()
        self.stack.push("David")
        self.assertEqual(2, self.stack.get_size())

    def testStackCanPeekAMostRecentElement(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.assertEqual("Ayoade", self.stack.peek())
        self.stack.pop()
        self.assertEqual("Clinton", self.stack.peek())

    def testPeekEmptyStack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertRaises(ValueError, self.stack.peek)

    def testStackToReturnIndexOfSearchedElement(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Clinton")
        self.stack.push("Ayoade")
        self.stack.push("David")
        self.assertEqual(0, self.stack.search("Clinton"))
        self.assertEqual(2, self.stack.search("David"))

    def testSearchEmptyStack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertRaises(ValueError, self.stack.search, "Clinton")
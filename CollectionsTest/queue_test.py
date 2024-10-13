import unittest

from Collections.queue import Queue
class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def testQueueIsEmpty(self):
        self.assertTrue(self.queue.is_empty())

    def testAddXCheckIfQueueIsEmpty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.assertFalse(self.queue.is_empty())

    def testAddXRemoveXCheckIfQueueIsEmpty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.remove()
        self.assertTrue(self.queue.is_empty())

    def testAddXYRemoveXCheckIfQueueIsNotEmpty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.assertEqual("Clinton", self.queue.remove())

    def testAddXYZCheckQueueIsFull(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.add("Peter")
        self.assertTrue(self.queue.is_full())

    def testAddXYCheckQueueIsNotEmpty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.assertFalse(self.queue.is_empty())

    def testAddMoreElementsThanQueueCapacity(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.add("Peter")
        self.assertRaises(ValueError, self.queue.add, "Ayoade")

    def testRemoveFromEmptyQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.assertRaises(ValueError, self.queue.remove)

    def testRemoveAnElementFromQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.add("Peter")
        self.assertEqual("Clinton", self.queue.remove())

    def testPeekFromEmptyQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.assertRaises(ValueError, self.queue.peek)

    def testPeekTheHeadOfTheQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.add("Peter")
        self.assertEqual("Clinton", self.queue.peek())

    def testPeekAfterRemoveFromQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.remove()
        self.assertEqual("David", self.queue.peek())

    def testRetrieveTheHeadOfTheQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.add("Peter")
        self.assertEqual("Clinton", self.queue.retrieve())

    def testRetrieveFromEmptyQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.assertRaises(ValueError, self.queue.retrieve)

    def testInsertAnElementIntoTheQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.assertTrue(self.queue.offer("Peter"))

    def testInsertElementIntoTheQueueWhenFull(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.add("Peter")
        self.assertFalse(self.queue.offer("Ayoade"))

    def testRemoveAllElementsFromQueue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add("Clinton")
        self.queue.add("David")
        self.queue.add("Peter")
        self.queue.remove()
        self.queue.remove()
        self.queue.remove()
        self.assertTrue(self.queue.is_empty())
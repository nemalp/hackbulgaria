import unittest
from linkedlist import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_get_size(self):
        self.assertEqual(self.ll.size(), 0)

    '''
    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)

    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)
    '''

if __name__ == '__main__':
    unittest.main()

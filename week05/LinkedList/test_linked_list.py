import unittest
from linkedlist import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_get_size(self):
        self.assertEqual(self.ll.size(), 0)

    def test_add_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)
        self.ll.add_element(5)
        self.assertEqual(self.ll.index(0).get_data(), 4)
        self.assertEqual(self.ll.index(1).get_data(), 5)
        self.assertEqual(self.ll.size(), 2)

    def test_add_first(self):
        self.ll.add_first(10)
        self.ll.add_first(12)
        self.assertEqual(self.ll.index(0).get_data(), 12)
        self.assertEqual(self.ll.index(1).get_data(), 10)
        self.assertEqual(self.ll.size(), 2)

    def test_add_at_index(self):
        self.ll.add_at_index(0, 5)
        self.assertEqual(self.ll.to_list(), [5])
        self.ll.add_element(15)
        self.ll.add_element(9)
        self.assertEqual(self.ll.to_list(), [5, 15, 9])
        self.ll.add_at_index(1, 12)
        self.assertEqual(self.ll.to_list(), [5, 12, 15, 9])
        self.ll.add_at_index(3, 12)
        self.assertEqual(self.ll.to_list(), [5, 12, 15, 12, 9])
        self.ll.add_at_index(2, 1)
        self.assertEqual(self.ll.to_list(), [5, 12, 1, 15, 12, 9])

    def test_to_list(self):
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3])

    def test_add_list(self):
        self.ll.add_first(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll.add_list([9, 8, 7, 6])
        self.assertEqual(self.ll.to_list(), [1, 2, 3, 9, 8, 7, 6])

    def test_add_linked_list(self):
        self.linked_list = LinkedList()
        self.linked_list.add_first(2)
        self.linked_list.add_element(3)
        self.assertEqual(self.linked_list.to_list(), [2, 3])

    def test_ll_from_to(self):
        self.ll.add_list([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.ll.ll_from_to(0, 2).to_list(), [1, 2, 3])

    def test_remove(self):
        self.ll.add_list([1, 2, 3])
        self.ll.remove(0)
        self.assertEqual(self.ll.to_list(), [2, 3])
        self.ll.remove(1)
        self.assertEqual(self.ll.to_list(), [2])
        self.ll.remove(0)
        self.assertEqual(self.ll.to_list(), [])

    def test_pop(self):
        self.ll.add_list([1, 2, 3])
        self.assertEqual(self.ll.pop(), 3)

    def test_reduce_to_unique(self):
        self.ll.add_list([1, 2, 3, 2, 1, 3])
        self.assertEqual(self.ll.reduce_to_unique().to_list(), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

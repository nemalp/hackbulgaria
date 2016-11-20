import unittest
from binary_search import binary_search
from turning_point import turning_point


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 3, 5, 8, 12, 33]
        self.arr1 = [1, 2, 3, 4, 5]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.arr1, 0, len(self.arr1), 5), 4)
        self.assertEqual(binary_search(self.arr, 0, len(self.arr), 1), 0)
        self.assertEqual(binary_search(self.arr1, 0, len(self.arr1), 3), 2)
        self.assertEqual(binary_search(self.arr, 0, len(self.arr), 5), 2)


class TestTurningPoint(unittest.TestCase):

    def setUp(self):
        self.tp_arr = [1, 3, 7, 9, 4, 2]
        self.tp_arr1 = [1, 6, 4, 3, 2]
        self.tp_arr2 = [1, 4, 5, 2]

    def test_turning_point(self):
        self.assertEqual(turning_point(self.tp_arr, 0, 6), 4)
        self.assertEqual(turning_point(self.tp_arr1, 0, 5), 2)
        self.assertEqual(turning_point(self.tp_arr2, 0, 4), 3)


if __name__ == '__main__':
    unittest.main()

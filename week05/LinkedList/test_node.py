import unittest
from node import Node


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node(1, 2, 1)

    def test_str_(self):
        self.assertEqual(str(self.node), '1')

    def test_get_prev(self):
        self.assertEqual(self.node.get_prev(), 1)

    def test_get_next(self):
        self.assertEqual(self.node.get_next(), 2)

    def test_set_prev(self):
        self.node.set_prev(10)
        self.assertEqual(self.node.get_prev(), 10)

    def test_set_next(self):
        self.node.set_next(20)
        self.assertEqual(self.node.get_next(), 20)

    def test_get_data(self):
        self.assertEqual(self.node.get_data(), 1)

    def test_set_data(self):
        self.node.set_data(9)
        self.assertEqual(self.node.get_data(), 9)


if __name__ == '__main__':
    unittest.main()

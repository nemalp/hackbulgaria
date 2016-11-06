import unittest
from polynoms import Polynom


class TestPolynom(unittest.TestCase):

    def setUp(self):
        pass

    def test_polynom_str(self):
        self.assertEqual(str(Polynom(4, 'x', 3)), '4*x^3')
        self.assertEqual(str(Polynom(0, 'x', 5)), '0')
        self.assertEqual(str(Polynom(1, 'x', 5)), 'x^5')
        self.assertEqual(str(Polynom(1, 'x', 0)), '1')
        self.assertEqual(str(Polynom(0, 'x', 0)), '0')
        self.assertEqual(str(Polynom(4, 'x', 0)), '4')
        self.assertEqual(str(Polynom(1, 'x', 1)), 'x')
        self.assertEqual(str(Polynom(4, 'x', 1)), '4*x')

    def test_derivat(self):
        self.assertEqual(Polynom(4, 'x', 3).calc_derivat(), Polynom(12, 'x', 2))
        self.assertEqual(Polynom(1, 'x', 1).calc_derivat(), Polynom(1, 'x', 0))
        self.assertEqual(str(Polynom(2, 'x', 0).calc_derivat()), '0')


if __name__ == '__main__':
    unittest.main()

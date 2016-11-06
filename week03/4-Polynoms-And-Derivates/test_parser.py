import unittest
from parser import Parser


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser1 = Parser('x^4+10x^3')
        self.parser2 = Parser('2x^4+10x')
        self.parser3 = Parser('x+x^3')
        self.parser4 = Parser('1')
        self.parser5 = Parser('x')
        self.parser6 = Parser('x+x^3')
        self.parser7 = Parser('3x^2')

    def test_parse_exp(self):
        self.assertEqual(self.parser1.parse_exp(),
                         [['x', '4'], ['10x', '3']])

        self.assertEqual(self.parser2.parse_exp(),
                         [['2x', '4'], ['10x']])

        self.assertEqual(self.parser3.parse_exp(),
                         [['x'], ['x', '3']])

        self.assertEqual(self.parser4.parse_exp(),
                         [['1']])

        self.assertEqual(self.parser5.parse_exp(),
                         [['x']])

        self.assertEqual(self.parser6.parse_exp(),
                         [['x'], ['x', '3']])

        self.assertEqual(self.parser7.parse_exp(),
                         [['3x', '2']])

    def test_get_coef(self):
        self.assertEqual(self.parser1.get_coef('x'), 1)
        self.assertEqual(self.parser1.get_coef('2x'), 2)
        self.assertEqual(self.parser1.get_coef('10x'), 10)

    def test_get_power(self):
        self.assertEqual(self.parser1.get_power(['x']), 1)
        self.assertEqual(self.parser1.get_power(['x', '2']), 2)
        self.assertEqual(self.parser1.get_power(['2x', 2]), 2)
        self.assertEqual(self.parser1.get_power(['20x', 2]), 2)
        self.assertEqual(self.parser1.get_power(['20']), 0)

    def test_build_dict(self):
        self.assertEqual(self.parser1.build_dict(), {3: [10], 4: [1]})
        self.assertEqual(self.parser2.build_dict(), {1: [10], 4: [2]})
        self.assertEqual(self.parser3.build_dict(), {1: [1], 3: [1]})
        self.assertEqual(self.parser4.build_dict(), {0: [1]})
        self.assertEqual(self.parser5.build_dict(), {1: [1]})
        self.assertEqual(self.parser6.build_dict(), {1: [1], 3: [1]})
        self.assertEqual(self.parser7.build_dict(), {2: [3]})
        self.assertEqual(Parser('5').build_dict(), {0: [5]})
        self.assertEqual(Parser('5+3x^2+3').build_dict(), {0: [3], 2: [3]})
        self.assertEqual(Parser('5+3x^2+3+1x^2').build_dict(),
                         {0: [3], 2: [3, 1]})
        self.assertEqual(Parser('3x^2+1').build_dict(), {0: [1], 2: [3]})


if __name__ == '__main__':
    unittest.main()

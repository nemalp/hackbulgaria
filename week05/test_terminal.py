import unittest
from terminal import Terminal
# watch -n 2 python3 filename


class TestTerminal(unittest.TestCase):

    def setUp(self):
        self.t = Terminal(number=1, max_flights=20)

    def test_init_terminal(self):
        self.assertTrue(isinstance(self.t, Terminal))

    def test_get_terminal_flights(self):
        self.assertEqual(self.t.get_terminal_flights(), 20)

if __name__ == '__main__':
    unittest.main()

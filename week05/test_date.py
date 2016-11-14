import unittest
from date import Date


class TestDate(unittest.TestCase):

    def setUp(self):
        self.date = Date(29, 11, 2016, hour='12:20')

    def test_date_init(self):
        self.assertTrue(isinstance(self.date, Date))

    def test_date_get_hour(self):
        self.assertEqual(self.date.get_hours(), 12)

    def test_date_get_minutes(self):
        self.assertEqual(self.date.get_minutes(), 20)

if __name__ == '__main__':
    unittest.main()

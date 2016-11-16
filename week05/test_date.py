import unittest
from date import Date
from flight import Flight
from terminal import Terminal


class TestDate(unittest.TestCase):

    def setUp(self):
        self.date = Date(29, 11, 2016, hour='12:20')
        self.date_ = Date(29, 11, 2016, hour='12:20')
        self.date1 = Date(29, 11, 2015, hour='12:20')
        self.date2 = Date(29, 11, 2016, hour='12:20')
        self.flight = Flight(start_time=Date(19, 10, 2015, hour='11:20'),
                              end_time=Date(29, 11, 2015, hour='15:30'),
                              passengers=100, max_passengers=120,
                              from_dest="Sofia", to_dest="Chicago",
                              terminal=Terminal(1, 20),
                              declined=True)

        self.flight1 = Flight(start_time=Date(19, 10, 2015, hour='11:20'),
                              end_time=Date(29, 11, 2015, hour='15:30'),
                              passengers=100, max_passengers=120,
                              from_dest="Sofia", to_dest="Chicago",
                              terminal=Terminal(1, 20),
                              declined=True)

    def test_date_init(self):
        self.assertTrue(isinstance(self.date, Date))

    def test_date_str(self):
        self.assertEqual(str(self.date), 'day=29, month=11, year=2016, hour=12:20')

    def test_date_eq(self):
        self.assertEqual(self.date, self.date_)

    def test_date_get_hour(self):
        self.assertEqual(self.date.get_hours(), 12)

    def test_date_get_minutes(self):
        self.assertEqual(self.date.get_minutes(), 20)

    def test_date_lt(self):
        self.assertTrue(self.date1 < self.date)

    def test_date_gt(self):
        self.assertTrue(self.date > self.date1)

if __name__ == '__main__':
    unittest.main()

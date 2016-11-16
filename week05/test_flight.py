import unittest
from flight import Flight
from date import Date
from terminal import Terminal


class TestFlight(unittest.TestCase):

    def setUp(self):
        self.flight = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                             end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120,
                             from_dest="Sofia", to_dest="London",
                             terminal=Terminal(2, 30),
                             declined=False)

    def test_init_flight(self):
        self.assertTrue(isinstance(self.flight, Flight))

    def test_flight_empty_seats(self):
        self.assertEqual(self.flight.flight_empty_seats(), 20)

    def test_flight_duration(self):
        self.assertEqual(self.flight.flight_duration(), '3:10')

    def test_is_declined(self):
        self.assertFalse(self.flight.is_declined())

    def test_get_start_time(self):
        self.assertEqual(self.flight.get_start_time(), Date(29, 11, 2016, hour='12:20'))

    def test_get_end_time(self):
        self.assertEqual(self.flight.get_end_time(), Date(29, 11, 2016, hour='15:30'))

    def test_get_from_destination(self):
        self.assertEqual(self.flight.get_from_destination(), 'Sofia')

    def test_get_to_destination(self):
        self.assertEqual(self.flight.get_to_destination(), 'London')

if __name__ == '__main__':
    unittest.main()

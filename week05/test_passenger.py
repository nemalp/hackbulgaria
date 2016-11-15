import unittest
from flight import Flight
from date import Date
from terminal import Terminal
from passenger import Passenger


class TestPassenger(unittest.TestCase):

    def setUp(self):
        self.flight = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                             end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120,
                             from_dest="Sofia", to_dest="London",
                             terminal=Terminal(2, 30),
                             declined=False)

        self.passenger = Passenger(first_name="Rositsa",
                                   last_name="Zlateva",
                                   flight=self.flight, age=22)

    def test_passenger_init(self):
        self.assertTrue(isinstance(self.passenger, Passenger))


if __name__ == '__main__':
    unittest.main()

import unittest
from date import Date
from terminal import Terminal
from reservation import Reservation
from flight import Flight
from passenger import Passenger
from airport import Airport


class TestAirport(unittest.TestCase):

    def setUp(self):
        self.flight = Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                             end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120,
                             from_dest="Sofia", to_dest="London",
                             terminal=Terminal(2, 30),
                             declined=False)

        self.flight1 = Flight(start_time=Date(19, 10, 2015, hour='11:20'),
                              end_time=Date(29, 11, 2015, hour='15:30'),
                              passengers=100, max_passengers=120,
                              from_dest="Sofia", to_dest="Chicago",
                              terminal=Terminal(1, 20),
                              declined=True)

        self.passenger = Passenger(first_name="Rositsa",
                                   last_name="Zlateva",
                                   flight=self.flight, age=22)

        self.date = Date(29, 11, 2016, '12:20')
        self.date1 = Date(19, 10, 2015, '12:20')

        self.reservation = Reservation(self.flight, self.passenger, True)
        self.airport = Airport([self.flight, self.flight1])

    def test_airport_init(self):
        self.assertTrue(isinstance(self.airport, Airport))

    def test_get_flights_for(self):
        self.assertEqual(self.airport.get_flights_for(self.date), 1)

    def test_get_flight_before(self):
        self.assertEqual(self.airport.get_flight_before(self.date1), 1)


if __name__ == '__main__':
    unittest.main()

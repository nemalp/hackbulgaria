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


        self.flight2 = Flight(start_time=Date(19, 10, 2015, hour='11:20'),
                              end_time=Date(29, 11, 2015, hour='15:30'),
                              passengers=100, max_passengers=120,
                              from_dest="London", to_dest="Chicago",
                              terminal=Terminal(2, 20),
                              declined=False)

        self.passenger = Passenger(first_name="Rositsa",
                                   last_name="Zlateva",
                                   flight=self.flight, age=22)

        self.date = Date(29, 11, 2016, '12:20')
        self.date1 = Date(19, 10, 2017, '12:20')
        self.date2 = Date(11, 10, 2015, '11:20')

        self.reservation = Reservation(self.flight, self.passenger, True)
        self.airport = Airport([self.flight, self.flight1, self.flight2])

    def test_airport_init(self):
        self.assertTrue(isinstance(self.airport, Airport))

    def test_airport_flights(self):
        self.assertEqual(self.airport.flights, [self.flight, self.flight2])

    def test_get_flights_for(self):
        self.assertEqual(self.airport.get_flights_for(self.date), 1)

    def test_get_flight_before(self):
        self.assertEqual(self.airport.get_flight_before(self.date),
                         [self.flight, self.flight2])

    def test_get_flight_from(self):
        self.assertEqual(self.airport.get_flight_from(
            self.flight2.get_from_destination()), [self.flight2])

    def test_get_flight_to(self):
        self.assertEqual(self.airport.get_flight_to(
            self.flight2.get_to_destination()), [self.flight2])

    def test_get_terminal_flights(self):
        self.assertEqual(self.airport.get_terminal_flights(2),
                         [self.flight, self.flight2])

    def test_get_terminal_flights_on(self):
        self.assertEqual(self.airport.get_terminal_flights_on(self.date, 2),
                         [self.flight])

    def test_get_terminal_flights_to_dest(self):
        self.assertEqual(self.airport.terminal_flights_to_dest('London', 2),
                         [self.flight])

if __name__ == '__main__':
    unittest.main()

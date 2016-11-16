class Airport:

    def __init__(self, flights):
        self.flights = [flight for flight in flights if not flight.declined]

    def get_flights_for(self, date):
        flights_for = [flight for flight in self.flights
                       if flight.get_start_time() == date]
        return len(flights_for)

    def get_flight_before(self, date):
        flights_before = [flight for flight in self.flights
                          if flight.get_start_time() < date]

        return flights_before

    def get_flight_from(self, destination):
        return [f for f in self.flights
                if f.get_from_destination() == destination]

    def get_flight_to(self, destination):
        return [f for f in self.flights
                if f.get_to_destination() == destination]

    def get_terminal_flights(self, terminal):
        return [f for f in self.flights if f.get_terminal_number() == terminal]

    def get_terminal_flights_on(self, date, terminal):
        return [f for f in self.flights
                if f.get_terminal_number() == terminal and
                f.get_start_time() == date]

    def terminal_flights_to_dest(self, destination, terminal):
        return [f for f in self.flights
                if f.get_terminal_number() == terminal and
                f.get_to_destination() == destination]

    def flights_on_date_lt_hours(self, date, hours):
        pass

    def flights_within_duration(self, start_time, end_time):
        pass

    def passengers_to_dest(self, dest):
        pass

    def passengers_reservations(self, flight):
        pass

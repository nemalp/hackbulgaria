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

    def flights_with_passengers(self, size):
        return [f for f in self.flights if len(f.passengers) > size]

    def passengers_from_terminal(self, terminal):
        return [p for f in self.flights if f.get_terminal_number() == terminal
                for p in f.passengers]

    def flights_on_date_lt_hours(self, date):
        flights = []
        for f in self.flights:
            if f.get_start_time() == date:
                flight_hours = f.get_start_time().get_hours()
                flight_minutes = f.get_start_time().get_minutes()
                date_hours = date.get_hours()
                date_minutes = date.get_minutes()

                if flight_hours < date_hours:
                    flights.append(f)

                if flight_hours == date_hours:
                    if flight_minutes < date_minutes:
                        flights.append(f)

        return flights

    def reservations_to_destination(self, destination):
        return [r for f in self.flights
                if f.get_to_destination() == destination for r in f.reservations]

    def passengers_under_18(self, flight):
        return [p for p in flight.passengers if p.age < 18]

    def passengers_to_dest(self, dest):
        return [p for f in self.flights
            if f.get_to_destination() == dest for p in f.passengers]

    def passengers_reservations(self, flight):
        return [r for r in flight.reservations]

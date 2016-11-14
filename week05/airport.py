class Airport:

    def __init__(self, flight, terminal):
        self.flights = []

    def get_flights_for(self, date):
        pass

    def get_flight_before(self, hour):
        pass

    def get_flight_from(self, date, destination):
        pass

    def get_terminal_flights_on(self, date):
        pass

    def flight_before(self, date, hour):
        pass

    def get_flight_to(self, date, destination):
        pass

    def terminal_flights_to_dest(self, destination):
        pass

    def flights_on_date_lt_hours(self, date, hours):
        pass

    def flights_within_duration(self, start_time, end_time):
        pass

    def passengers_to_dest(self, dest):
        pass

    def passengers_reservations(self, flight):
        pass

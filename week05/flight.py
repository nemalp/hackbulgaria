class Flight:

    def __init__(self, start_time, end_time, passengers, max_passengers,
                 from_dest, to_dest, terminal, declined):
        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined
        self.empty_seats = self.max_passengers - self.passengers

    def flight_empty_seats(self):
        return self.empty_seats

    def is_declined(self):
        return self.declined

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_from_destination(self):
        return self.from_dest

    def get_to_destination(self):
        return self.to_dest

    def get_terminal_number(self):
        return self.terminal.number

    def flight_duration(self):
        start_hours = self.start_time.get_hours()
        start_minutes = self.start_time.get_minutes()
        end_hours = self.end_time.get_hours()
        end_minutes = self.end_time.get_minutes()
        duration = str(abs(start_hours - end_hours)) + ':' + \
            str(abs(start_minutes - end_minutes))

        return duration

class Date:

    def __init__(self, dd, mm, yy, hour):
        self.day = dd
        self.month = mm
        self.year = yy
        self.hour = hour

    def __eq__(self, other):
        if self.day == other.day and self.month == other.month and \
                self.year == other.year:

            return True

        return False

    def get_hours(self):
        return int(self.hour.split(':')[0])

    def get_minutes(self):
        return int(self.hour.split(':')[1])

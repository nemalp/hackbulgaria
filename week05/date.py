class Date:

    def __init__(self, dd, mm, yy, hour):
        self.day = dd
        self.month = mm
        self.year = yy
        self.hour = hour

    def __str__(self):
        return 'day={}, month={}, year={}, hour={}'.format(self.day, self.month, self.year, self.hour)

    def __eq__(self, other):
        if self.day == other.day and self.month == other.month and \
                self.year == other.year:

            return True

        return False

    def __lt__(self, other):
        other_hours = int(other.hour.split(':')[0])
        other_minutes = int(other.hour.split(':')[1])

        return self.day <= other.day or self.month <= other.month or \
                self.year <= other.year or self.get_hours() <= other_hours or \
                self.get_minutes() < other_minutes


                # date = Date(29, 11, 2016, hour='12:20')
                # date1 = Date(29, 11, 2015, hour='12:20')

    def __gt__(self, other):
        # TODO ask trainer for better solution
        return self.__lt__(other)

    def get_hours(self):
        return int(self.hour.split(':')[0])

    def get_minutes(self):
        return int(self.hour.split(':')[1])

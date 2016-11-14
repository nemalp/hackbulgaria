class Date:

    def __init__(self, dd, mm, yy, hour):
        self.day = dd
        self.month = mm
        self.year = yy
        self.hour = hour

    def get_hours(self):
        return int(self.hour.split(':')[0])

    def get_minutes(self):
        return int(self.hour.split(':')[1])

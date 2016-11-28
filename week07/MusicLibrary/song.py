from datetime import datetime, timedelta


class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = self.parse_length(length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title,
                                             self.album, str(self._length))

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        pass

    @staticmethod
    def parse_length(time):
        if len(time.split(':')) == 3:
            t = datetime.strptime(time, '%H:%M:%S')
            return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        else:
            t = datetime.strptime(time, '%M:%S')
            return timedelta(minutes=t.minute, seconds=t.second)

    def length(self, **kwargs):
        for key, value in kwargs.items():
            if key is 'seconds' and value is True:
                pass

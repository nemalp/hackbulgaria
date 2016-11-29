from datetime import datetime, timedelta


class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = length
        self.length_as_obj = self.parse_length(length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title,
                                             self.album, self._length)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.__str__())

    @staticmethod
    def parse_length(time):
        if len(time.split(':')) == 3:
            # try with %-M in order to remove the leading zero
            t = datetime.strptime(time, '%H:%M:%S')
            return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        else:
            t = datetime.strptime(time, '%M:%S')
            return timedelta(minutes=t.minute, seconds=t.second)

    # length(seconds=True) - should return the length in seconds or just the seconds.
    def length(self, **kwargs):
        for key, value in kwargs.items():
            if key is 'seconds' and value is True:
                return self.length_as_obj
            if key is 'hours' and value is True:
                return type(self.length_as_obj)
                # TODO

s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
print(s.length(hours=True))
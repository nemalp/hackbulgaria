from datetime import timedelta


class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title,
                                             self.album, self._length)

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __hash__(self):
        return hash(self.__str__())

    @staticmethod
    def get_seconds(time):
        t = [int(x) for x in time.split(':')]

        if len(t) == 3:
            s = timedelta(hours=t[0], minutes=t[1], seconds=t[2])
            return s.total_seconds()
        else:
            s = timedelta(minutes=t[0], seconds=t[1])
            return s.total_seconds()

    def length(self, seconds=False, minutes=False, hours=False):
        time = self._length.split(':')

        if seconds:
            s = self.get_seconds(self._length)
            return s

        elif minutes:
            if len(time) == 3:
                m = (int(time[0]) * 60) + int(time[1])
            else:
                m = int(time[0])

            return m

        elif hours:
            if len(time) == 3:
                return int(time[0])
            else:
                raise ValueError

        return self._length

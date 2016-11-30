from datetime import timedelta


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__songs = []

    def get_songs(self):
        return self.__songs

    def add_song(self, song):
        self.__songs.append(song)

    def add_songs(self, songs: list):
        # self.__songs + songs doesn't work
        for s in songs:
            self.__songs.append(s)

    def remove_song(self, song):
        self.__songs.remove(song)

    def total_length(self):
        total_len = sum([song.length(seconds=True) for song in self.__songs])
        return str(timedelta(seconds=total_len))

    def artists(self):
        artists = {}
        for song in self.__songs:
            if song.artist not in artists:
                artists[song.artist] = 1
            else:
                artists[song.artist] += 1

        return artists

    def next_song(self):
        pass

    def pprint_playlist():
        # import terminaltables
        pass

    def save(self):
        pass

    def load(self, path):
        pass

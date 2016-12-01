import random
from datetime import timedelta


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.song_idx = 0
        self.__songs = []
        self.__shuffled_songs = self.__songs

    def get_songs(self):
        return self.__songs

    def add_song(self, song):
        self.__songs.append(song)

    def add_songs(self, songs: list):
        self.__songs += songs
        '''
        for s in songs:
            self.__songs.append(s)
        '''

    def remove_song(self, song):
        idx = self.__songs.index(song)
        self.__songs.pop(idx)

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
        if self.repeat:
            song = self.__songs[self.song_idx]

        if self.shuffle:
            if self.__songs != self.__shuffled_songs:
                random.shuffle(self.__shuffled_songs)

            song = self.__shuffled_songs[self.song_idx]

            for s in self.__shuffled_songs:
                print(s.title)

        self.song_idx += 1

        if self.song_idx == len(self.__songs) - 1 and self.shuffle is False:
            self.song_idx = 0
        elif self.song_idx == len(self.__shuffled_songs) - 1 and self.shuffle:
            self.__shuffled_songs = random.shuffle(self.__songs)
            self.song_idx = 0

        return song

    def pprint_playlist():
        # import terminaltables
        pass

    def save(self):
        pass

    def load(self, path):
        pass

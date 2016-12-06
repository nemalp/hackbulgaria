import json
import random
from datetime import timedelta
from terminaltables import AsciiTable
from song import Song


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.song_idx = 0
        self.__songs = []
        self.__played_songs = []

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
            if len(self.__songs) == self.song_idx:
                self.song_idx = 0
            song = self.__songs[self.song_idx]

        if self.shuffle:
            song = random.choice(self.__songs)

            while song in self.__played_songs:
                song = random.choice(self.__songs)

            self.__played_songs.append(song)

            if len(self.__songs) == len(self.__played_songs):
                self.__played_songs = []

        self.song_idx += 1

        return song

    def pprint_playlist(self):
        data = [[song.artist, song.title, song._length]
                for song in self.__songs]
        data.insert(0, ['Artist', 'Song', 'Length'])
        table = AsciiTable(data)
        table.title = 'Playlist'
        print(table.table)

    def save(self):
        json_data = {}
        json_data['name'] = self.name
        json_data['songs'] = []

        playlist = [[song.title, song.artist, song.album, song._length]
                    for song in self.__songs]

        for song in playlist:
            json_data['songs'].append({'title': song[0], 'artist': song[1],
                                      'album': song[2], 'length': song[3]})

        with open('' + self.name + '.json', 'w') as output:
            json.dump(json_data, output, indent=True)

    @staticmethod
    def load(filename):
        songs = []

        with open(filename, 'r') as f:
            content = f.read()
            data = json.loads(content)
            playlist = Playlist(data['name'], repeat=True)

            for song in data['songs']:
                songs.append(Song(song['title'], song['artist'],
                                  song['album'], song['length']))

            playlist.add_songs(songs)

        return playlist

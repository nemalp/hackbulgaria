
import unittest
from song import Song
from playlist import Playlist


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.pl = Playlist(name="Rock")
        self.pl1 = Playlist(name="Rock", repeat=True, shuffle=True)

        self.s = Song(title="Odin", artist="Manowar", album="The Sons of Odin",
                      length="3:10")

        self.s1 = Song(title="Die for Metal", artist="Manowar",
                       album="Unknown", length="5:10")

        self.s2 = Song(title="The crown and the ring", artist="Manowar",
                       album="New", length="7:10")

    def test_init(self):
        self.assertTrue(isinstance(self.pl, Playlist))
        self.assertTrue(isinstance(self.pl1, Playlist))

    def test_get_songs(self):
        self.assertEqual(self.pl.get_songs(), [])

    def test_add_song(self):
        self.pl.add_song(self.s)
        self.pl.add_song(self.s1)
        self.assertEqual([self.s, self.s1], self.pl.get_songs())

    def test_add_songs(self):
        self.pl.add_song(self.s2)
        self.pl.add_songs([self.s, self.s1])
        self.assertEqual([self.s2, self.s, self.s1],
                         self.pl.get_songs())

    def test_remove_song(self):
        self.pl.add_songs([self.s, self.s2])
        self.pl.remove_song(self.s2)
        self.assertEqual([self.s], self.pl.get_songs())

    def test_total_length(self):
        self.pl.add_songs([self.s, self.s1, self.s2])
        self.assertEqual(self.pl.total_length(), '0:15:30')

    def test_artists(self):
        pass

    def test_next_song(self):
        pass


if __name__ == '__main__':
    unittest.main()

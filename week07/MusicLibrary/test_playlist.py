
import unittest
from song import Song
from playlist import Playlist


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.pl = Playlist(name="Rock")
        self.pl1 = Playlist(name="Rock", repeat=False, shuffle=True)

        self.s = Song(title="Odin", artist="Manowar", album="The Sons of Odin",
                      length="3:10")

        self.s1 = Song(title="Odin", artist="Manowar",
                       album="Unknown", length="5:10")

        self.s2 = Song(title="The crown and the ring", artist="Manowar",
                       album="New", length="7:10")

        self.s3 = Song(title="Cowboys from hell", artist="Pantera",
                       album="Cowboys from hell", length="5:10")

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
        self.pl.add_songs([self.s, self.s1, self.s2, self.s3])
        self.assertEqual({'Manowar': 3, 'Pantera': 1}, self.pl.artists())

    def test_next_song(self):
        self.pl1.add_songs([self.s, self.s1])
        self.pl1.next_song()
        self.assertEqual(self.pl1.next_song().title, self.s.title)
        # self.assertEqual(self.pl1.next_song(), self.s1)
        # self.assertEqual(self.pl1.next_song(), self.s2)
        # self.assertEqual(self.pl1.next_song(), self.s3)
        # self.assertEqual(self.pl1.next_song(), self.s)


if __name__ == '__main__':
    unittest.main()

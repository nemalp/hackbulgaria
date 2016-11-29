import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.s = Song(title="Odin", artist="Manowar", album="The Sons of Odin",
                      length="3:44")

        self.s1 = Song(title="Odin", artist="Manowar",
                       album="The Sons of Odin", length="3:44")

        self.s2 = Song(title="Die for Metal", artist="Manowar",
                       album="New", length="1:3:44")

    def test_init(self):
        self.assertTrue(isinstance(self.s, Song))

    def test_str(self):
        self.assertEqual(str(self.s),
                         "Manowar - Odin from The Sons of Odin - 3:44")

    def test_eq(self):
        self.assertEqual(self.s, self.s1)

    def test_get_seconds(self):
        self.assertEqual(self.s.get_seconds('2:20'), 140)
        self.assertEqual(self.s.get_seconds('1:2:20'), 3740)

    def test_length(self):
        self.assertEqual(self.s.length(seconds=True), 224)
        self.assertEqual(self.s2.length(seconds=True), 3824)
        self.assertEqual(self.s.length(minutes=True), 3)
        self.assertEqual(self.s2.length(hours=True), 1)
        with self.assertRaises(ValueError):
            self.s.length(hours=True)


if __name__ == '__main__':
    unittest.main()

import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.s = Song(title="Odin", artist="Manowar", album="The Sons of Odin",
                      length="3:44")

        self.s1 = Song(title="Odin", artist="Manowar",
                       album="The Sons of Odin", length="3:44")

    def test_init(self):
        self.assertTrue(isinstance(self.s, Song))

    def test_str(self):
        self.assertEqual(str(self.s),
                         "Manowar - Odin from The Sons of Odin - 3:44")

    def test_eq(self):
        self.assertEqual(self.s, self.s1)

    def test_length(self):
        pass
       #  self.assertEqual(self.s.length(seconds=True),
       #                  self.s.parse_length('3:44'))


if __name__ == '__main__':
    unittest.main()

import unittest
from panda import Panda


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda(name="Ivo", email="ivo@pandamail.com", gender="male")
        self.john = Panda(name="John", email="john@pandamail.com",
                          gender="male")

    def test__init__(self):
        self.assertTrue(isinstance(self.ivo, Panda))

    def test__str__(self):
        self.assertEqual(str(self.ivo),
                         'name: Ivo, email: ivo@pandamail.com, gender: male')

    def test__eq__(self):
        self.ivo2 = Panda(name="Ivo", email="ivo@pandamail.com", gender="male")
        self.assertEqual(self.ivo, self.ivo2)

    def test__hash__(self):
        self.ivo2 = Panda(name="Ivo", email="sdf@pandamail.com",
                          gender="male")
        dict_ = {hash(self.ivo): self.ivo, hash(self.ivo2): self.ivo2}
        self.assertEqual(len(dict_), 2)

        dict_ = {hash(self.ivo): self.ivo, hash(self.ivo): self.ivo}
        self.assertEqual(len(dict_), 1)

    def test_name(self):
        self.assertEqual(self.john.name(), 'John')

    def test_email(self):
        self.assertEqual(self.john.email(), 'john@pandamail.com')

    def test_gender(self):
        self.assertEqual(self.john.gender(), 'male')

    def test_isMale(self):
        self.assertTrue(self.john.isMale())

    def test_isFemale(self):
        self.raya = Panda(name="Raya", email="raya@pandamail.com",
                          gender="female")
        self.assertTrue(self.raya.isFemail())


if __name__ == '__main__':
    unittest.main()

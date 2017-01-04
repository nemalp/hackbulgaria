import unittest
from panda import Panda
from socialnetwork import PandaSocialNetwork


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.panda1 = Panda(name='panda1', email='eee@abv.bg', gender='male')
        self.panda2 = Panda(name='panda2', email='ggg@abv.bg', gender='female')
        self.panda3 = Panda(name='panda3', email='ppp@abv.bg', gender='female')

    def test_get_pandas_return_1_panda_if_1_panda_is_added(self):
        panda = Panda(name='Jane', email='test@gmail.com',
                      gender='female')

        self.network.add_panda(panda)
        self.assertEqual([panda], self.network.get_pandas())

    def test_make_friends(self):
        self.network.make_friends(self.panda1, self.panda2)

        self.assertEqual(2, len(self.network.get_pandas()))
        self.assertTrue(self.network.are_friends(self.panda1, self.panda2))
        self.assertTrue(self.network.are_friends(self.panda2, self.panda1))

    def test_connection_level_for_network_with_4_connected_pandas(self):
        panda1 = Panda('one', 'one@abv.bg', 'male')
        panda2 = Panda('two', 'two@abv.bg', 'male')
        panda3 = Panda('three', 'three@abv.bg', 'male')
        panda4 = Panda('four', 'four@abv.bg', 'female')

        self.network.make_friends(panda1, panda2)
        self.network.make_friends(panda2, panda3)
        self.network.make_friends(panda3, panda4)

        self.assertEqual(self.network.connection_level(panda1, panda3),
                         (2, [panda1, panda2, panda3]))

    def test_if_two_pandas_are_friends(self):
        self.network.make_friends(self.panda1, self.panda2)
        self.assertTrue(self.network.are_friends(self.panda1, self.panda2))

    def test_friends_of_panda(self):
        self.network.make_friends(self.panda1, self.panda2)
        self.network.make_friends(self.panda1, self.panda3)
        self.assertEqual(self.network.friends_of_panda(self.panda1),
                         set([self.panda2, self.panda3]))

    def test_if_two_pandas_are_connected_somehow(self):
        self.network.make_friends(self.panda1, self.panda2)
        self.assertEqual(self.network.connection_level(self.panda1,self.panda2),
                         (1, [self.panda1, self.panda2]))

if __name__ == '__main__':
    unittest.main()

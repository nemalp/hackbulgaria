import sys
import unittest
import os
sys.path.append("..")
import sql_manager
from queries.queries import COUNT_USER, GET_CLIENT_PASS


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123', 'test@test.com')
        sql_manager.cursor.execute(GET_CLIENT_PASS, ['Tester'])
        self.hashed_pass = sql_manager.cursor.fetchone()[0]

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE CLIENT')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        sql_manager.register('Dinko', 'StrongPass1!', 'dinko@borderr.com')
        sql_manager.cursor.execute(GET_CLIENT_PASS, ['Dinko'])
        hashed_pass = sql_manager.cursor.fetchone()[0]

        sql_manager.cursor.execute(COUNT_USER, ['Dinko', hashed_pass])
        users_count = sql_manager.cursor.fetchone()
        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_sql_injection(self):
        logged_user = sql_manager.login("' OR 1 = 1 --", '1234')
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()

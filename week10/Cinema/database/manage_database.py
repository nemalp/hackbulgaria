import sys
sys.path.append('..')
import sqlite3
from queries.create_db_queries import *
from queries.manage_db_queries import *
from settings.general_settings import *
from user_interface.validators import *
from colorama import Fore

DB = sqlite3.connect('../database/' + DB_NAME)
DB.row_factory = sqlite3.Row
c = DB.cursor()


def login(username, password):
    if validate_user(username, password):
        c.execute(LOGIN_USER, [username, password])
        DB.commit()

        print(Fore.GREEN + 'Hello, {}'.format(username + Fore.RESET))
        return True
    else:
        print(Fore.RED + 'Incorrect username or password' + Fore.RESET)


def is_logged(username, password):
    c.execute(SELECT_USER, [username, password])
    user = c.fetchone()

    if user['is_logged']:
        return True

    return False




if __name__ == '__main__':
    main()

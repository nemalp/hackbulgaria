import sqlite3
import argparse
from colorama import Fore, Back, Style
import sys
sys.path.append('..')
from settings.general_settings import *
from queries.manage_db_queries import *

DB = sqlite3.connect('../database/' + DB_NAME)
DB.row_factory = sqlite3.Row
c = DB.cursor()


def validate_user(username, password):
    c.execute(SELECT_USER, [username, password])
    user = c.fetchone()

    if user:
        return True

    return False


if __name__ == '__main__':
    main()

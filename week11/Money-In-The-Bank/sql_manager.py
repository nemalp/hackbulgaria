import sqlite3
from client import Client
from settings.general_settings import (DB_NAME)
from time import time
# from helpers.hash_password import hash_password
from queries.queries import (CREATE_CLIENT_TABLE, CREATE_BANNED_CLIENT_TABLE,
                             UPDATE_CLIENT_MESSAGE, UPDATE_CLIENT_PASSWORD,
                             REGISTER_CLIENT, SELECT_CLIENT, BAN_CLIENT,
                             CHECK_FOR_BAN, REMOVE_BAN)


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def create_clients_table():
    cursor.execute(CREATE_CLIENT_TABLE)
    conn.commit()


def create_banned_clients_table():
    cursor.execute(CREATE_BANNED_CLIENT_TABLE)
    conn.commit()


def change_message(new_message, logged_user):
    cursor.execute(UPDATE_CLIENT_MESSAGE, [new_message, logged_user.get_id()])
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(UPDATE_CLIENT_PASSWORD, [new_pass, logged_user.get_id()])
    conn.commit()


def register(username, password):
    # hashed_password = hash_password(password)
    cursor.execute(REGISTER_CLIENT, [username, password])
    conn.commit()


def login(username, password):
    cursor.execute(SELECT_CLIENT, [username, password])
    user = cursor.fetchone()

    if user:
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False


def ban_client(username):
    ban_time = time() + 300
    cursor.execute(BAN_CLIENT, [username, ban_time])
    conn.commit()


def remove_ban(username):
    cursor.execute(REMOVE_BAN, [username])
    conn.commit()


def is_banned(username):
    cursor.execute(CHECK_FOR_BAN, [username])
    user = cursor.fetchone()

    return user

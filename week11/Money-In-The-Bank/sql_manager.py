import sqlite3
import hashlib
import smtplib
from client import Client
from settings.general_settings import (DB_NAME)
from time import time
from helpers.hash_password import hash_password, check_password
from queries.queries import (CREATE_CLIENT_TABLE, CREATE_BANNED_CLIENT_TABLE,
                             UPDATE_CLIENT_MESSAGE, UPDATE_CLIENT_PASSWORD,
                             REGISTER_CLIENT, SELECT_CLIENT, BAN_CLIENT,
                             CHECK_FOR_BAN, REMOVE_BAN, GET_CLIENT_PASS)


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
    cursor.execute(UPDATE_CLIENT_PASSWORD, [hash_password(new_pass),
                                            logged_user.get_id()])
    conn.commit()


def register(username, password, email):
    hashed_password = hash_password(password)
    cursor.execute(REGISTER_CLIENT, [username, hashed_password, email])
    conn.commit()


def login(username, password):
    cursor.execute(GET_CLIENT_PASS, [username])
    hashed_pass = cursor.fetchone()

    if hashed_pass:
        if check_password(hashed_pass[0], password):
            cursor.execute(SELECT_CLIENT, [username])
            user = cursor.fetchone()

            if user:
                return Client(user[0], user[1], user[2], user[3], user[4])

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


def send_reset_password_email(from_, to, password):
    try:
        content = 'Test email'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(from_, password)
        server.sendmail(from_, to, content)
        server.close()
    except:
        print('This functionality is still in beta.' +
              'It is possible to experience some outages')

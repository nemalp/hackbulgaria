import sqlite3
from queries.create_db_queries import *
from queries.manage_db_queries import *
from settings.sql_creation_settings import *

DB = sqlite3.connect(DB_NAME)
c = DB.cursor()


def drop_db():
    DB.executescript(DROP_DB)


def init_db():
    DB.execute(CREATE_USER_TABLE)
    DB.execute(CREATE_PROJECTION_TABLE)
    DB.execute(CREATE_MOVIE_TABLE)
    DB.execute(CREATE_RESERVATION_TABLE)


def populate_user_table():
    users = [('Rositsa Zlateva', '1234'),
             ('Slavyana Monkova', '2234'),
             ('Radoslav Georgiev', '8234'),
             ('Krasimira Badova', '1934'),
             ('Kiril Hristov', '1204'),
             ('Vladimir Delchev', '1237')]

    c.executemany(INSERT_INTO_USER, users)
    DB.commit()


def populate_projections_table():
    projections = [('1', '3D', '2014-04-01', '19:10'),
                   ('1', '2D', '2014-04-01', '19:00'),
                   ('1', '4DX', '2014-04-02', '21:00'),
                   ('3', '2D', '2014-04-05', '20:20'),
                   ('2', '3D', '2014-04-02', '22:00'),
                   ('2', '2D', '2014-04-02', '19:30')]

    c.executemany(INSERT_INTO_PROJECTION, projections)
    DB.commit()


def populate_movie_table():
    movies = [('The Hunger Games: Catching Fire', 7.9),
              ('Wreck-It Ralph', 7.8),
              ('Her', 8.3)]

    c.executemany(INSERT_INTO_MOVIE, movies)
    DB.commit()


def populate_reservation_table():
    reservations = [(3, 1, 2, 1),
                    (3, 1, 3, 5),
                    (3, 1, 7, 8),
                    (2, 3, 1, 1),
                    (2, 3, 1, 2),
                    (5, 5, 2, 1),
                    (6, 5, 2, 4)]

    c.executemany(INSERT_INTO_RESERVATION, reservations)
    DB.commit()


def main():
    drop_db()
    init_db()
    populate_user_table()
    populate_projections_table()
    populate_movie_table()
    populate_reservation_table()
    DB.close()

if __name__ == '__main__':
    main()

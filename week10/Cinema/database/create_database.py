import sqlite3
from queries.create_db_queries import *
from queries.manage_db_queries import *
from settings.sql_creation_settings import *

DB = sqlite3.connect(DB_NAME)
c = DB.cursor()

c.executescript(DROP_DB)
DB.commit()


DB.execute(CREATE_USER_TABLE)
DB.commit()

users = [('Rositsa Zlateva', '1234'),
         ('Slavyana Monkova', '2234'),
         ('Radoslav Georgiev', '8234'),
         ('Krasimira Badova', '1934'),
         ('Kiril Hristov', '1204'),
         ('Vladimir Delchev', '1237')]

c.executemany(INSERT_INTO_USER, users)
DB.commit()

DB.execute(CREATE_PROJECTION_TABLE)
DB.commit()

projections = [('1', '3D', '2014-04-01', '19:10'),
               ('1', '2D', '2014-04-01', '19:00'),
               ('1', '4DX', '2014-04-02', '21:00'),
               ('3', '2D', '2014-04-05', '20:20'),
               ('2', '3D', '2014-04-02', '22:00'),
               ('2', '2D', '2014-04-02', '19:30')]

c.executemany(INSERT_INTO_PROJECTION, projections)
DB.commit()

DB.execute(CREATE_MOVIE_TABLE)
DB.commit()

movies = [('The Hunger Games: Catching Fire', 7.9),
          ('Wreck-It Ralph', 7.8),
          ('Her', 8.3)]

c.executemany(INSERT_INTO_MOVIE, movies)
DB.commit()

DB.close()

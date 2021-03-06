DROP_DB = '''
    DROP TABLE IF EXISTS MOVIE;
    DROP TABLE IF EXISTS PROJECTION;
    DROP TABLE IF EXISTS USER;
    DROP TABLE IF EXISTS RESERVATION;
    '''

CREATE_MOVIE_TABLE = '''
    CREATE TABLE IF NOT EXISTS MOVIE (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        RATING INTEGER
    )'''

CREATE_PROJECTION_TABLE = '''
    CREATE TABLE IF NOT EXISTS PROJECTION (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MOVIE_ID INTEGER,
        TYPE TEXT NOT NULL,
        DATE TEXT NOT NULL,
        TIME TEXT NOT NULL,
        FOREIGN KEY(MOVIE_ID) REFERENCES MOVIE(ID)
    )'''

CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS USER (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        IS_LOGGED INTEGER DEFAULT 0
    )'''

CREATE_RESERVATION_TABLE = '''
    CREATE TABLE IF NOT EXISTS RESERVATION (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_ID INTEGER,
        PROJECTION_ID INTEGER,
        ROW INTEGER,
        COL INTEGER,
        FOREIGN KEY(USER_ID) REFERENCES USER(ID),
        FOREIGN KEY(PROJECTION_ID) REFERENCES PROJECTION(ID)
    )'''

CREATE_CLIENT_TABLE = '''
    CREATE TABLE IF NOT EXISTS
    CLIENT (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME TEXT,
                PASSWORD TEXT,
                BALANCE REAL DEFAULT 0,
                MESSAGE TEXT,
                EMAIL TEXT)
'''

UPDATE_CLIENT_MESSAGE = '''
    UPDATE CLIENT
    SET MESSAGE = ? WHERE id = ?
'''

UPDATE_CLIENT_PASSWORD = '''
    UPDATE CLIENT
    SET PASSWORD = ? WHERE id = ?
'''

REGISTER_CLIENT = '''
    INSERT INTO CLIENT (USERNAME, PASSWORD) VALUES (?, ?)
'''

SELECT_CLIENT = '''
    SELECT ID, USERNAME, BALANCE, MESSAGE
    FROM CLIENT WHERE USERNAME = ? AND PASSWORD = ? LIMIT 1
'''

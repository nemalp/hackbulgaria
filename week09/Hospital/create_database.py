import sqlite3
from queries import *

DB_NAME = "py_hospital.db"
db = sqlite3.connect(DB_NAME)
c = db.cursor()

c.executescript(DROP_DB)
db.commit()

db.execute(CREATE_PATIENTS_TABLE)
db.commit()

patients = [('Rositsa', 'Zlateva', 22, 'F', 1),
            ('Roza', 'Rozova', 4, 'F', 1),
            ('Kamen', 'Kotsev', 22, 'M', 2),
            ('Monika', 'Valerieva', 30, 'F', 2),
            ('Kristina', 'Valchanova', 30, 'F', 2),
            ('Ivaylo', 'Bachvarov', 23, 'M', 3),
            ('Pandio', 'Pandev', 4, 'M', 3)]

c.executemany(INSERT_INTO_PATIENTS, patients)
db.commit()

db.execute(CREATE_DOCTORS_TABLE)
db.commit()


doctors = [('Pavlina', 'Zdravkova'),
           ('Valentina', 'Yordanova'),
           ('Albena', 'Bachvarova')]

db.executemany(INSERT_INTO_DOCTORS, doctors)
db.commit()

db.execute(CREATE_HOSPITAL_STAY)
db.commit()

hospital_data = [(3, '2016-10-10', '2016-10-11', 'crazy', 1),
                 (6, '2016-10-12', '2016-10-15', 'headache', 2),
                 (2, '2016-09-30', '2016-10-01', 'crazy', 3),
                 (5, '2016-10-17', '2016-10-20', 'pregnancy', 4),
                 (3, '2016-10-12', '2016-10-12', 'кidney сtones', 5),
                 (7, '2016-10-09', '2016-10-12', 'headache', 6),
                 (1, '2016-10-09', '2016-10-11', 'hernia', 7),
                 (1, '2016-10-23', '2016-10-25', 'toothache', 1)]

c.executemany(INSERT_INTO_HOSPITAL_STAY, hospital_data)
db.commit()
db.close()

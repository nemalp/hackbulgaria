import sqlite3

DB_NAME = "py_hospital.db"
db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

drop_db = """DROP TABLE IF EXISTS PATIENTS;
             DROP TABLE IF EXISTS HOSPITAL_STAY;
             DROP TABLE IF EXISTS DOCTORS;"""

c.executescript(drop_db)
db.commit()

create_patients_table = """
                        CREATE TABLE IF NOT EXISTS PATIENTS (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            FIRSTNAME TEXT NOT NULL,
                            LASTNAME TEXT NOT NULL,
                            AGE INTEGER NOT NULL,
                            GENDER VARCHAR(6),
                            DOCTOR INT,
                            FOREIGN KEY(DOCTOR) REFERENCES DOCTOR(ID)
                        )
                        """

db.execute(create_patients_table)
db.commit()

insert_patients = """
    INSERT INTO PATIENTS (FIRSTNAME, LASTNAME, AGE, GENDER, DOCTOR)
    VALUES(?, ?, ?, ?, ?)
    """

patients = [('Rositsa', 'Zlateva', 22, 'F', 1),
            ('Roza', 'Rozova', 4, 'F', 1),
            ('Kamen', 'Kotsev', 22, 'M', 2),
            ('Monika', 'Valerieva', 30, 'F', 2),
            ('Kristina', 'Valchanova', 30, 'F', 2),
            ('Ivaylo', 'Bachvarov', 23, 'M', 3),
            ('Pandio', 'Pandev', 4, 'M', 3)]

c.executemany(insert_patients, patients)
db.commit()

create_doctors_table = """
                       CREATE TABLE IF NOT EXISTS DOCTORS (
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           FIRSTNAME VARCHAR(255) NOT NULL,
                           LASTNAME VARCHAR(255) NOT NULL
                       )
                       """

db.execute(create_doctors_table)
db.commit()

insert_doctors = "INSERT INTO DOCTORS (FIRSTNAME, LASTNAME) VALUES (?, ?)"

doctors = [('Pavlina', 'Zdravkova'),
           ('Valentina', 'Yordanova'),
           ('Albena', 'Bachvarova')]

db.executemany(insert_doctors, doctors)
db.commit()

create_hospital_stay_table = """
                             CREATE TABLE IF NOT EXISTS HOSPITAL_STAY (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                ROOM INT NOT NULL,
                                STARTDATE DATE NOT NULL,
                                ENDDATE DATE int,
                                INJURY VARCHAR(255) NOT NULL,
                                PATIENT INT,
                                FOREIGN KEY(PATIENT) REFERENCES PATIENTS(ID)
                            )
                            """

db.execute(create_hospital_stay_table)
db.commit()

insert_hospital_stay_data = """
    INSERT INTO HOSPITAL_STAY (ROOM, STARTDATE, ENDDATE, INJURY, PATIENT)
    VALUES (?, ?, ?, ?, ?);
    """

hospital_data = [(3, '2016-10-10', '2016-10-11', 'crazy', 1),
                 (6, '2016-10-12', '2016-10-15', 'headache', 2),
                 (2, '2016-09-30', '2016-10-01', 'crazy', 3),
                 (5, '2016-10-17', '2016-10-20', 'pregnancy', 4),
                 (3, '2016-10-12', '2016-10-12', 'кidney сtones', 5),
                 (7, '2016-10-09', '2016-10-12', 'headache', 6),
                 (1, '2016-10-09', '2016-10-11', 'hernia', 7),
                 (1, '2016-10-23', '2016-10-25', 'toothache', 1)]

c.executemany(insert_hospital_stay_data, hospital_data)
db.commit()

list_doctors = """SELECT * FROM DOCTORS """
result = c.execute(list_doctors)
for row in result:
    print(row['firstname'])

db.commit()
db.close()

import sqlite3
# from terminaltables import AsciiTable

class Hospital:

    def __init__(self, db: str):
        self.db = db
        self.db = sqlite3.connect(db)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()

    def get_patient(self, name):
        patient = self.c.execute("SELECT patients.id FROM PATIENTS WHERE patients.firstname = ?", [name])
        self.db.commit()
        return patient

    def list_patients(self):
        all_patients = self.c.execute("SELECT id, firstname, lastname, age FROM PATIENTS")
        data = [['id', 'firstname', 'lastname', 'age']]

        for p in all_patients:
            data.append([p['id'], p['firstname'], p['lastname'], p['age']])

        # patients_table = AsciiTable(data)
        # patients_table.title = 'All Patients'

    def list_doctors(self):
        all_doctors = self.c.execute("SELECT id, firstname, lastname FROM DOCTORS")
        data = [['id', 'firstname', 'lastname']]

        for d in all_doctors:
            data.append([d['id'], d['firstname'], d['lastname']])

        # doctors_table = AsciiTable(data)
        # doctors_table.title = 'All Doctors'
        print(data)

    def add_new_patient(self):
        fname = input('first name: ')
        lname = input('last name: ')
        age = input('age: ')

        insert_patient = "INSERT INTO PATIENTS (FIRSTNAME, LASTNAME, AGE) VALUES(?, ?, ?)"

        try:
            self.c.execute(insert_patient, [fname, lname, age])
            self.db.commit()
            print('{} {} has been added successfully.'.format(fname, lname))
        except Exception:
            print('Oops! Something went wrong')

    def add_new_doctor(self):
        fname = input('first name: ')
        lname = input('last name: ')

        insert_doctor = "INSERT INTO DOCTORS (FIRSTNAME, LASTNAME) VALUES(?, ?)"

        try:
            self.c.execute(insert_doctor, [fname, lname])
            self.db.commit()
            print('Doc. {} {} has been added successfully.'.format(fname, lname))
        except Exception:
            print('Oops! Something went wrong')

    def add_hospital_stay_of_a_patient(self):
        insert_hospital_stay = """INSERT INTO HOSPITAL_STAY (ROOM, STARTDATE, ENDDATE, INJURY, PATIENT)
                                    VALUES (?, ?, ?, ?, ?)"""

        room = input('room: ')
        start_date = input('start date: ')
        end_date = input('end date: ')
        injury = input('injury: ')
        patient_name = input('patient name: ')

        try:
            patient_id = self.c.execute(self.get_patient(patient_name), [patient_name])
            patient_id = [id['id'] for id in patient_id][0]
            self.c.execute(insert_hospital_stay, [room, start_date, end_date, injury, patient_id])
            self.db.commit()
        except Exception:
            print('Oops! Something went wrong')

    def update_patient(self):
        update_patient_info = """"""


def main():
    h = Hospital('py_hospital.db')
    h.add_hospital_stay_of_a_patient()

if __name__ == '__main__':
    main()

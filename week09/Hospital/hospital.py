import sqlite3
from terminaltables import AsciiTable
from queries import *
from settings import *


class Hospital:

    def __init__(self, db: str):
        self.db = db
        self.db = sqlite3.connect(db)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()

    def get_patient(self, name):
        patient = self.c.execute(SELECT_PATIENT, [name])
        self.db.commit()
        return patient

    def list_patients(self):
        all_patients = self.c.execute(SELECT_ALL_PATIENTS)
        data = [['id', 'firstname', 'lastname', 'age']]

        for p in all_patients:
            data.append([p['id'], p['firstname'], p['lastname'], p['age']])

        patients_table = AsciiTable(data)
        patients_table.title = 'All Patients'

        print(patients_table.table)

    def list_doctors(self):
        all_doctors = self.c.execute(SELECT_ALL_DOCTORS)
        data = [['id', 'firstname', 'lastname']]

        for d in all_doctors:
            data.append([d['id'], d['firstname'], d['lastname']])

        doctors_table = AsciiTable(data)
        doctors_table.title = 'All Doctors'
        print(doctors_table.table)

    def list_all_patients_of_a_doctor(self):
        doctor_name = input('Doctor name> :')

        try:
            doctor = self.c.execute(SELECT_DOCTOR, [doctor_name])
            doctor_id = [d['id'] for d in doctor][0]

            all_patients_of_a_doc = self.c.execute(
                SELECT_ALL_PATIENTS_OF_A_DOCTOR,
                [doctor_id])

            data = [['id', 'firstname', 'lastname', 'age']]
            for p in all_patients_of_a_doc:
                data.append([p['id'], p['firstname'], p['lastname'], p['age']])

            patients_table = AsciiTable(data)
            patients_table.title = 'All patients for Dr.{}'.format(doctor_name)
            print(patients_table.table)
        except Exception:
            print('Oops! Something went wrong')

    def list_patients_by_injury(self):
        injury = input('Injury> :')

        patients_by_injury = self.c.execute(SELECT_PATIENTS_BY_INJURY, [injury])
        data = [['patients', 'injury']]
        for p in patients_by_injury:
            data.append([p['p'], injury])

        table = AsciiTable(data)
        table.title = 'Patients grouped by injury'
        print(table.table)

    def list_doctors_by_injury(self):
        doctors_by_injury = self.c.execute(SELECT_DOCTORS_BY_INJURY)
        data = [['injury', 'doctor']]

        for injury, doctor in doctors_by_injury:
            data.append([injury, doctor])

        table = AsciiTable(data)
        table.title = 'List of doctors by injury'
        print(table.table)

    def list_patients_from_to(self):
        print('Enter date in the following format> : yyyy-mm-dd')
        from_date = input('from date> :')
        to_date = input('to date> :')
        patients = self.c.execute(SELECT_PATIENTS_FROM_TO, [from_date, to_date])
        data = [['id', 'firstname', 'lastname', 'age']]

        for p in patients:
            data.append([p['id'], p['firstname'], p['lastname'], p['age']])

        patients_table = AsciiTable(data)
        patients_table.title = 'from {} to {}'.format(from_date, to_date)
        print(patients_table.table)

    def add_new_patient(self):
        fname = input('first name: ')
        lname = input('last name: ')
        age = input('age: ')

        try:
            self.c.execute(INSERT_A_PATIENT, [fname, lname, age])
            self.db.commit()
            print('{} {} has been added successfully.'.format(fname, lname))
        except Exception:
            print('Oops! Something went wrong')

    def add_new_doctor(self):
        fname = input('first name: ')
        lname = input('last name: ')

        try:
            self.c.execute(INSERT_A_DOCTOR, [fname, lname])
            self.db.commit()
            print('Dr. {} {} has been added successfully'.format(fname, lname))
        except Exception:
            print('Oops! Something went wrong')

    def add_hospital_stay_of_a_patient(self):
        room = input('room: ')
        start_date = input('start date: ')
        end_date = input('end date: ')
        injury = input('injury: ')
        patient_name = input('patient name: ')

        try:
            patient = self.get_patient(patient_name)
            patient_id = [p['id'] for p in patient][0]
            self.c.execute(INSERT_INTO_HOSPITAL_STAY,
                           [room, start_date, end_date, injury, patient_id])
            self.db.commit()
            print("{} has been added into the hospital".format(patient_name))
        except Exception:
            print('Oops! Something went wrong')

    def update_patient(self):
        input_ = True
        patient_name = input('name> :')
        # TODO check if patient name is valid
        # Throw an error if it is not

        print('When you are ready type "exit"')
        print('Which column you\'d like to update?')
        print('Available columns => firstname, lastname, gender, age')

        while input_:
            column = input('column> :').upper()

            if column == 'EXIT':
                input_ = False
                break

            while column not in PATIENT_COLUMNS and column is not 'EXIT':
                print('No such column')
                column = input('column> :').upper()

            new_value = input('new value> :')

            self.c.execute(UPDATE_PATIENT_INFO.format(column), [new_value,
                                                                patient_name])
            self.db.commit()

            if column == 'FIRSTNAME':
                patient_name = new_value

    def update_doctor(self):
        input_ = True
        doctor_name = input('name> :')
        # TODO check if doctor name is valid
        # Throw an error if it is not

        print('When you are ready type "exit"')
        print('Which column you\'d like to update?')
        print('Available columns => firstname, lastname')

        while input_:
            column = input('column> :').upper()

            if column == 'EXIT':
                input_ = False
                break

            while column not in DOCTOR_COLUMNS and column is not 'EXIT':
                print('No such column')
                column = input('column> :').upper()

            new_value = input('new value> :')

            self.c.execute(UPDATE_DOCTOR_INFO.format(column), [new_value,
                                                               doctor_name])
            self.db.commit()

            if column == 'FIRSTNAME':
                doctor_name = new_value

    def update_hospital_stay(self):
        input_ = True
        patient_name = input('Patient name> :')
        patient = self.get_patient(patient_name)
        patient_id = [p['id'] for p in patient][0]

        print('When you are ready type "exit"')
        print('Which column you\'d like to update?')
        print('Available columns => room, startdate, enddate, injury')

        while input_:
            column = input('column> :').upper()

            if column == 'EXIT':
                input_ = False
                break

            '''EXIT does not work inside the loop below'''
            while column not in HOSPITAL_STAY_COLUMNS and column is not 'EXIT':
                print('No such column')
                column = input('column> :').upper()

            new_value = input('new value> :')

            self.c.execute(UPDATE_HOSPITAL_STAY.format(column), [new_value,
                                                                 patient_id])
            self.db.commit()

    def delete_patient(self):
        patient_name = input('Patient name> :')
        print('Are you sure you want to delete {} from the database?'
              .format(patient_name))
        confirmation = input('Y/N> :')

        if confirmation == 'Y':
            self.c.execute(DELETE_PATIENT, [patient_name])
            self.db.commit()
            print('{} has been removed successfully'.format(patient_name))

    def delete_doctor(self):
        doctor_name = input('Doctor name> :')
        print('Are you sure you want to delete {} from the database?'
              .format(doctor_name))
        confirmation = input('Y/N> :')

        if confirmation == 'Y':
            self.c.execute(DELETE_DOCTOR, [doctor_name])
            self.db.commit()
            print('{} has been removed successfully'.format(doctor_name))

    def delete_hospital_stay(self):
        patient_name = input('Patient name> :')
        patient = self.get_patient(patient_name)
        patient_id = [p['id'] for p in patient][0]

        print('Are you sure you want to delete {}\'s stay from the database?'
              .format(patient_name))
        confirmation = input('Y/N> :')

        if confirmation == 'Y':
            self.c.execute(DELETE_HOSPITAL_STAY, [patient_id])
            self.db.commit()
            print('{}\'s stay has been removed from the database'.
                  format(patient_name))


def main():
    h = Hospital('py_hospital.db')
    h.list_patients()
    # h.list_doctors()
    # h.list_patients_from_to()
    # h.list_doctors_by_injury()
    # h.list_patients_by_injury()
    # h.list_all_patients_of_a_doctor()
    # h.delete_hospital_stay()
    # h.update_doctor()
    # h.add_hospital_stay_of_a_patient()
    # h.update_doctor()

if __name__ == '__main__':
    main()

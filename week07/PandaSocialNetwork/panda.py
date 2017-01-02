import re


class Panda:

    def __init__(self, name, email, gender):
        self._name = name
        self._email = self.validate_email(email)
        self._gender = gender

    def __str__(self):
        return 'name: {}, email: {}, gender: {}'.format(self._name,
                                                        self._email,
                                                        self._gender)

    def __eq__(self, other):
        return self._name == other._name and \
            self._email == other._email and self._gender == other._gender

    def __hash__(self):
        return hash(self.__str__())

    @staticmethod
    def validate_email(email):
        if not re.match(r'^[\w\.\-]+@[a-zA-Z\d\-]+\.[a-zA-Z]+$', email):
            raise ValueError("Invalid email")

        return email

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return self.gender() == 'male'

    def isFemail(self):
        return self.gender() == 'female'

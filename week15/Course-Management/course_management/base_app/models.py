from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @classmethod
    def exists(cls, email):
        return True if cls.objects.filter(email=email) else False


class Student(User):
    pass


class Lecturer(User):
    pass

from django.db import models
from courses.models import Course


class Lecture(models.Model):
    name = models.CharField(max_length=60)
    week = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)

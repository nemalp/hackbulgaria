from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

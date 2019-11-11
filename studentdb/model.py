from django.db import models

class StudentDB(models.Model):
    fisrtname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    age = models.FloatField()
    email = models.CharField(max_length=100)

from django.db import models

class MilitaryRecruitmentDB(models.Model):
    name = models.CharField(max_length = 50)
    age = models.FloatField()
    has_glasses = models.BooleanField()

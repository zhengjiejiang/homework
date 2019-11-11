from django.db import models

class CalculatorMemory(models.Model):
    value = models.FloatField()

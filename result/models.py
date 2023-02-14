from django.db import models


class Result(models.Model):
    address = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    temperature = models.IntegerField()

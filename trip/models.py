from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField, TextField

# Create your models here.
class Test(models.Model):
    test = models.CharField(max_length=10)
    def __str__(self):
        return self.test

class Trip(models.Model):
    userName = models.CharField(max_length=30)
    tripName = models.CharField(max_length=30)
    data = models.TextField()
 #   latitude = models.FloatField()
 #   longitutde = models.FloatField()
 #   index = models.IntegerField()
    totalLength = models.IntegerField()

    def __str__(self):
        return self.tripName + " " + self.totalLength
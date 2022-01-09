from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField, TextField

# Create your models here.
class Test(models.Model):
    test = models.CharField(max_length=10)
    def __str__(self):
        return self.test

class Trip(models.Model):
    userName = models.TextField()
    tripName = models.TextField()
    data = models.TextField()
    totalLength = models.IntegerField()

    def __str__(self):
        return self.tripName + " " + str(self.totalLength)
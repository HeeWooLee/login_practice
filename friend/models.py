from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField, TextField

# Create your models here.
class Test(models.Model):
    test = models.CharField(max_length=10)
    def __str__(self):
        return self.test

class Friend(models.Model):
    userName = models.TextField()
    userFriend = models.TextField()  

    def __str__(self):
        return self.userName + " " + self.userFriend
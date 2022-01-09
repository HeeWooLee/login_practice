from django.db import models

# Create your models here.
class Test(models.Model):
    test = models.CharField(max_length=10)
    def __str__(self):
        return self.test

class Hey(models.Model):
    userName = models.CharField(max_length=10)
    passWord = models.CharField(max_length=10)
    def __str__(self):
        return self.userName + " " + self.passWord
from django.db import models
from django.contrib.auth.models import User, Group

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    saldo = models.IntegerField()
    sueldo = models.IntegerField()

    def __str__(self):
        return self.name
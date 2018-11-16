from django.db import models

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=20,unique=True)
    root = models.CharField(max_length=100)
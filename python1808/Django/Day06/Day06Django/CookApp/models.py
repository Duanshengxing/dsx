from django.db import models

# Create your models here.

class UserModels(models.Model):
    user = models.CharField(max_length=20,unique=True)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return self.user
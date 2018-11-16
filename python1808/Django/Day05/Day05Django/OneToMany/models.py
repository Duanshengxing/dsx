from django.db import models

# Create your models here.



class UserType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    user_type_id = models.ForeignKey(UserType)
    def __str__(self):
        return self.name




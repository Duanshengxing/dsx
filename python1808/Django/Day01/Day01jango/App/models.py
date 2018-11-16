from django.db import models

# Create your models here.


class Grade(models.Model):
    name = models.CharField(max_length=20,null=False,primary_key=True)
    date = models.DateTimeField()
    girl_num = models.IntegerField()
    boy_num = models.IntegerField()
    is_delete = models.BooleanField(default=False)



class Student(models.Model):
    choce = (
        (0,u'男'),
        (1,u'女'),
    )
    name = models.CharField(max_length=20,null=False)
    age = models.IntegerField()
    gender = models.IntegerField(choices=choce)
    info = models.CharField(max_length=50)
    is_delete = models.BooleanField(default=False)



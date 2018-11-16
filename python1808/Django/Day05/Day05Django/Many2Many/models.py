from django.db import models

# 多对多


# 用户和组： 多对多
#   组： 可以包含多个用户
#   用户: 可以属于多个分组

# 组 Group
class Group(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# 用户 User
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    password = models.CharField(max_length=200)
    groups = models.ManyToManyField(Group)

    girl_num = models.IntegerField()
    boy_num = models.IntegerField()

    def __str__(self):
        return self.name















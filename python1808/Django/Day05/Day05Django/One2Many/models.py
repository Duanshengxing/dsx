from django.db import models


# 一对多

# class UserInfo(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#     user_type = models.CharField(max_length=30)


# 用户类型
class UserType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


def fn():
    return 2

# 用户信息
class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    user_type = models.ForeignKey(UserType)
    # user_type = models.ForeignKey(UserType, related_name='info')

    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)  # 默认值,级联删除
    # user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)  # 保护，阻止删除 (常用)
    # user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True)  # 删除时会设置为null
    # user_type = models.ForeignKey(UserType, on_delete=models.SET_DEFAULT, default=2)  # 删除时会设置为default值
    # user_type = models.ForeignKey(UserType, on_delete=models.SET(fn))  # 删除时会设置为指定值
    # user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)  # 删除时不会影响其他表 (常用)


    def __str__(self):
        return self.name


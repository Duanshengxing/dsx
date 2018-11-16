from django.db import models

# Create your models here.

class Student(models.Model):
    # pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, name='姓名', verbose_name='姓名', db_index=True, editable=False)
    # age = models.IntegerField(default=18)
    # address = models.TextField()
    # height = models.FloatField(default=1.80)
    # sex = models.BooleanField(default=True)

    # weight = models.DecimalField(max_digits=6, decimal_places=2, default=140.23)
    # n = models.NullBooleanField(default=True)

    # birthday = models.DateTimeField(auto_now=True)  # 自动更新最新一次修改的时间
    # birthday2 = models.DateTimeField(auto_now_add=True)  # 表创建时自动添加的时间，以后不会改变

    # d = models.DateField()
    # t = models.TimeField()

    # file = models.FileField()
    # img = models.ImageField()

    # http 状态码
    #  2xx： 成功
    #  3xx: 重定向
    #  4xx: 客户端错误
    #  5xx: 服务端错误

    # type_list = (
    #     (1, "青铜用户"),
    #     (2, "白银用户"),
    #     (3, "黄金用户"),
    #     (4, "铂金用户"),
    #     (5, "钻石用户"),
    #     (6, "星耀用户"),
    #     (7, "王者用户"),
    # )
    # user_type = models.IntegerField(choices=type_list, default=1)
    #
    # class Meta:
    #     db_table = 'Person'  # 表名
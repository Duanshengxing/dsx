from django.db import models

# 一对一

# 身份证
class IdCard(models.Model):
    idnum = models.CharField(max_length=18)

    def __str__(self):
        return self.idnum



# 定制Manager
# 男人累
class ManManager(models.Manager):
    # 修改默认的查询集
    # 重写父类的方法
    def get_queryset(self):
        return super().get_queryset().filter(sex=True)
    # 自定义数据操作
    def search(self, name):
        return self.filter(name__contains=name)

# 女人泪
class FemaleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(sex=False)
    # 查找姓name的人
    def search(self, name):
        return self.filter(name__startswith=name)


# 人
class Person(models.Model):
    name = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    idcard = models.OneToOneField(IdCard)

    # 把objects改名，原来的objects不可以使用了
    # m = models.Manager()

    # 管理男人
    man = ManManager()
    female = FemaleManager()  # 管理女人

    objects = models.Manager()


    def __str__(self):
        return self.name










# 一对多： ForiegnKey(),
#       正向: userinfo.user_type（对象）
#       反向: usertype.userinfo_set.all()（集合）
# 多对多： ManyToMany()
#       正向: user.groups.all() （集合）
#       反向: group.user_set.all() （集合）
# 一对一： OneToOne()
#       正向: person.idcard（对象）
#       反向: idcard.person（对象）



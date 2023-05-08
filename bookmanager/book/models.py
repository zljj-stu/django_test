from django.db import models

# Create your models here.
'''
1、模型类需要继承models.Model
2、系统自动添加主键--id
3、字段定义：字段名=model.类型(选项)，不要与关键字重名
'''


class BookInfo(models.Model):
    # 相当于varchar(10)
    name = models.CharField(max_length=10)

    def __str__(self):
        # 重写str方法使得显示name
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束，人数属于那本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

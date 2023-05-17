from django.db import models

# Create your models here.
'''
1、模型类需要继承models.Model
2、系统自动添加主键--id
3、字段定义：字段名=model.类型(选项)，不要与关键字重名
4、数据类型为MySQL中一致
5、verbose_name属性用于设置该应用的直观可读的名字
6、表名默认为子应用名_类名（全部小写），
'''


class BookInfo(models.Model):
    # 相当于varchar(10)
    name = models.CharField(max_length=10, unique=True)
    pub_date=models.DateField(null=True)
    # 阅读量
    readcount=models.IntegerField(default=0)
    # 评论量
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    class Meta:
        # 修改表的名字
        db_table= 'bookinfo'
        verbose_name= '书籍管理'

    def __str__(self):
        # 重写str方法使得显示name
        return self.name


class PeopleInfo(models.Model):

    name = models.CharField(max_length=10, unique=True)
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female'),
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    # 外键约束，人数属于那本书;系统自动为外键添加_id;删除时级联删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        # 修改表的名字
        db_table= 'peopleinfo'
        verbose_name= '人员管理'

    def __str__(self):
        return self.name

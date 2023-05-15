from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from book.models import BookInfo
# Create your views here.
'''
视图函数有以下要求
1、接受请求request(HttpRequest的类对象)
2、必须返回响应response(HttpResponse的类对象)
'''
def index(request):
    # return HttpResponse('ok')
    books = BookInfo.objects.all()
    print(books)
    # return render(request, 'index.html', context=context)
    return HttpResponse('index')


# 增加信息
# 方式一,保存到数据库必须调用save方法
books=BookInfo(
    name='django',
    pub_date='2000-1-1',
    readcount=10,
)
books.save()

# 方式二
BookInfo.objects.create(
    name='2023联考',
    pub_date='2023-4-2',
    readcount=100,
)

# 修改数据
# 方式一，根据get改，需要调用save
book = BookInfo.objects.get(id=6)
book.name = '2023事业单位联考'
book.save()

# 方式二，filter
BookInfo.objects.filter(id=6).update(name='湖北事业单位联考', commentcount=666)


# 删除数据，物理和逻辑删除
# 物理删除
# book = B
# 逻辑删除
# BookInfo.objects.filter(id=6).update(is_delete=True)

# 查询
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
# all查询多个结果。
# count查询结果数量。
# 实现SQL中的where功能，包括
#     filter过滤出多个结果,结果为列表
#     exclude排除掉符合条件剩下的结果
#     get过滤单一结果，结果为一个对象
# 过滤条件的表达语法如下：属性名称__比较运算符=值,exact：表示判等,contains：是否包含
# 查询编号为1的图书
book = BookInfo.objects.get(id=1)  # 简写
book = BookInfo.objects.get(id__exact=1)  # 完整写法
book = BookInfo.objects.get(pk=1)  # 主键
# 查询书名包含'湖'的图书
book = BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
book = BookInfo.objects.filter(name__endswith='湖')
# 查询书名为空的图书
book = BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
book = BookInfo.objects.filter(id__in=[1, 4, 5])
# 查询编号大于3的图书
# 比较查询
#     gt大于 (greater then)
#     gte大于等于 (greater then equal)
#     lt小于 (less then)
#     lte小于等于 (less then equal)
book = BookInfo.objects.filter(id__gt=3)
# 不等于的运算符，使用exclude()过滤器
book = BookInfo.objects.exclude(id=3)
# 查询1980年发表的图书
book = BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
book = BookInfo.objects.filter(pub_date__gt='1990-1-1')
# 之前的查询都是对象的属性与常量值比较，两个属性怎么比较呢？ 答：使用F对象，被定义在django.db.models中
from django.db.models import F
# 查询阅读量大于等于评论量的图书,可以在F对象上使用算数运算。
data = BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
# 多条件查询
book = BookInfo.objects.filter(id__gt=3).filter(readcount__gt=20)
book = BookInfo.objects.filter(id__gt=3, readcount__gt=20)
# 或查询，如果需要实现逻辑或or的查询，需要使用Q()对象结合|运算符，Q对象被义在django.db.models中
from django.db.models import Q
book = BookInfo.objects.filter(Q(id__gt=3) | Q(readcount__gt=20))
# Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或,Q对象前可以使用~操作符，表示非not
book = BookInfo.objects.filter(~Q(id=3))
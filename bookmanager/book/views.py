from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from book.models import BookInfo, PeopleInfo
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

def shop(request, city_id, shop_id):
    # 获取查询参数,返回一个字典
    query_params = request.GET
    # querydict允许一键多值，getlist获取多值，get获取最后一个
    print(city_id, shop_id, query_params, query_params.getlist('order'), query_params['order'])
    return HttpResponse('zlj')


# # 增加信息
# # 方式一,保存到数据库必须调用save方法
# books=BookInfo(
#     name='django',
#     pub_date='2000-1-1',
#     readcount=10,
# )
# books.save()
#
# # 方式二
# BookInfo.objects.create(
#     name='2023联考',
#     pub_date='2023-4-2',
#     readcount=100,
# )
#
# # 修改数据
# # 方式一，根据get改，需要调用save
# book = BookInfo.objects.get(id=6)
# book.name = '2023事业单位联考'
# book.save()
#
# # 方式二，filter
# BookInfo.objects.filter(id=6).update(name='湖北事业单位联考', commentcount=666)
#
#
# # 删除数据，物理和逻辑删除
# # 物理删除
# # book = B
# # 逻辑删除
# # BookInfo.objects.filter(id=6).update(is_delete=True)
#
# # 查询
# # get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
# # all查询多个结果。
# # count查询结果数量。
# # 实现SQL中的where功能，包括
# #     filter过滤出多个结果,结果为列表
# #     exclude排除掉符合条件剩下的结果
# #     get过滤单一结果，结果为一个对象
# # 过滤条件的表达语法如下：属性名称__比较运算符=值,exact：表示判等,contains：是否包含
# # 查询编号为1的图书
# book = BookInfo.objects.get(id=1)  # 简写
# book = BookInfo.objects.get(id__exact=1)  # 完整写法
# book = BookInfo.objects.get(pk=1)  # 主键
# # 查询书名包含'湖'的图书
# book = BookInfo.objects.filter(name__contains='湖')
# # 查询书名以'部'结尾的图书
# book = BookInfo.objects.filter(name__endswith='湖')
# # 查询书名为空的图书
# book = BookInfo.objects.filter(name__isnull=True)
# # 查询编号为1或3或5的图书
# book = BookInfo.objects.filter(id__in=[1, 4, 5])
# # 查询编号大于3的图书
# # 比较查询
# #     gt大于 (greater then)
# #     gte大于等于 (greater then equal)
# #     lt小于 (less then)
# #     lte小于等于 (less then equal)
# book = BookInfo.objects.filter(id__gt=3)
# # 不等于的运算符，使用exclude()过滤器
# book = BookInfo.objects.exclude(id=3)
# # 查询1980年发表的图书
# book = BookInfo.objects.filter(pub_date__year=1980)
# # 查询1990年1月1日后发表的图书
# book = BookInfo.objects.filter(pub_date__gt='1990-1-1')
# # 之前的查询都是对象的属性与常量值比较，两个属性怎么比较呢？ 答：使用F对象，被定义在django.db.models中
# from django.db.models import F
# # 查询阅读量大于等于评论量的图书,可以在F对象上使用算数运算。
# data = BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
# # 多条件查询
# book = BookInfo.objects.filter(id__gt=3).filter(readcount__gt=20)
# book = BookInfo.objects.filter(id__gt=3, readcount__gt=20)
# # 或查询，如果需要实现逻辑或or的查询，需要使用Q()对象结合|运算符，Q对象被义在django.db.models中
# from django.db.models import Q
# book = BookInfo.objects.filter(Q(id__gt=3) | Q(readcount__gt=20))
# # Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或,Q对象前可以使用~操作符，表示非not
# book = BookInfo.objects.filter(~Q(id=3))
# # 聚合函数,使用aggregate()过滤器调用聚合函数,aggregate的返回值是一个字典类型{'属性名__聚合类小写':值},count时一般不使用aggregate()过滤器
# from django.db.models import Sum, Avg, Count, Max, Min
# num = BookInfo.objects.aggregate(Sum('readcount'))
# num = BookInfo.objects.count()
# # 使用order_by对结果进行排序,默认升序
# book = BookInfo.objects.all().order_by('readcount')
# # 降序
# book = BookInfo.objects.all().order_by('-readcount')
# # 级联查询
# # 查询书籍为1的所有人物信息
# # 由一到多的访问语法：一对应的模型类对象.多对应的模型类名小写_set 例：
# book = BookInfo.objects.get(id=1)
# book.peopleinfo_set.all()
# # 查询人物为1的书籍信息
# person = PeopleInfo.objects.get(id=1)
# # 关联的过滤查询,关联模型类名小写__属性名__条件运算符=值
# # 查询图书，要求图书人物为"郭靖"
# BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
# # 查询图书，要求图书中人物的描述包含"八"
# book = BookInfo.objects.filter(peopleinfo__description__contains='八')
# # 查询书名为“天龙八部”的所有人物
# people = PeopleInfo.objects.filter(book__name='天龙八部')
# # 查询图书阅读量大于30的所有人物
# people = PeopleInfo.objects.filter(book__readcount__gt=30)
# # Django的ORM中存在查询集的概念。
# #
# # 查询集，也称查询结果集、QuerySet，表示从数据库中获取的对象集合。
# #
# # 当调用如下过滤器方法时，Django会返回查询集（而不是简单的列表）：
# #
# #     all()：返回所有数据。
# #     filter()：返回满足条件的数据。
# #     exclude()：返回满足条件之外的数据。
# #     order_by()：对结果进行排序。
# #
# # 对查询集可以再次调用过滤器进行过滤
# # 创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用
# # 使用同一个查询集，第一次使用时会发生数据库的查询，然后Django会把结果缓存下来，再次使用这个查询集时会使用缓存的数据，减少了数据库的查询次数。
# # 可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句。不支持负数索引
# # 分页
# #查询数据
# books = BookInfo.objects.all()
# #导入分页类
# from django.core.paginator import Paginator
# #创建分页实例
# paginator=Paginator(books,2)
# #获取指定页码的数据
# page_books = paginator.page(1)
# #获取分页数据
# total_page=paginator.num_pages
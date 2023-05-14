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

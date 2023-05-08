from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
'''
视图函数有以下要求
1、接受请求request(HttpRequest的类对象)
2、必须返回响应response(HttpResponse的类对象)
'''
def index(request):
    return HttpResponse('ok')

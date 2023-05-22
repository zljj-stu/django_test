from django.contrib import admin
# 转换器相关
from django.urls import converters
# 用于注册转换器
from django.urls.converters import register_converter
from django.urls import path
from book.views import *


# 自定义转换器
class Shop_idConverter:
    # 修改正则规则
    regex = "1[3-9]\d{9}"

    # 验证无误的数据给视图函数
    def to_python(self, value):
        return value

    # 匹配结果用于反向解析传值时使用
    def to_url(self, value):
        return value


# 注册转换器,参数为转换器名和类型名
register_converter(Shop_idConverter, 'phone')

urlpatterns = [
    path('index/', index),
    # 转换器：变量名，转换器对变量数据正则验证
    path('<int:city_id>/<phone:shop_id>/', shop),
    path('register/', register),
    path('json/', json_learn),
    path('method/', method),
    path('res/', res),
    path('jsres/', json_res),
    path('redir/', redir),
    path('cookie/', set_cookie),
    path('get_cookie/', get_cookie),
]

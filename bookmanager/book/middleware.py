# 测试中间件的使用
from django.utils.deprecation import MiddlewareMixin
class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print("每次请求前执行")
        username = request.COOKIES.get('username')
        if username is None:
            print("无用户信息")
        else:
            print('有用户信息')

    def process_response(self, request, response):
        print("每次响应前都会调用")
        return response


class TestMiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print("****每次请求前执行")
        # username = request.COOKIES.get('username')
        # if username is None:
        #     print("无用户信息")
        # else:
        #     print('有用户信息')

    def process_response(self, request, response):
        print("****每次响应前都会调用")
        return response
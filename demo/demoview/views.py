from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# 创建视图函数indexview
def indexview(request):
    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':

        # 根据不同的请求方式,做不同的操作处理:
        return HttpResponse('indexview get func')

    else:
        # 根据不同的请求方式,做不同的操作处理:

        return HttpResponse('indexview pots func')


# 导入类视图的父类View
from django.views.generic import View


class RegisterView(View):
    """
    类视图：处理注册
    """

    def get(self, requset):
        """
        处理GET请求，返回注册页面
        """
        return HttpResponse('get func')

    def post(self, request):
        """
         处理POST请求，返回注册页面
         """
        return HttpResponse('pots func')


from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator


# 定义第一个装饰器
def my_decorator(func):
    def wrapper(request, *args, **kwargs):  # 第一个参数request对象
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)  # 此处增加了self

    return wrapper


# 定义的第二个装饰器:
def my_decorator2(func):
    def wrjapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)

    return wrjapper


# 额外增加的第一个扩展类
class BaseView(object):
    # 第一次重写父类中的as_view方法
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        # 对获取的view第一次添加装饰器
        return my_decorator(view)


# 额外增加的第二个扩展类
class Base2View(object):
    # 第二次重写父类中的as_view方法
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        # 对获取的view进行第二次添加装饰器
        return my_decorator2(view)


# 我们定义的类视图, 继承自两个额外增加的类
class Demoview(BaseView, Base2View, View):
    # 类视图的get方法
    def get(self, requset):
        print('get')
        return HttpResponse('get func')

    # 类视图的post方法
    def post(self, requset):
        print('post')
        return HttpResponse('post func')

from django.shortcuts import render, redirect

# Create your views here.

# 从django.http模块中导入HttpRespose
from django.http import HttpResponse
from django.urls import reverse


def index(request,a): #1.必须有参数requst
    """
     index视图
    :param requst: 响应对象，包含了请求信息的请求对象
    :return: 返回
    """
    print(a)
    # 2.必须有返回
    # a = 1 / 0
    return HttpResponse('hello ')


def say(request):
    return HttpResponse("say func")


def sayhello(request):

    # reverse('命名空间的名称:name中的名字')

    url = reverse('userspace:sayname')

    print(url)

    # return HttpResponse('sayhello func')
    # 跳转从定向，应用场景支付宝，支付成功，跳转
    return redirect(url)

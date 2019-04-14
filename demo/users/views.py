import json
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


# 表单类型 (Form Data)
def req(request):
    a = request.POST.get('a')
    b = request.POST.get('b')

    alist = request.POST.getlist('a')

    print(a)
    print(b)
    print(alist)

    return HttpResponse('ok req')


# 非表单类型 (Non-Form Data)
def jsonData(request):
    # 返回的字典类型
    json_bytes = request.body
    # 数据解码
    json_str = json_bytes.decode()

    # python3.6及以上版本中, json.loads()方法可以接收str和bytes类型
    # 但是python3.5以及以下版本中, json.loads()方法只能接收str, 所以我们的版本如果是
    # 3.5 需要有上面的编码步骤.

    #拆包
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])

    return HttpResponse('ok json')


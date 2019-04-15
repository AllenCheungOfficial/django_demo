from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.

# 表单类型


def req(request):
    # request.POST属性获取qd对象
    qd= request.POST

    # get 一k一v
    a = qd.get('a')
    b = qd.get('b')

    # getlist 一k多v
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)

    return HttpResponse('OK')


# 非表单类型
def form(request):
    # request.body返回bytes类型。
    # 获取参数,然后解码: str
    json_bytes = request.body
    # 编码
    json_str = json_bytes.decode()

    # python3.6及以上版本中, json.loads()方法可以接收str和bytes类型
    # 但是python3.5以及以下版本中, json.loads()方法只能接收str, 所以我们的版本如果是
    # 3.5 需要有上面的编码步骤.

    # json.loads: 把字符串变为python字典:
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('OK')


# request.META为字典类型
def getheadrs(request):
    content_type = request.META['CONTENT_TYPE']
    leg = request.META['CONTENT_LENGTH']
    print(content_type)
    print(leg)

    print(request.method)
    print(request.user)

    return HttpResponse('ok')


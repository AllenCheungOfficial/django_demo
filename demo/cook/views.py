from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

# HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)

def setcook(request):
    # 设置cookie:
    response = HttpResponse('cookie ok')

    # 设置cookie有效时间
    response.set_cookie('Mrzhang','1',max_age=3600*24)

    # 默认有效期,不同的浏览器,时间不同
    response.set_cookie('ls','1')

    return response

def getcook(requst):

    # 读取cookie
    # 通过HttpRequest对象的COOKIES属性来读取本次请求携带的cookie值。
    # request.COOKIES为字典类型
    value = requst.COOKIES.get('ls')

    print(value)

    return HttpResponse('cookie ok')


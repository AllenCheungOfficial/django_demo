from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def setsession(request):

    # 保存session数据
    request.session['one'] = '1'

    return HttpResponse('set session')

def getsession(request):
    # 获取session数据
    value = request.session['one']
    print(value)
    return HttpResponse('getsession')

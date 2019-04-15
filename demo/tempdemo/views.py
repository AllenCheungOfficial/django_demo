from django.shortcuts import render
import datetime
# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    # 定义模板字典数据
    context = {
        '黑马': 'itheima',
        'list':[
            'A', 'B', 'C'
        ],
        'dict':{
            'name':'zhangyan',
            'age':18
        },
        'bianliang':'<a href="#">这是a标签</a>',

        'value':datetime.datetime.now(),

    }
    # 调用render函数
    # 调试模板继承需要注释
    # return render(request, 'index.html',context=context)
    return render(request, 'son.html')

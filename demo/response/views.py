from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


# HttpResponse(
#     content=响应体,
#     content_type=响应体数据类型,
#     status=状态码
# )
def responsedemo(request):

    print('responsedemo')

    # return HttpResponse('hello',content_type="application/json",status=400)

    response = HttpResponse('hello', content_type='application/json', status=404)

    response['itcast'] = 'python'

    return response


# 帮助我们将数据转换为json字符串
# 设置响应头Content-Type为 application/json
def jsonResponse(request):
    print('jsonResponse')

    # 字典转换json格式
    # dict = {
    #     'a':123,
    #     'b':1345,
    # }
    #
    # return JsonResponse(dict)

    list = [
        {
            'a':123,
            'b':"33",
        }
    ]

    # 非字典要写safe=false
    return JsonResponse(list,safe=False)
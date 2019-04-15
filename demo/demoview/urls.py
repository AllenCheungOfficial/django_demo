# 从urls模块中导入url
from django.conf.urls import url


# 从当前目录导入我们的视图模块views
from . import views

urlpatterns = [
    # 添加一个视图函数的路由
    url(r'^indexview/$', views.indexview),

    # 定义类视图, 且类视图继承自View
    # 注意:
    # url(路径, 执行的函数)
    # url的第二个参数需要是一个函数
    # 我们这里如果传入: views.RegisterView 会发现这个是一个类, 不是一个函数,
    # 所以我们需要调用系统给我们提供的 as_view() 方法
    url(r'^vw/$', views.RegisterView.as_view()),
    url(r'^demov/$', views.Demoview.as_view()),

]
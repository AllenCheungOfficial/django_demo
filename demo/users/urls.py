"""
定义路由URL
在子应用中新建一个urls.py文件用于保存该应用的路由
在users/urls.py文件中定义路由信息。
"""
# 从urls模块中导入url
from django.conf.urls import url

# 从当前目录导入我们的视图模块views
from . import views

# urlpatterns是被django自动识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^index/(\d{4})/$', views.index),
    url(r'^say/$', views.say,name='sayname'),
    url(r'^sayhello/$', views.sayhello),

]

"""
总路由
demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# 在工程总路由demo/urls.py中添加子应用的路由数据


from django.conf.urls import url, include  # 使用include来将子应用users里的全部路由包含进工程路由中

from django.contrib import admin

urlpatterns = [
    # django默认包含的,这个我们不用关心
    url(r'^admin/', admin.site.urls),
    # 把子路由信息添加到总路由中
    url(r'users/',include('users.urls',namespace='userspace'))
    # url(r'^', include('users.urls', namespace='userspace')),

]

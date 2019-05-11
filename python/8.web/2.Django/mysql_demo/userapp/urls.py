"""mysql_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# 导入视图模块
from userapp import views

# https://docs.djangoproject.com/zh-hans/2.2/topics/http/urls/#path-converters
urlpatterns = [
    # /user/index 个人中心
    path('index', views.index, name="index"),
    path('add', views.add, name="add"),
    path('detail/', views.detail),
    # /user/detail/1
    path('detail/<int:id>', views.detail, name="detail"),
    # 不包含/的任意字符
    path('test/<str:obj>', views.test),
    # 匹配任何非空字符串，包括路径分隔符 '/'
    # eg：https://www.baidu.com我的个%20神啊~!@$%%5E&*()_+%7C
    path('test2/<path:obj>', views.test),

]

from django.urls import path

from . import views

# 2.进行url配置（建立url地址和视图的对应关系）
urlpatterns = [
    # /users/index ==> view的index处理函数
    path('index', views.index),
    path('list', views.list),
]

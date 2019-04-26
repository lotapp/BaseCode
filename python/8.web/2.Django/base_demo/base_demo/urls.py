"""base_demo URL Configuration

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
from django.contrib import admin
from django.urls import path, include

# 项目urls配置文件
urlpatterns = [
    # 设置管理后台的路径（eg：/root/）
    path('root/', admin.site.urls),  # 可修改默认的admin
    path('users/', include("users.urls")),  # 配置项
]

# old Code
# from django.conf.urls import include, url
#
# urlpatterns = [
#     url(r'^admin', include(admin.site.urls)),
#     url(r'^users', include('users.urls'))
# ]

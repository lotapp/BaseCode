from django.shortcuts import render, redirect
from django.http import HttpResponse


# 个人中心
def index(request):
    return render(request, 'userapp/index.html', {"name": "张三", "id": 1})


# 添加页面
def add(request):
    return HttpResponse("add")


# 详情页
def detail(request, id=0):
    if id > 0:
        return HttpResponse(id)
    else:
        return redirect("add")  # 重定向到add视图函数

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


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


# 测试视图函数
def test(request, obj):
    # print(dir(request))
    print(request.path)
    print(request.method)
    print(request.encoding)  # None则为浏览器默认编码格式
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse(obj)

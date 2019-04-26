from django.shortcuts import render
from django.http import HttpResponse


# 1.定义视图函数
# http://127.0.0.1:8000/users/index
def index(request):
    print(request)
    # 响应浏览器请求（需要页面就去T拿，需要数据就去M找）
    return HttpResponse('这是users应用模块的index页面哦~')

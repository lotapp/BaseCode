from django.shortcuts import render
from django.http import HttpResponse


# 1.定义视图函数
# http://127.0.0.1:8000/users/index
def index(request):
    print(request)
    # 响应浏览器请求（需要页面就去T拿，需要数据就去M找）
    return HttpResponse('这是users应用模块的index页面哦~')


# 演示模版
def list(request):
    from users.models import UserInfo
    # 第二个参数：读取哪个模版（和net中的View("~/Views/xxx/xxx.cshtml")类似）
    # 第三参数：传一个dict进入模版，这边的key(users)就是模版遍历的对象
    # UserInfo.objects.all() 获取数据库中所有userinfo信息（是类名而不是对象名哦~）
    return render(request, "list.html", {"users": UserInfo.objects.all()})

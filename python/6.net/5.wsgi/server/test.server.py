# Python服务器网关接口：https://www.python.org/dev/peps/pep-3333/
# 从wsgiref模块导入:https://docs.python.org/3/library/wsgiref.html
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from test import application
# from hello import application

# 创建一个服务器，端口是8080，处理函数是application:
httpd = make_server('', 8080, application)
print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()
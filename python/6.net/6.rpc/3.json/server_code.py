# 和上一节一样
# 5.RPC Server（被调用者）本地执行后将结果返回给服务端的RPC Proxy
class MyCode(object):
    def sum(self, a, b):
        return a + b

    def get_time(self):
        import time
        return time.ctime()
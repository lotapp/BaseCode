# 定义一个临时类
class Temp(object):
    def __del__(self):
        print("你被干掉了")
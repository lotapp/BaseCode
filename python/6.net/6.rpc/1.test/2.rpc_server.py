import zerorpc


class Test(object):
    def say_hi(self, name):
        return f"Hi，My Name is{name}"


# 注册一个Test的实例
server = zerorpc.Server(Test())
server.bind("tcp://0.0.0.0:5438")
server.run()
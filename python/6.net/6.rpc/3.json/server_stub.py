import json
import socket


class ServerStub(object):
    def __init__(self, mycode):
        self.mycode = mycode

    def unpack(self, data):
        """3.服务端的RPC Proxy组件把通过网络接收到的数据包按照相应格式进行拆包解码，获取方法名和参数"""
        data = data.decode("utf-8")
        # 格式应该是"格式：{"func": "sum", "args": [1, 2]}"
        data = json.loads(data)
        func, args = data["func"], data["args"]
        if args:
            return (func, tuple(args))  # (func,args)
        return (func, )

    def pack(self, result):
        """打包：把方法和参数拼接成自定义的协议"""
        # 格式："data:返回值"
        json_str = json.dumps({"data": result})
        return json_str.encode("utf-8")

    def exec(self, func, args=None):
        """4.服务端的RPC Proxy组件根据方法名和参数进行本地调用"""
        # 如果没有这个方法则返回None
        func = getattr(self.mycode, func)
        if args:
            return func(*args)  # 解包
        else:
            return func()  # 无参函数

    def handle(self, client_socket, client_addr):
        while True:
            # 获取客户端发送的数据包
            data = client_socket.recv(2048)
            if data:
                try:
                    data = self.unpack(data)  # 解包
                    if len(data) == 1:
                        data = self.exec(data[0])  # 执行无参函数
                    elif len(data) > 1:
                        data = self.exec(data[0], data[1])  # 执行带参函数
                    else:
                        data = "RPC Server Error Code:500"
                except Exception as ex:
                    data = "RPC Server Function Error"
                    print(ex)
                # 6.服务端的RPC Proxy组件将返回值打包编码成自定义的协议数据包，并通过网络发送给客户端的RPC Proxy组件
                data = self.pack(data)  # 把函数执行结果按指定协议打包
                # 把处理过的数据发送给客户端
                client_socket.send(data)
            else:
                print(f"客户端：{client_addr}已断开\n")
                break
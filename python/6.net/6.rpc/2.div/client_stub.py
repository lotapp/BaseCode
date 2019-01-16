import socket


class ClientStub(object):
    def __init__(self, address):
        """address ==> (ip,port)"""
        self.socket = socket.socket()
        self.socket.connect(address)

    def convert(self, obj):
        """根据类型转换成对应的类型编号"""
        if isinstance(obj, int):
            return 1
        if isinstance(obj, float):
            return 2
        if isinstance(obj, str):
            return 3

    def pack(self, func, args):
        """打包：把方法和参数拼接成自定义的协议
        格式：func:函数名@params:类型-参数,类型2-参数2...
        """
        result = f"func:{func}"
        if args:
            params = ""
            # params:类型-参数,类型2-参数2...
            for item in args:
                params += f"{self.convert(item)}-{item},"
            # 去除最后一个,
            result += f"@params:{params[:-1]}"
        # print(result)  # log 输出
        return result.encode("utf-8")

    def unpack(self, data):
        """解包：获取返回结果"""
        msg = data.decode("utf-8")
        # 格式应该是"data:xxxx"
        params = msg.split(":")
        if len(params) > 1:
            return params[1]
        return None

    def get(self, func, args=None):
        """1.客户端的RPC Proxy组件收到调用后，负责将被调用的方法名、参数等打包编码成自定义的协议"""
        data = self.pack(func, args)
        # 2.客户端的RPC Proxy组件在打包完成后通过网络把数据包发送给RPC Server
        self.socket.send(data)
        # 等待服务端返回结果
        data = self.socket.recv(2048)
        if data:
            return self.unpack(data)
        return None

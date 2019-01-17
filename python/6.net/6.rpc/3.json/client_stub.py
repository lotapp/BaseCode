import json
import socket


class ClientStub(object):
    def __init__(self, address):
        """address ==> (ip,port)"""
        self.socket = socket.socket()
        self.socket.connect(address)

    def pack(self, func, args):
        """打包：把方法和参数拼接成自定义的协议
        格式：{"func": "sum", "args": [1, 2]}
        """
        json_str = json.dumps({"func": func, "args": args})
        # print(json_str)  # log 输出
        return json_str.encode("utf-8")

    def unpack(self, data):
        """解包：获取返回结果"""
        data = data.decode("utf-8")
        # 格式应该是"{data:xxxx}"
        data = json.loads(data)
        # 获取不到就返回None
        return data.get("data", None)

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

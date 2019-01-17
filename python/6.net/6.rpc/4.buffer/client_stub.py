import socket
import pickle


class ClientStub(object):
    def __init__(self, address):
        """address ==> (ip,port)"""
        self.socket = socket.socket()
        self.socket.connect(address)

    def pack(self, func, args):
        """打包：把方法和参数拼接成自定义的协议"""
        return pickle.dumps((func, args))

    def unpack(self, data):
        """解包：获取返回结果"""
        return pickle.loads(data)

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

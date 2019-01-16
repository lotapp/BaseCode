from xmlrpc.server import SimpleXMLRPCServer


def sum(a, b):
    """return a+b"""
    return a + b


# PS：50051是gRPC默认端口
server = SimpleXMLRPCServer(('', 50051))
# 把函数注册到RPC服务器中
server.register_function(sum)
print("Server启动ing，Port：50051")
server.serve_forever()
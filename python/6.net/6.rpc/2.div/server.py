import socket
from server_stub import ServerStub


class RPCServer(object):
    def __init__(self, address, mycode):
        self.mycode = mycode
        # 服务端存根（RPC Proxy）
        self.server_stub = ServerStub(mycode)
        # TCP Socket
        self.socket = socket.socket()
        # 端口复用
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定端口
        self.socket.bind(address)

    def run(self):
        self.socket.listen()
        while True:
            # 等待客户端连接
            client_socket, client_addr = self.socket.accept()
            print(f"来自{client_addr}的请求：\n")
            # 交给服务端存根（Server Proxy）处理
            self.server_stub.handle(client_socket, client_addr)


if __name__ == "__main__":
    from server_code import MyCode
    server = RPCServer(('', 50051), MyCode())
    print("Server启动ing，Port：50051")
    server.run()

from socket import socket
from socketserver import ThreadingTCPServer, BaseRequestHandler


def write_log(msg):
    print(msg.decode("utf-8"))


class MyHandler(BaseRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息：]\n")
        data = self.request.recv(2048)
        write_log(data)
        if data:
            with socket() as tcp_socket:
                tcp_socket.connect(("www.baidu.com", 80))
                # 转发请求到指定网站
                tcp_socket.send(data)
                new_data = tcp_socket.recv(2048)
                write_log(new_data)
                self.request.send(new_data)


def main():
    ThreadingTCPServer.allow_reuse_address = True
    with ThreadingTCPServer(('', 8080), MyHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()

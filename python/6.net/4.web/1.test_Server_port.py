from socket import SOL_SOCKET, SO_REUSEADDR
from socketserver import ThreadingTCPServer, BaseRequestHandler


class MyHandler(BaseRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息：]")
        data = self.request.recv(2048)
        print(data)
        self.request.send(
            "HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n<h1>小明，晚上吃鱼汤吗？</h1>"
            .encode("utf-8"))


def main():
    # bind_and_activate=False 手动绑定和激活
    with ThreadingTCPServer(('', 8080), MyHandler, False) as server:
        # 防止端口占用
        server.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server.server_bind()  # 自己绑定
        server.server_activate()  # 自己激活
        server.serve_forever()


if __name__ == "__main__":
    main()

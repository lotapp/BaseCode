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
    # 防止端口占用
    ThreadingTCPServer.allow_reuse_address = True
    with ThreadingTCPServer(('', 8080), MyHandler) as server:
        # print(server.allow_reuse_address)
        # server.allow_reuse_address = True
        server.serve_forever()


if __name__ == "__main__":
    main()

from socketserver import BaseRequestHandler, TCPServer


class MyHandler(BaseRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息:]\n")
        data = self.request.recv(2048)
        if data:
            print(data.decode("utf-8"))
        self.request.send(b'HTTP/1.1 200 ok\r\n\r\n<h1>TCP Server Test</h1>')


def main():
    with TCPServer(('', 8080), MyHandler) as server:
        server.allow_reuse_address = True  # 防止端口占用
        server.serve_forever()  # 期待服务器并执行自定义的Handler方法
        # 不启动也可以使用client_socket, client_address = server.get_request()来自定义处理


if __name__ == "__main__":
    main()

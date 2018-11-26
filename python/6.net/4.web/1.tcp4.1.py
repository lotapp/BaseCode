from socketserver import ForkingTCPServer, BaseRequestHandler


class MyHandler(BaseRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息：]\n")
        data = self.request.recv(2048)
        if data:
            print(data.decode("utf-8"))
        self.request.send(
            "HTTP/1.1 200 ok\r\n\r\n<h1>TCP Server Forking</h1>".encode("utf-8"))


if __name__ == "__main__":
    with ForkingTCPServer(('', 8080), MyHandler) as server:
        server.serve_forever()

import socketserver


# 自定义处理函数
class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(2048)
        if data:
            header, _ = data.decode("utf-8").split("\r\n", 1)
            print(header)

            self.request.send(
                """HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n<h1>This is MyServer</h1>"""
                .encode("utf-8"))
        else:
            self.request.send(b"over")


def main():
    with socketserver.ThreadingTCPServer(("", 8080), MyHandler) as server:
        server.allow_reuse_address = True  # 防止端口占用
        server.serve_forever()


if __name__ == "__main__":
    main()

from socketserver import UDPServer, BaseRequestHandler


class MyHandler(BaseRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息:]\n")
        data = self.request.recvfrom(2048)
        if data:
            print(data.decode("utf-8"))
        self.request.sendto(self.client_address, b"ok")


def main():
    with UDPServer(('', 8080), MyHandler) as server:
        # server.allow_reuse_address = True  # 防止端口占用（防止TCP四次握手迟迟不释放端口）
        server.serve_forever()


if __name__ == "__main__":
    main()

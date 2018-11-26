from socketserver import UDPServer, BaseRequestHandler


class MyHandler(BaseRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息:]\n")
        data, socket = self.request
        with socket:
            if data:
                print(data.decode("utf-8"))
            socket.sendto("行啊，小张晚上我请你吃～".encode("utf-8"), self.client_address)


def main():
    with UDPServer(('', 8080), MyHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()

from multiprocessing.dummy import threading
from socketserver import TCPServer, BaseRequestHandler


class MyHandler(BaseRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息：]\n")
        data = self.request.recv(2048)
        if data:
            print(data.decode("utf-8"))
        self.request.send(
            "HTTP/1.1 200 ok\r\n\r\n<h1>TCP Server</h1>".encode("utf-8"))


if __name__ == "__main__":
    with TCPServer(('', 8080), MyHandler) as server:
        for _ in range(10):  # 指定线程数
            t = threading.Thread(target=server.serve_forever)
            t.setDaemon(True)
            t.start()
        server.serve_forever()

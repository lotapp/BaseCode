import re
import socket


class HttpServer(object):
    def __init__(self):
        # 路由表
        self.router_urls = {"/test": "/test.py", "/user": "/test2.py"}

    def run(self):
        with socket.socket() as server:
            # 端口复用
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(("", 8080))
            server.listen()
            while True:
                self.client_socket, self.client_address = server.accept()
                print(f"[{self.client_address}已上线]")
                self.handler()

    def response(self, status, body=None):
        with self.client_socket as socket:
            header = f"HTTP/1.1 {status}\r\n\r\n"
            socket.send(header.encode("utf-8"))
            if body:
                socket.send(body)

    def __static_handler(self, name):
        try:
            with open(f"./www{name}", "rb") as fs:
                return fs.read()
        except Exception as ex:
            print(ex)
            return None

    def __dynamic_handler(self, name):
        try:
            m = __import__(name)
            return m.application().encode("utf-8")
        except Exception as ex:
            print(ex)
            return None

    def handler(self):
        data = self.client_socket.recv(2048)
        if data:
            header, _ = data.decode("utf-8").split("\r\n", 1)
            # GET /xxx HTTP/1.1
            ret = re.match("^\w+? (/[^ ]*) .+$", header)
            if ret:
                url = ret.group(1)
                print(url)  # print url log
                body = None
                # 路由有记录：动态页面
                if url in self.router_urls.keys():
                    url = self.router_urls[url]
                    # 切片提取模块名
                    body = self.__dynamic_handler(url[1:-3])
                else:  # 静态服务器
                    if url == "/":
                        url = "/index.html"
                    body = self.__static_handler(url)
                # 没有这个页面或者出错
                if body:
                    self.response("200 ok", body)
                else:
                    self.response("404 Not Found")
            else:
                # 404
                self.response("404 Not Found")
        else:
            print(f"{self.client_address}已下线")
            self.client_socket.close()


if __name__ == "__main__":
    import sys
    sys.path.insert(1, "./www/bin")
    HttpServer().run()
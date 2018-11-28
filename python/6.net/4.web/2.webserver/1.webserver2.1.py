import os
import re
import socketserver


class MyHandler(socketserver.BaseRequestHandler):
    # 处理请求
    def handle(self):
        with self.request:
            print(f"[来自{self.client_address}的消息：")
            data = self.request.recv(2048)
            if data:
                msg, _ = data.decode("utf-8").split("\r\n", 1)
                self.respose(msg)

    # 相应浏览器
    def respose(self, msg):
        # GET (/xxx.html) HTTP/1.1
        # 不匹配开头结尾也行：re.match("[^/]+(/[^ ]*).+", msg)
        filename = "/index.html"
        ret = re.match("^[^/]+(/[^ ]*).+$", msg)
        if ret:
            page = ret.group(1)  # 请求页面
            if not page == "/":
                filename = page

        # 获取本地文件
        data = self.read_file(filename)
        # 回复浏览器
        self.request.send(
            b"HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n"
        )
        self.request.send(data)

    # 获取本地文件内容
    def read_file(self, filename):
        print("请求页面:", filename)
        path = f"./root{filename}"
        # 没有这个文件就定位到404页面
        if not os.path.exists(path):
            path = "./root/404.html"
        print("本地路径:", path)
        # 读取页面并返回
        with open(path, "rb") as fs:
            return fs.read()


if __name__ == "__main__":
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(('', 8080), MyHandler) as server:
        server.serve_forever()

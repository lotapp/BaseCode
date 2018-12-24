import re
import socket
from index import WebFrame


class WSGIServer(object):
    def __init__(self):
        # 请求头
        self.env = dict()
        # 存放处理后的响应头
        self.response_headers = str()

    def run(self):
        with socket.socket() as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(("", 8080))
            server.listen()
            while True:
                self.client_socket, self.client_address = server.accept()
                self.handler()

    # 转换浏览器请求头格式
    def request_headers_handler(self, headers):
        # 过滤一下空字符串（不能过滤空列表）
        headers = list(filter(None, headers.split("\r\n")))
        # 提取 Method 和 Url
        ret = re.match("^([\w]+?) (/[^ ]*?) .+$", headers[0])
        if ret:
            self.env["method"] = ret.group(1)
            url = ret.group(2)
            print(url)
            self.env["path"] = "/index.html" if url == "/" else url
        else:
            return None
        # [['Host', ' localhost:8080'], ['Connection', ' keep-alive']...]
        array = map(lambda item: item.split(":", 1), headers[1:])
        for item in array:
            self.env[item[0].lower()] = item[1]
        # print(self.env)
        return "ok"

    # 响应客户端（吐槽一下，request和response的headers为毛格式不一样，这设计真不合理！）
    def start_response(self, status, header_list=[]):
        # 响应头
        self.response_headers = f"HTTP/1.1 {status}\r\n"
        for item in header_list:
            self.response_headers += f"{item[0]}:{item[1]}\r\n"
        # print(self.response_headers)

    # 响应浏览器
    def response(self, body):
        with self.client_socket as client:
            # 省略一系列服务器响应的headers
            self.response_headers += "server:WSGIServer\r\n\r\n"
            client.send(self.response_headers.encode("utf-8"))
            if body:
                client.send(body)

    def handler(self):
        with self.client_socket as client:
            data = client.recv(2048)
            if data:
                # 浏览器请求头
                headers = data.decode("utf-8")
                if self.request_headers_handler(headers):
                    # 模仿php所有请求都一个文件处理
                    body = WebFrame().application(self.env,
                                                  self.start_response)
                    # 响应浏览器
                    self.response(body)
                else:
                    self.start_response("404 Not Found")
            else:
                client.close()

if __name__ == "__main__":
    WSGIServer().run()
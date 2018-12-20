import re
import socket


class HTTPServer(object):
    def __init__(self):
        with socket.socket() as tcp_server:
            tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcp_server.bind(('', 8080))
            tcp_server.listen()
            while True:
                self.client_socket, self.client_address = tcp_server.accept()
                self.handle()

    def response(self, status, body=None):
        print(status)
        # response_header
        header = f"HTTP/1.1 {status}\r\n\r\n"
        with self.client_socket:
            self.client_socket.send(header.encode("utf-8"))
            if body:
                self.client_socket.send(body)

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

    def handle(self):
        with self.client_socket:
            print(f"[来自{self.client_address}的消息:]\n")
            data = self.client_socket.recv(2048)
            if data:
                header, _ = data.decode("utf-8").split("\r\n", 1)
                print(header)
                # GET /xxx HTTP/1.1
                ret = re.match("^\w+? (/[^ ]*) .+$", header)
                if ret:
                    url = ret.groups(1)[0]
                    # Python三元表达式(之前好像忘说了)
                    url = "/index.html" if url == "/" else url
                    print("请求url:", url)
                    body = str()
                    # 动态页面
                    if ".py" in url:
                        # 提取模块名(把开头的/和.py排除)
                        body = self.__dynamic_handler(url[1:-3])
                    else:  # 静态服务器
                        body = self.__static_handler(url)
                    # 根据返回的body内容，返回对应的响应码
                    if body:
                        self.response("200 ok", body)
                    else:
                        self.response("404 Not Found")
                else:  # 匹配不到url（基本上不会发生，不排除恶意修改）
                    self.response((404, "404 Not Found"))


if __name__ == "__main__":
    import sys
    # 防止 __import__ 导入模块的时候找不到，忘了可以查看：
    # https://www.cnblogs.com/dotnetcrazy/p/9253087.html#5.自己添加模块路径
    sys.path.insert(1, "./www/bin")
    HTTPServer()

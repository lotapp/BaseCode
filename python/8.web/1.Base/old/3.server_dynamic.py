import re
import socketserver


# 自定义处理函数
class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        """自定义处理方法"""
        data = self.request.recv(2048)
        if data:
            header, other = data.decode("utf-8").split("\r\n", 1)
            self.set_request_headers(other)  # 把请求头组装成字典
            # GET /xxx HTTP/1.1
            ret = re.match("[^ ]+ ([^ ]+)", header)
            if ret:
                file_name = ret.group(1)
                if file_name == "/":
                    file_name = "/index.html"  # 代表主页
            # 是否是动态页面
            if file_name.endswith(".py"):
                # .py去除掉
                self.response_body = self.__dynamic_handler(file_name[:-3])
            else:  # 静态页面
                self.response_body = self.__static_handler(file_name)
                # 根据有没有内容来设置返回的状态码
                if self.response_body:
                    self.start_response("200 ok")  # 有这个文件
                else:
                    self.response_404()  # 404页面
            # 响应浏览器
            self.response()

    # 没有变化
    def set_request_headers(self, headers):
        """设置请求头为指定格式"""
        self.request_headers = dict()
        for line in headers.splitlines():
            # 防止出现：Host:https://www.baidu.com 这种情况
            item = line.split(":", 1)  # key-value array
            if len(item) == 2:  # 最后一行是空（[:]）
                self.request_headers[item[0]] = item[1]

    # 没有变化
    def start_response(self, status, header_dict={}):
        """设置响应头"""
        self.response_headers = f"HTTP/1.1 {status}\r\n"
        for key, value in header_dict.items():
            self.response_headers += f"{key}:{value}\r\n"
        # header和body分隔的地方是两个\r\n
        self.response_headers += "Server:MyServer\r\n\r\n"

    # 没有变化
    def response(self):
        """响应浏览器"""
        self.request.send(
            self.response_headers.encode("utf-8") + self.response_body)

    # 没有变化
    def response_404(self):
        """返回404页面"""
        self.start_response("404 Not Found")  # 没有这个文件
        self.response_body = self.__static_handler("/404.html")

    # 没有变化
    def __static_handler(self, file_name):
        """返回文件内容"""
        file_name = f"./root{file_name}"
        print(file_name)
        import os
        if os.path.exists(file_name):
            # 二进制方式打开文件（图片、文本都适用）
            with open(file_name, "rb") as f:
                return f.read()
        else:
            return None

    def __dynamic_handler(self, name):
        """动态页面"""
        self.request_headers["path"] = name  # 把请求方法传递过去

        from dynamic.frame import WebFrame
        # 根据WSGI协议来
        return WebFrame().application(self.request_headers,
                                      self.start_response)


# 没有变化
def main():
    with socketserver.ThreadingTCPServer(("", 8080), MyHandler) as server:
        server.allow_reuse_address = True  # 防止端口占用
        server.serve_forever()


if __name__ == "__main__":
    main()

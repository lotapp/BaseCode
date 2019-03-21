import re
import logging
import socketserver

logger = logging.Logger(__name__)
logger.setLevel(logging.INFO)


# 自定义处理函数（框架不用修改）
class MyHandler(socketserver.BaseRequestHandler):
    def set_logging(self):
        """简单版日志记录"""
        import time
        file_name = f"{time.strftime('%Y-%m-%d',time.localtime())}.log"
        # 支持中文
        fh = logging.FileHandler(file_name, mode="a+", encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
            ))
        logger.addHandler(fh)

        # PS：不支持中文的一步到位
        # logging.basicConfig(level=logging.INFO,filename=f"{time.strftime('%Y-%m-%d',time.localtime())}.log",filemode="a+",format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

    def handle(self):
        """自定义处理方法"""
        try:
            self.set_logging()  # 日志配置相关

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
                    # 访问的页面一般都记录一下（便于找Bug）
                    logger.info(f"访问的页面为：{file_name}")  # logging.info(xx)

                # 伪静态：先看磁盘有没有html文件，如果没有就交给后端`伪造`
                self.response_body = self.__static_handler(file_name)
                # 根据有没有内容来设置返回的状态码
                if self.response_body:
                    self.start_response("200 ok")  # 有这个文件
                # 本地没有html文件就交给框架来伪静态（有404处理，不用担心）
                else:
                    # 去除.html
                    self.response_body = self.__dynamic_handler(file_name[:-5])
                # 响应浏览器
                self.response()
        except Exception as ex:
            logger.error(ex)  # logging.error(ex)

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

    # 没有变化
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

class WebFrame(object):
    def __init__(self):
        # 路由表
        self.router_urls = {"/time": "get_time", "/user": "get_name"}

    def get_time(self):
        import time
        return time.ctime().encode("utf-8")

    def get_name(self):
        return "<h2>My Name Is XiaoMing</h2>".encode("utf-8")

    def application(self, env, start_response):
        body = b""
        url = env["path"]
        # 请求的页面都映射到路由对应的方法中
        if url in self.router_urls.keys():
            func = self.router_urls[url]
            body = getattr(self, func)()
        else:
            # 否则就请求对应的静态资源
            try:
                with open(f"./www{url}", "rb") as fs:
                    body = fs.read()
            except Exception as ex:
                start_response("404 Not Found")
                print(ex)
                return b"404 Not Found"  # 出错就直接返回了
        # 返回对应的页面响应头
        start_response("200 ok", [("Content-Type", "text/html"),
                                  ("Scripts", "Python")])
        return body
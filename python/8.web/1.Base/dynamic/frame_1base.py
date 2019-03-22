class WebFrame(object):
    def get_time(self):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S",
                             time.localtime()).encode("utf-8")

    route_dict = {"/time": get_time}

    def application(self, env, start_response):
        """约定的方法入口"""
        # 根据路由查找对应的动态方法
        func = self.route_dict.get(env["path"])
        if func:
            start_response("200 ok",
                           {"Content-Type": "text/html;charset=UTF-8"})
            return func(self)
        else:
            start_response("404 Not Found",
                           {"Content-Type": "text/html;charset=UTF-8"})
            return b"404 Not Found"


def main():
    result = WebFrame().get_time()
    print(result)


if __name__ == "__main__":
    main()

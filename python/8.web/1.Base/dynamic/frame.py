import re
import functools

# 自动化路由的好处就来了，任意加函数，只有使用路由装饰器就能一一对应


# add match
class Route(object):
    """提取一个路由类"""
    route_dict = {}  # 路由表
    match_dict = {}  # 开启正则的路由字典（是路由表的子集）

    def __init__(self, url, match=False):
        self.url = url  # /time
        self.match = match  # 是否开启正则

    def __call__(self, func):
        # 把映射关系添加到路由中
        self.route_dict[self.url] = func

        # 把开启正则的路由单独列出来
        if self.match:
            self.match_dict[self.url] = func

        # 复制原方法的签名
        @functools.wraps(func)
        def inner(frame_self):  # frame_self是WebFrame的self
            return func(frame_self)  # 返回执行结果

        return inner


# frame V3：正则版路由
class WebFrame(object):
    # 没有变化
    @Route("/time")
    def get_time(self):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S",
                             time.localtime()).encode("utf-8")

    @Route(r"/info/(\d+)", True)
    def get_info(self, id):
        return f"<h2>Info For {id}</h2>".encode("utf-8")

    # add：正则匹配
    def application(self, env, start_response):
        """约定的方法入口"""
        url = env["path"]

        # 尽量减少正则匹配的次数（PS：子集比全集匹配次数更少）
        for pattern, func in Route.match_dict.items():
            ret = re.match(pattern, url)
            if ret:
                start_response("200 ok",
                               {"Content-Type": "text/html;charset=UTF-8"})
                return func(self, ret.group(1))

        # 没匹配到，那就和之前一样的流程：根据路由查找对应的动态方法
        func = Route.route_dict.get(url)
        if func:
            start_response("200 ok",
                           {"Content-Type": "text/html;charset=UTF-8"})
            return func(self)
        else:
            start_response("404 Not Found",
                           {"Content-Type": "text/html;charset=UTF-8"})
            return b"404 Not Found"


# 没有变化
def main():
    # 摸拟一个请求（忽略后面顺便摸拟的lambda表达式）
    frame = WebFrame()
    result = frame.application({"path": "/time"}, lambda x, y: x)
    print(result)

    result = frame.application({"path": "/info"}, lambda x, y: x)
    print(result)


if __name__ == "__main__":
    main()

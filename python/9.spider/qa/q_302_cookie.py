import urllib
import http.cookiejar

# 请求头
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}


# 登录并保存状态
def login_save():
    # 请求url
    url = "http://www.biquge.cm/login.php"
    # 表单数据
    data = urllib.parse.urlencode({
        "username": "dnt",
        "password": "dnt",
        "action": "login"
    }).encode("utf-8")
    # 返回构造的request
    request = urllib.request.Request(
        url, headers=headers, data=data, method="POST")
    # 实例化cookie对象
    cookie = http.cookiejar.LWPCookieJar("cookie.log")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)

    # 遍历看看cookie
    for item in cookie:
        print(f"{item.name}：{item.value}")

    # 需要被丢弃的cookie和过期的cookie也保存
    cookie.save(ignore_discard=True, ignore_expires=True)
    return True


def main():
    if login_save():
        # 实例化cookie对象
        cookie = http.cookiejar.LWPCookieJar()
        # 加载登录后的cookie状态
        cookie.load("cookie.log")

        # 遍历看看cookie
        for item in cookie:
            print(f"{item.name}：{item.value}")

        # 构建cookie处理器
        handler = urllib.request.HTTPCookieProcessor(cookie)
        # 获取openner对象
        opener = urllib.request.build_opener(handler)
        # 构造request对象
        # 书架（登录后才能查看）
        url = "http://www.biquge.cm/modules/article/bookcase.php"  # 有一个302跳转
        request = urllib.request.Request(url, headers=headers)
        # 发送请求
        response = opener.open(request)
        print(response.read().decode("gbk"))
    else:
        print("登录失败")


if __name__ == "__main__":
    main()

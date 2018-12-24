def application(env, start_response):
    # 设置动态页面的响应头（回头服务器会再加上自己的响应头）
    # 列表里面的 item 是 tuple
    start_response("200 OK", [("Content-Type", "text/html")])
    # 返回一个列表
    return ["<h1>This is Test!</h1>".encode("utf-8")]
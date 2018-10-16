def actor():
    while True:
        try:
            msg = yield  # 获取消息
            print(msg, end="")
        except RuntimeError:
            print('Actor退出')


p = actor()
next(p)  # 准备接收
p.send("你好～")
p.send("小明")
p.close()

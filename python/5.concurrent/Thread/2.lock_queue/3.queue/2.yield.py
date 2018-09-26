def consumer():
    status = ""
    while True:
        tmp = yield status
        if not tmp:
            print("消费者已经睡觉了...")
            return
        print("消费者：获得商品%s号..." % tmp)
        status = "ok"


def produce(c):
    # 启动消费者
    c.send(None)
    for i in range(1, 3):
        print("生产者：出产商品%s号..." % i)
        # 生产商品，并提交给消费者
        status = c.send(i)
        print("生产者：生产者消费状态: %s" % status)
    # c.send(None) 执行这个会引发StopIteration
    c.close()  # 使用close就可以避免了(手动关闭生成器函数，后面的调用会直接返回StopIteration异常)


if __name__ == '__main__':
    # 创建消费者
    c = consumer()
    produce(c)

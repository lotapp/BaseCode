from multiprocessing import Queue


def main():
    q = Queue(3)  # 只能 put 3条消息
    q.put([1, 2, 3, 4])  # put一个List类型的消息
    q.put({"a": 1, "b": 2})  # put一个Dict类型的消息
    q.put({1, 2, 3, 4})  # put一个Set类型的消息

    try:
        # 不加timeout，就一直阻塞，等消息队列有空位才能发出去
        q.put("再加条消息呗", timeout=2)
    # Full(Exception)是空实现，你可以直接用Exception
    except Exception:
        print("消息队列已满，队列数%s，当前存在%s条消息" % (q._maxsize, q.qsize()))

    try:
        # 非阻塞，不能put就抛异常
        q.put_nowait("再加条消息呗")  # 相当于q.put(obj,False)
    except Exception:
        print("消息队列已满，队列数%s，当前存在%s条消息" % (q._maxsize, q.qsize()))

    while not q.empty():
        print(
            "队列数：%s，当前存在%s条消息 内容%s" % (q._maxsize, q.qsize(), q.get_nowait()))

    print("队列数：%s，当前存在：%s条消息" % (q._maxsize, q.qsize()))


if __name__ == '__main__':
    main()

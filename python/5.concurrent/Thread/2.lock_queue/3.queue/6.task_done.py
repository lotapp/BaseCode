from multiprocessing.dummy import threading, Queue


def consumer(queue):
    while 1:
        data = queue.get()
        print(f"[消费者]消费商品{data}号")
        # 通知Queue完成任务了
        queue.task_done()


def producer(queue):
    for i in range(10):
        print(f"[生产者]生产商品{i}号")
        queue.put(i)


def main():
    queue = Queue()
    # 开启生产消费者线程任务
    t_list = [
        threading.Thread(target=func, args=(queue, ))
        for func in (producer, consumer)
    ]
    # 启动两个线程
    for t in t_list:
        t.setDaemon(True)  # 设置后台线程，就算是死循环当主线程退出的时候也会退出的
        t.start()
    # 等待所有任务完成
    queue.join()  # 你可以把这句话注释掉看输出
    print(f"当前队列未完成的数量：{queue.unfinished_tasks}")


if __name__ == '__main__':
    main()

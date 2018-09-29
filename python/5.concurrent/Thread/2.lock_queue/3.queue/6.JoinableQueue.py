from time import sleep
from multiprocessing import Process, JoinableQueue


def consumer(queue):
    while 1:
        if queue.empty():
            break  # 没数据就退出
        data = queue.get()
        print(f"[消费者]消费商品{data}号")
        # 通知Queue完成任务了
        queue.task_done()
        sleep(0.1)


def producer(queue):
    for i in range(10):
        print(f"[生产者]生产商品{i}号")
        queue.put(i)


def main():
    queue = JoinableQueue()
    # 开启生产消费者进程任务
    t_list = [
        Process(target=func, args=(queue, )) for func in (producer, consumer)
    ]
    # 启动两个进程
    for t in t_list:
        # t.daemon = True
        t.start()

    # 主进程回收子进程（你可以把这段换成queue.join试试坑）
    for t in t_list:
        t.join()


if __name__ == '__main__':
    main()

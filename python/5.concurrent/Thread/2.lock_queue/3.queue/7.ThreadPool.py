from os import cpu_count
from multiprocessing.dummy import threading, Process, Queue


class Task(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        print("开启一个线程～")

    def run(self):
        func, args, kws = self.queue.get()
        print(args, kws)
        func(args, kws)
        self.queue.task_done()


class ThreadPool(object):
    def __init__(self, count=0):
        # 设置Pool运行状态
        self.running = True

        # 默认是CPU核数，且至少有一个线程
        if count <= 0:
            count = cpu_count() or 1
        # 设置线程数
        self.queue = Queue(count)
        
        # 启动对应个数的线程
        for _ in range(count):
            Task(self.queue).start()

    def apply(self, func, args=(), kws={}):
        if self.running:
            # 执行任务
            self.queue.put((func, args, kws))

    def close(self):
        # 不再运行加入任务
        self.running = False

    def join(self):
        # 等待任务执行完退出
        self.queue.join()


def call_dad(*args, **kws):
    print(f"{args}~{kws}")


def main():
    pool = ThreadPool()
    pool.apply(call_dad, args=(1, 2, 3), kws={"dad": "小明"})
    pool.apply(call_dad, args=(1, 2, 3), kws={"dad": "小张"})
    pool.join()


if __name__ == '__main__':
    main()

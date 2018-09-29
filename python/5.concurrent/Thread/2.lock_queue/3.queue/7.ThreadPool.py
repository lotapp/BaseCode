from multiprocessing.dummy import threading, Queue


class Task(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

        self.setDaemon(True)  # 设置后台线程，主线程结束就终止
        self.start()  # 开启线程，执行run方法
        print(f"开启一个线程～{self.name}")

    def run(self):
        func, args, kws = self.queue.get()
        try:
            func(args, kws)
        except Exception as ex:
            print(ex)
        finally:
            self.queue.task_done()


class ThreadPool(object):
    def __init__(self, count=0):
        # 设置Pool运行状态
        self.running = True

        from os import cpu_count  # 用到的时候导入对应模块即可
        # 默认是CPU核数，且至少有一个线程
        if count <= 0:
            count = cpu_count() or 1
        # 设置线程数
        self.queue = Queue(count)

        # 启动对应个数的线程
        for _ in range(count):
            Task(self.queue)  # 不能在这直接启动，会阻塞Pool的

    def apply_async(self, func, args=(), kws={}):
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
    from time import sleep
    from random import randint
    n = randint(1, 2)  # [1,2]
    print(f"休息{n}s")
    sleep(n)
    print(f"{args}~{kws}")


def main():
    pool = ThreadPool()
    pool.apply_async(call_dad, args=(1, 2, 3), kws={"dad": "小明"})
    pool.apply_async(call_dad, args=(1, 2, 3), kws={"dad": "小张"})
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

from time import sleep
from contextlib import contextmanager  # 引入上下文管理器
from multiprocessing.dummy import threading


@contextmanager
def lock_manager(*args):
    # 先排个序（按照id排序）
    args = sorted(args, key=lambda x: id(x))

    try:
        # 依次加锁
        for lock in args:
            lock.acquire()
        yield
    finally:
        # 先释放最后加的锁（倒序释放）
        for lock in reversed(args):
            lock.release()


def eat(l_lock, r_lock):
    while True:
        with lock_manager(l_lock, r_lock):
            print(f"{threading.current_thread().name}，正在吃面")
            sleep(0.01)


def main():
    resource = 5  # 5个筷子，5个哲学家
    locks = [threading.Lock() for i in range(resource)]  # 几个资源几个锁

    # 抢左手筷子（locks[i]）和右手的筷子（locks[(i + 1) % resource]）
    # 举个例子更清楚：i=0 ==> 0,1；i=4 ==> 4,0
    tasks = [
        threading.Thread(
            target=eat, args=(locks[i], locks[(i + 1) % resource]))
        for i in range(resource)
    ]
    for t in tasks:
        t.start()
    for t in tasks:
        t.join()


if __name__ == '__main__':
    main()

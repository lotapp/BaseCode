from contextlib import contextmanager
from multiprocessing.dummy import threading, Pool as ThreadPool

# ThreadLocal
_local = threading.local()


@contextmanager
def acquire(*args):
    # 以id将锁进行排序
    args = sorted(args, key=lambda x: id(x))

    # 确保不违反以前获取的锁顺序
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(args[0]):
        raise RuntimeError('锁顺序有问题')

    # 获取所有锁
    acquired.extend(args)
    _local.acquired = acquired  # ThreadLocal：每个线程独享acquired

    # 固定格式
    try:
        for lock in args:
            lock.acquire()
        yield
    finally:
        # 逆向释放锁资源
        for lock in reversed(args):
            lock.release()
        # 把释放掉的锁给删了
        del acquired[-len(args):]


# ############### test ########################

x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


def main():
    p = ThreadPool()
    p.apply_async(thread_1)
    p.apply_async(thread_2)
    p.close()
    p.join()


if __name__ == '__main__':
    main()

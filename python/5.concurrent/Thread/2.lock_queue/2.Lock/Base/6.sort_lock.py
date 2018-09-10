from contextlib import contextmanager  # 引入上下文管理器
from multiprocessing.dummy import Pool as ThreadPool, Lock


@contextmanager
def lock_manager(*args):
    # 先排个序（按照id排序）
    args = sorted(args, key=lambda x: id(x))

    try:
        for lock in args:
            lock.acquire()
        yield
    finally:
        # 先释放最后加的锁（倒序释放）
        for lock in reversed(args):
            lock.release()


xiaoming = 5000
xiaozhang = 8000
m_lock = Lock()  # 小明的锁
z_lock = Lock()  # 小张的锁


# 小明转账1000给小张
def a_to_b():
    global xiaoming
    global xiaozhang
    global m_lock
    global z_lock
    print(f"[转账前]小明{xiaoming},小张{xiaozhang}")
    with lock_manager(m_lock, z_lock):
        xiaoming -= 1000
        xiaozhang += 1000
    print(f"[转账后]小明{xiaoming},小张{xiaozhang}")


# 小张转账1000给小明
def b_to_a():
    global xiaoming
    global xiaozhang
    global m_lock
    global z_lock
    print(f"[转账前]小明{xiaoming},小张{xiaozhang}")
    with lock_manager(m_lock, z_lock):
        xiaozhang -= 1000
        xiaoming += 1000
    print(f"[转账后]小明{xiaoming},小张{xiaozhang}")


def main():
    print(f"[互刷之前]小明{xiaoming},小张{xiaozhang}")
    p = ThreadPool()
    for _ in range(5):
        p.apply_async(a_to_b)
        p.apply_async(b_to_a)
    p.close()
    p.join()
    print(f"[互刷之后]小明{xiaoming},小张{xiaozhang}")


if __name__ == '__main__':
    main()

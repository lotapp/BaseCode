from time import sleep
from multiprocessing.dummy import Pool as ThreadPool, Lock

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
    # 以上次代码为例，这边只修改了这块
    with z_lock:  # 小张权重高，大家都先获取小张的锁
        xiaozhang += 1000
        sleep(0.01)
        with m_lock:
            xiaoming -= 1000


# 小张转账1000给小明
def b_to_a():
    global xiaoming
    global xiaozhang
    global m_lock
    global z_lock
    with z_lock:
        xiaozhang -= 1000
        sleep(0.01)
        with m_lock:
            xiaoming += 1000


def main():
    print(f"[转账前]小明{xiaoming},小张{xiaozhang}")
    p = ThreadPool()
    p.apply_async(a_to_b)
    p.apply_async(b_to_a)
    p.close()
    p.join()
    print(f"[转账后]小明{xiaoming},小张{xiaozhang}")


if __name__ == '__main__':
    main()

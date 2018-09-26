import time
import random
from multiprocessing.dummy import Pool as ThreadPool, Queue


def consumer(q, i):
    while True:
        data = q.get()
        print(f"[消费者{i}]商品{data}抢光了")


def producer(q):
    while True:
        num = random.random()
        q.put(num)
        print(f"[生产者]商品{num}出厂了\n")
        time.sleep(num)


def main():
    q = Queue(10)  # 为了演示，我这边限制一下
    pool = ThreadPool()
    # 一个生产者
    pool.apply_async(producer, args=(q,))
    # 两个消费者
    pool.apply_async(consumer, args=(q, 1))
    pool.apply_async(consumer, args=(q, 2))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

import time, random, uuid
from multiprocessing.dummy import Pool as ThreadPool, Queue

stop_obj = uuid.uuid1() # 获取UUID（GUID）


def consumer(q, i):
    while True:
        data = q.get()
        if data == stop_obj:
            print(f"[消费者{i}]光荣退伍了")
            q.put(data)  # 如果不加这个，其他消费者就不知道了（Queue里面的数据取出来就没了）
            break
        print(f"[消费者{i}]商品{data}抢光了")


def producer(q):
    for i in range(10):
        num = random.random()
        q.put(num)
        print(f"[生产者]商品{num}出厂了\n")
        time.sleep(num)
    q.put(stop_obj)  # 发送结束命令


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

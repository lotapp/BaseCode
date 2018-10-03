from time import sleep
from random import random
from multiprocessing.dummy import Pool as ThreadPool, Event

global_list = []
event = Event()
stop_event = Event()

n = 0


def consumer(i):
    print(f"消费者{i}等待ing")
    while 1:
        event.wait()
        count = len(global_list)
        # 防止List空的时候pop出错
        if count > 0:
            print(f"消费了产品{global_list.pop()}")
            event.clear()  # 重置状态（加这一句能减少很多次循环）
        # 防止生产者结束了，但是消费者还没处理完成
        elif len(global_list) == 0 and stop_event.is_set():
            break
        global n
        n += 1
    print(f"消费者{i}完成任务～总共循环{n}次")


def producer():
    print("生产者正在生产商品")
    for i in range(10):
        global_list.append(i)
        sleep(random())  # 模拟网络延迟
        event.set()  # 通知消费者生产结束
    stop_event.set()  # 通知消费者已经可以结束线程了


def main():
    pool = ThreadPool()
    pool.map_async(consumer, range(2))  # 两个消费者
    pool.apply_async(producer)  #
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
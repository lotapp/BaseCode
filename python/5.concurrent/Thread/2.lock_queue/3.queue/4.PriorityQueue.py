from uuid import uuid1
from queue import PriorityQueue
from multiprocessing.dummy import Pool as ThreadPool

stop_obj = uuid1()  # 获取UUID（GUID）


def task_put(queue):
    queue.put((-5, "小周"))
    queue.put((-7, "小潘"))
    queue.put((-3, "小明"))
    queue.put((-9, "小张"))
    global stop_obj
    # 可以思考一下为什么用0，如果按照小到大的顺序又该如何设置呢？
    queue.put((0, stop_obj))


def task_get(queue):
    global stop_obj
    # 全部读出来
    while 1:
        data = queue.get()
        if data[-1] == stop_obj:
            print("光荣退伍了")
            queue.put((0, stop_obj))  # 保证其他消费者也能安全退出
            break
        print(data[-1])


def error_print(msg):
    print(msg)


if __name__ == '__main__':
    queue = PriorityQueue()
    pool = ThreadPool()
    pool.apply_async(task_get, args=(queue, ), error_callback=error_print)
    pool.apply_async(task_put, args=(queue, ), error_callback=error_print)
    pool.close()
    pool.join()

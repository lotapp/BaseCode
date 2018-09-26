import heapq
from uuid import uuid1
from multiprocessing.dummy import Pool as ThreadPool, Condition


class MaxPriorityQueue(object):
    """自定义一个最大优先队列"""

    def __init__(self):
        self.__h_list = []
        self.__con = Condition()  # 条件变量
        self.__index = 0  # 索引

    def put(self, value, sort=0):
        with self.__con:
            # heapq是最小二叉堆，优先级取负就是最大二叉堆了
            heapq.heappush(self.__h_list, (-sort, self.__index, value))
            self.__index += 1
            self.__con.notify()  # 随机通知一个阻塞等的线程

    def get(self):
        with self.__con:
            while 1:
                # 0 => False
                if not self.qsize():
                    self.__con.wait()  # 列表为空则阻塞等
                return heapq.heappop(self.__h_list)[-1]  # 返回元组最后一个元素（value）

    def qsize(self):
        return len(self.__h_list)


stop_obj = uuid1()  # 获取UUID（GUID）


def task_put(queue):
    queue.put("小周", 5)
    queue.put("小潘", 7)
    queue.put("小明", 3)
    queue.put("小张", 9)
    global stop_obj
    queue.put(stop_obj)


def task_get(queue):
    global stop_obj
    # 全部读出来
    while 1:
        data = queue.get()
        if data == stop_obj:
            print("光荣退伍了")
            queue.put(stop_obj)  # 保证其他消费者也能安全退出
            break
        print(data)


if __name__ == '__main__':
    queue = MaxPriorityQueue()
    pool = ThreadPool()
    pool.apply_async(task_get, args=(queue,))
    pool.apply_async(task_put, args=(queue,))
    pool.close()
    pool.join()

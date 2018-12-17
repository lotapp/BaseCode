from contextlib import contextmanager
from collections import defaultdict


class Exchange(object):
    # 定义一个订阅者集合
    def __init__(self):
        self.__subscribers = set()

    # 定义一个附加任务的方法
    def attach(self, task):
        self.__subscribers.add(task)

    # 定义一个分离任务的方法
    def detach(self, task):
        self.__subscribers.remove(task)

    # 知识回顾：http://www.cnblogs.com/dotnetcrazy/p/9528315.html#锁专题扩展
    @contextmanager
    def subscribe(self, *tasks):
        # 防止用户忘记解绑任务
        for task in tasks:
            self.attach(task)
        # 不要放在循环内（容易出错）
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    # 批量调用订阅者们的send方法
    def send(self, msg):
        for subscribe in self.__subscribers:
            subscribe.send(msg)


exchange_dict = defaultdict(Exchange)


def get_exchange(key):
    return exchange_dict[key]


# 定义一个Task
class BaseTask(object):
    def send(self, msg):
        print(msg)


# 比如获取一个key是shop的交换机
exc = get_exchange("shop")

# 然后把任务1和2添加到交换机内
task1 = BaseTask()
task2 = BaseTask()

with exc.subscribe(task1, task2):
    exc.send("test")
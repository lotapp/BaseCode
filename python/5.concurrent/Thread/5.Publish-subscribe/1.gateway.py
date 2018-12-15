from collections import defaultdict  # dict的子类


# 交换机（发布者）
class Exchange(object):
    def __init__(self):
        # 订阅者集合
        self.__subscribers = set()

    # 添加一个Task到订阅者集合中
    def attach(self, task):
        self.__subscribers.add(task)

    # 把Task从订阅者集合中移除
    def detach(self, task):
        self.__subscribers.remove(task)

    def send(self, msg):
        for subscriber in self.__subscribers:
            subscriber.send(msg)


exchange_dict = defaultdict(Exchange)
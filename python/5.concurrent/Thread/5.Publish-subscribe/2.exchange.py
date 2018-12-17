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
            # 调用订阅者里面的send方法
            subscriber.send(msg)


exchange_dict = defaultdict(Exchange)


def get_exchange(key):
    return exchange_dict[key]

# 交换机上的订阅者
class PrintMessages:
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print(f"msg[{self.count}]: {msg}")


exc = get_exchange('shop')
exc.attach(PrintMessages())


# 定义一个Task
class BaseTask(object):
    def send(self, msg):
        print(msg)


# 比如获取一个key是shop的交换机
exc = get_exchange("shop")

# 然后把任务1和2添加到交换机内（模拟其他PC的订阅者）
task1 = BaseTask()
task2 = BaseTask()
exc.attach(task1)
exc.attach(task2)  # 分离使用：detach

# 这时候要是群发消息就简单了：
exc.send("test")

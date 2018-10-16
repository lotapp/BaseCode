from BaseActor import BaseActor
from multiprocessing.dummy import Event


class TaskResult(object):
    def __init__(self):
        self.__event = Event()
        self.__result = None

    def result(self):
        # 阻塞等结果
        self.__event.wait()
        return self.__result

    def set_result(self, value):
        self.__result = value
        self.__event.set()  # 标记执行完毕


class ActorTask(BaseActor):
    def apply_async(self, func, *args, **kwagrs):
        self.r = TaskResult()
        self.send((func, args, kwagrs))
        return self.r

    def run(self):
        func, args, kvargs = self.recv()
        # 执行指定方法并return返回值
        value = func(*args, **kvargs)
        self.r.set_result(value)


def test_add(a, b):
    return a + b


actor = ActorTask()
actor.start()
task = actor.apply_async(test_add, 1, 2)
print(task.result())
actor.close()
actor.join()

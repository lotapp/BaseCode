from multiprocessing.dummy import threading, Queue, Event


class ActorExit(Exception):
    """用来标记Actor退出（特殊的哨兵值）"""
    pass


class BaseActor(object):
    def __init__(self):
        """queue：Actor内部的邮箱队列"""
        self.__mailbox = Queue()

    def recv(self):
        """Actor接受消息"""
        msg = self.__mailbox.get()
        if msg is ActorExit:
            # 抛出异常（模版方法会处理）
            raise ActorExit
        return msg

    def send(self, msg):
        """Actor发送消息"""
        self.__mailbox.put(msg)

    def close(self):
        """发送结束标识"""
        self.send(ActorExit)

    def start(self):
        self.__terminated_event = Event()  # 为Join服务
        t = threading.Thread(target=self.__templet)
        t.setDaemon(True)  # 设置为守护线程
        t.start()

    def __templet(self):
        """模版方法（run会被子类重写）"""
        try:
            self.run()  # 执行Run代码
        except ActorExit:
            pass  # 防止线程挂掉
        finally:
            # 设置Event标识
            self.__terminated_event.set()

    def join(self):
        # Event在set之后便结束等待
        self.__terminated_event.wait()

    def run(self):
        """
        由子类实现即可，eg：
        while True:
            msg = self.recv()
            print(msg)
        """
        pass


class TestActor(BaseActor):
    def run(self):
        while True:
            msg = self.recv()
            print(msg)


if __name__ == '__main__':
    p = TestActor()
    p.start()
    p.send('Hello')
    p.send('World')
    p.close()
    p.join()

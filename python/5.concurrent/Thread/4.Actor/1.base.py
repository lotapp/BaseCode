from multiprocessing.dummy import Queue


class Actor(object):
    def __init__(self):
        # Actor内部的消息缓存队列
        self.__mailbox = Queue()

    def send(self, msg):
        self.__mailbox.put(msg)

    def recv(self):
        return self.__mailbox.get()


if __name__ == '__main__':
    xiaoming = Actor()
    xiaoming.send("存款")
    msg = xiaoming.recv()
    print(msg)

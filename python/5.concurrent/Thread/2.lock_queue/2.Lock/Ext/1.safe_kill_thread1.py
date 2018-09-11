from time import sleep
from multiprocessing.dummy import threading


class ShutdownTask(object):
    def __init__(self):
        self.__running = True

    def terminate(self):
        self.__running = False

    def run(self):
        # 轮询方式必须根据业务来，不然没有意义
        while self.__running:
            print("do something")
            sleep(2)


def main():
    task = ShutdownTask()
    t = threading.Thread(target=task.run)
    t.start()
    task.terminate()  # 结束线程
    t.join()
    print("over")


if __name__ == '__main__':
    main()

from time import sleep
from multiprocessing.dummy import threading


class MyThread(threading.Thread):
    def __init__(self):
        self.__running = True
        super().__init__()

    def terminate(self):
        self.__running = False

    def run(self):
        # 轮询方式必须根据业务来，不然没有意义
        while self.__running:
            print("do something")
            sleep(2)


def main():
    t = MyThread()
    t.start()
    t.terminate()
    t.join()
    # t.join(timeout=1)  # 超时时间
    print("over")


if __name__ == '__main__':
    main()

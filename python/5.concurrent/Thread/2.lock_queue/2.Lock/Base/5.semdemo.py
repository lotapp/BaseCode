import time
from multiprocessing.dummy import threading, Semaphore


class MyThread(threading.Thread):
    def __init__(self, id, sem):
        super().__init__()
        self.__id = id
        self.__sem = sem

    def run(self):
        self.__sem.acquire()  # 获取
        self.api_test()

    def api_test(self):
        """模拟api请求"""
        time.sleep(1)
        print(f"id={self.__id}")
        self.__sem.release()  # 释放


def main():
    sem = Semaphore(10)  # 控制并发数
    t_list = [MyThread(i, sem) for i in range(1000)]
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()


if __name__ == '__main__':
    main()

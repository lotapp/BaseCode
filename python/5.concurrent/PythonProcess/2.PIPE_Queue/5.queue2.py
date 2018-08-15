import os
import time
from multiprocessing import Process, Queue


def pro_test1(q):
    print("[子进程1]PPID=%d,PID=%d,GID=%d" % (os.getppid(), os.getpid(),
                                           os.getgid()))
    q.put("[子进程1]小明，今晚撸串不？")

    # 设置一个简版的重试机制（三次重试）
    for i in range(3):
        if not q.empty():
            print(q.get())
            break
        else:
            time.sleep((i + 1) * 2)  # 第一次1s，第二次4s，第三次6s


def pro_test2(q):
    print("[子进程2]PPID=%d,PID=%d,GID=%d" % (os.getppid(), os.getpid(),
                                           os.getgid()))
    print(q.get())
    time.sleep(4)  # 模拟一下网络延迟
    q.put("[子进程2]不去，我今天约了妹子")


def main():
    queue = Queue()
    p1 = Process(target=pro_test1, args=(queue, ))
    p2 = Process(target=pro_test2, args=(queue, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
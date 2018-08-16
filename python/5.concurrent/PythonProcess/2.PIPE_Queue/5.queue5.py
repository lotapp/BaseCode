import os
import time
from multiprocessing import Pool, Queue


def error_callback(msg):
    print(msg)


def pro_test1():
    print("[子进程1]PPID=%d,PID=%d" % (os.getppid(), os.getpid()))
    q.put("[子进程1]小明，今晚撸串不？")

    # 设置一个简版的重试机制（三次重试）
    for i in range(3):
        if not q.empty():
            print(q.get())
            break
        else:
            time.sleep((i + 1) * 2)  # 第一次1s，第二次4s，第三次6s


def pro_test2():
    print("[子进程2]PPID=%d,PID=%d" % (os.getppid(), os.getpid()))
    print(q.get())
    time.sleep(4)  # 模拟一下网络延迟
    q.put("[子进程2]不去，我今天约了妹子")


def init(queue):
    global q
    q = queue


def main():
    print("[父进程]PPID=%d,PID=%d" % (os.getppid(), os.getpid()))
    queue = Queue()
    p = Pool(initializer=init, initargs=(queue, ))
    p.apply_async(pro_test1, error_callback=error_callback)
    p.apply_async(pro_test2, error_callback=error_callback)
    p.close()
    p.join()


if __name__ == '__main__':
    main()
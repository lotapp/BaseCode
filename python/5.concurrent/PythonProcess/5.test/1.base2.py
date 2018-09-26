import os
from time import sleep
from multiprocessing import Process


def test(i):
    print(f"[{i}]PID:{os.getpid()},PPID:{os.getppid()}")
    sleep(1)


def main():
    p_list = [Process(target=test, args=(i, )) for i in range(10)]
    for p in p_list:
        p.start()
    for p in p_list:
        p.join()
        print(f"[子进程{p.pid}]正常退出")


if __name__ == '__main__':
    main()

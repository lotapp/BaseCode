import os
# 注意一下，导入的是Process不是process（Class是大写开头）
from multiprocessing import Process


def test(name):
    print("[子进程-%s]PID：%d，PPID：%d" % (name, os.getpid(), os.getppid()))


def main():
    print("[父进程]PID：%d，PPID：%d" % (os.getpid(), os.getppid()))
    p = Process(target=test, args=("萌萌哒", ))
    p.start()
    p.join()  # 父进程回收子进程资源（内部调用了wait系列方法）


if __name__ == '__main__':
    main()
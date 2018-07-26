import os
import time


def main():
    pid = os.fork()
    if pid == 0:
        print("子进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
        while 1:
            print("孩子老卵，就是不听话")
            time.sleep(3)
    elif pid > 0:
        print("父进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
        wpid, status = os.wait()  # 调用一次只能回收一次，想都回收，就来个while循环，-1则退出
        print(wpid)
        print(status)
        if status == 0:
            print("正常退出")
        elif status == 9:
            print("被信号9干死了")

    print("pid=%d,over" % os.getpid())


if __name__ == '__main__':
    main()

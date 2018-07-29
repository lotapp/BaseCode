import os
import time
import signal


def main():
    # 不受进程影响，每个进程只能有一个定时器，再设置只是重置
    signal.alarm(3)  # 设置终止时间（3s），然后终止进程（sigaltirm）

    pid = os.fork()
    if pid == 0:
        print("[子进程]PID=%d,PPID=%d" % (os.getpid(), os.getppid()))
        for i in range(5):
            print("[子进程]孩子老卵，怎么滴吧～")
            time.sleep(1)
    elif pid > 0:
        print("[父进程]PID=%d,PPID=%d" % (os.getpid(), os.getppid()))

    print("[遗言]PID=%d,PPID=%d" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    main()
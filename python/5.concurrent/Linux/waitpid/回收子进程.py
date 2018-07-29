import os
import time


def main():
    pid = os.fork()

    if pid == 0:
        print("[子进程]PID：%d，PPID：%d" % (os.getpid(), os.getppid()))
        time.sleep(2)

    elif pid > 0:
        print("[父进程]PID：%d，PPID：%d" % (os.getpid(), os.getppid()))
        while True:
            try:
                wpid, status = os.waitpid(-1, os.WNOHANG)
                if wpid > 0:
                    print("回收子进程wpid:%d,状态status:%d" % (wpid, status))
            except OSError:
                print("没有子进程了")
                break

            print("父进程忙着挣钱养家呢～")
            time.sleep(3)

    print("[over]PID：%d，PPID：%d" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    main()
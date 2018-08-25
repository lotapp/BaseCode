import os
import time


def main():
    pid = os.fork()
    if pid == 0:
        print("子进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)  # 睡1s
    elif pid > 0:
        print("父进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))

    print("pid=%d,over" % os.getpid())


if __name__ == '__main__':
    main()

# 父进程：Pid=15918,PPID=8345
# pid=15918,over
# 子进程：Pid=15921,PPID=15918

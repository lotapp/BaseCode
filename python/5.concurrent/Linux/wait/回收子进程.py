import os
import time


def main():
    pid = os.fork()
    if pid == 0:
        print("子进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
    elif pid > 0:
        print("父进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
        wpid, status = os.wait()
        print(wpid)
        print(status)

    print("pid=%d,over" % os.getpid())


if __name__ == '__main__':
    main()

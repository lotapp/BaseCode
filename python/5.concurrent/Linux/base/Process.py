import os


def main():
    print("准备测试～PID：%d" % os.getpid())
    pid = os.fork()
    if pid == 0:
        print("子进程：PID：%d,PPID：%d" % (os.getpid(), os.getppid()))
    elif pid > 0:
        print("父进程：PID：%d,PPID：%d" % (os.getpid(), os.getppid()))
    print("PID:%d,我是卖报的小行家，大风大雨都不怕" % os.getpid())


if __name__ == '__main__':
    main()

import os
import time


def main():
    pid = os.fork()
    if pid == 0:
        print("子进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
    elif pid > 0:
        print("父进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
        while 1:
            print("父亲我忙着呢，没时间管你个小屁孩")
            time.sleep(3)

    print("pid=%d,over" % os.getpid())


if __name__ == '__main__':
    main()

# 父进程：Pid=16297,PPID=10369
# 父亲我忙着呢，没时间管你个小屁孩
# 子进程：Pid=16298,PPID=16297
# pid=16298,over
# 父亲我忙着呢，没时间管你个小屁孩
# 父亲我忙着呢，没时间管你个小屁孩
# 父亲我忙着呢，没时间管你个小屁孩
# ...
# kill -9 xxx 杀不死子进程，因为孩子已经死了（可以把父亲杀死，这样就被系统干爹领养处理调了）
import os


def main():
    num = 100
    pid = os.fork()
    # 子进程
    if pid == 0:
        num += 10
    elif pid > 0:
        num += 20

    print("PID:%d，PPID：%d，Num=%d" % (os.getpid(), os.getppid(), num))


if __name__ == '__main__':
    main()
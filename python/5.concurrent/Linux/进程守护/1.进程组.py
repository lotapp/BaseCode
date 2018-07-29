import os
import time


def main():
    pid = os.fork()
    if pid == 0:
        for i in range(7):
            print("子进程：PID=%d,PPID=%d,PGrpID=%d" % (os.getpid(), os.getppid(),
                                                    os.getpgrp()))
            time.sleep(i)
    elif pid > 0:
        print("父进程：PID=%d,PPID=%d,PGrpID=%d" % (os.getpid(), os.getppid(),
                                                os.getpgrp()))
        time.sleep(4)

    print("遗言：PID=%d,PPID=%d,PGrpID=%d" % (os.getpid(), os.getppid(),
                                           os.getpgrp()))


if __name__ == '__main__':
    main()
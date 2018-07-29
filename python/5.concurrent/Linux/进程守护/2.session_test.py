import os


def main():
    pid = os.getpid()
    print("进程：PPID=%d,PID=%d,GID=%d,SID=%d" % (pid, os.getppid(), os.getpgrp(),
                                               os.getsid(pid)))
    os.setsid()


if __name__ == '__main__':
    main()
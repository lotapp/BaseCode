import os
import time


def main():
    i = 0
    while i < 3:
        pid = os.fork()
        # 防止产生孙子进程（可以自己思索下）
        if pid == 0:
            break
        i += 1

    if i == 0:
        print("i=%d,子进程：Pid=%d,PPID=%d" % (i, os.getpid(), os.getppid()))
        time.sleep(1)
    elif i == 1:
        print("i=%d,子进程：Pid=%d,PPID=%d" % (i, os.getpid(), os.getppid()))
        time.sleep(1)
    elif i == 2:
        print("i=%d,子进程：Pid=%d,PPID=%d" % (i, os.getpid(), os.getppid()))
        time.sleep(3)
        while 1:
            print("(PID=%d)我又老卵了，怎么滴～" % os.getpid())
            time.sleep(3)
    elif i == 3:  # 循环结束后，父进程才会退出，这时候i=3
        print("i=%d,父进程：Pid=%d,PPID=%d" % (i, os.getpid(), os.getppid()))
        while True:
            print("等待回收子进程")
            try:
                wpid, status = os.wait()
                print(wpid)
                print(status)
                if status == 0:
                    print("正常退出")
                elif status == 9:
                    print("被信号9干死了")
            except OSError as ex:
                print(ex)
                break

    print("pid=%d,over，ppid=%d" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    main()

import os
import time


def main():
    pid = os.fork()

    if pid > 0:
        print("父进程(pid=%d)开始写入：" % os.getpid())
        with open(str(pid), "w") as f:
            f.write("[父进程写入]从前有座山,山上有座庙,庙里有个老和尚和一个小和尚。有一天,老和尚对小和尚说:\n")
        time.sleep(2)
        print("父进程(pid=%d)开始读取：" % os.getpid())
        with open(str(pid), "r") as f:
            print(f.read())

        wpid, status = os.wait()  # 收尸
        print("pid=%d已经回收,status:%d" % (wpid, status))

    elif pid == 0:
        print("子进程(pid=%d)开始读取：" % os.getpid())
        with open(str(os.getpid()), "r") as f:
            print(f.read())
        print("子进程(pid=%d)开始追加：" % os.getpid())
        with open(str(os.getpid()), "a") as f:  # 追加
            f.write("[子进程追加]从前有座山,山上有座庙,庙里有个老和尚和一个小和尚。有一天,老和尚对小和尚说:\n")

    print("\n进程(pid=%d)完蛋了" % os.getpid())


if __name__ == '__main__':
    main()

import os
import time


def main():
    print("[PID:%d]进程运行中..." % os.getpid())
    time.sleep(5)
    os.abort()  # 给自己发异常终止信号


if __name__ == '__main__':
    main()

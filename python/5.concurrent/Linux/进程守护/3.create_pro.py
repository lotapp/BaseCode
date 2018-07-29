import os
import time
from sys import stdin, stdout, stderr


def main():

    # 【必须】1. fork子进程，父进程退出（子进程变成了孤儿）
    pid = os.fork()
    if pid > 0:
        exit(0)

    # 【必须】2. 子进程创建新会话（创建出新会话会丢弃原有的控制终端）
    os.setsid()

    # 3. 改变当前工作目录【为了减少bug】# 改成不会被删掉的目录，比如/
    os.chdir("/home/dnt")  # 我这边因为是用户创建的守护进程，就放它下面，用户删了，它也没必要存在了

    # 4. 重置文件掩码（获取777权限）
    os.umask(0)

    # 5. 关闭文件描述符（如果写日志就重定向一下）
    os.close(stdin.fileno())
    os.close(stdout.fileno())
    os.close(stderr.fileno())

    # 【必须】6. 自己的逻辑代码
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
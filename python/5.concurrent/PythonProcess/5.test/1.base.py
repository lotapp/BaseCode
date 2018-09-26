import os
from time import sleep


def main():
    i = 0

    # 创建子进程
    while i < 10:
        pid = os.fork()
        if pid == 0:
            break  # 防止产生孙子进程
        i += 1

    # 主进程回收子进程，循环结束后父进程才会退出，这时i=10
    if i == 10:
        while True:
            try:
                wpid, status = os.wait()
                if status == 0:
                    print(f"[子进程{wpid}]正常退出")
            except OSError as ex:
                print(ex)
                break
    else:
        print(f"[{i}]PID:{os.getpid()},PPID:{os.getppid()}")
        sleep(1)


if __name__ == '__main__':
    main()

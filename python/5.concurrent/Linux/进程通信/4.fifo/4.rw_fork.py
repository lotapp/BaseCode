import os


def main():
    file_name = "fifo_test"
    if not os.path.exists(file_name):
        os.mkfifo(file_name)

    fd = os.open(file_name, os.O_RDWR)  # 读写方式打开文件描述符 （O_RDONLY | O_WRONLY）

    pid = os.fork()
    if pid == 0:
        print("子进程：PID:%d，PPID:%d" % (os.getpid(), os.getppid()))

        os.write(fd, "子进程说：老爸，我想出去玩".encode())  # 写
        msg = os.read(fd, 1024).decode()  # 读
        print("[子进程]%s" % msg)
    elif pid > 0:
        print("父进程：PID:%d，PPID:%d" % (os.getpid(), os.getppid()))

        msg = os.read(fd, 1024).decode()  # 阻塞方式，不用担心
        print("[父进程]%s" % msg)
        os.write(fd, "父进程说：去吧乖儿子".encode())

        # 给子进程收尸
        wpid, status = os.wait()
        print("父进程收尸：子进程PID=%d，PPID=%d" % (wpid, status))

    print("进程遗言：PID=%d，PPID=%d" % (os.getpid(), os.getppid()))  # 剩下的代码段


if __name__ == '__main__':
    main()

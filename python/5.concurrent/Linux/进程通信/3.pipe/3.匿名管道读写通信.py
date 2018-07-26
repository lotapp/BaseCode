import os


def close_fd(*fd_tuple_args):
    """关闭fd，fd_tuple_args是可变参数"""
    for item in fd_tuple_args:
        os.close(item[0])
        os.close(item[1])


def main():
    # 管道是单向的，相互读写，那就创建两个管道
    fd_tuple1 = os.pipe()  # 进程1写，进程2读
    fd_tuple2 = os.pipe()  # 进程2写，进程1读

    i = 0
    while (i < 2):
        pid = os.fork()
        if pid == 0:
            break
        i += 1
    # 子进程1
    if i == 0:
        print("[子进程]pid：%d，ppid：%d" % (os.getpid(), os.getppid()))

        os.close(fd_tuple1[0])  # 进程1写，则关闭下读端
        msg_str = "进程1说：兄弟，今天撸串吗？"
        os.write(fd_tuple1[1], msg_str.encode())  # 把字符串xxx转换成bytes

        # 不读的我关闭掉：
        os.close(fd_tuple2[1])  # 进程2写，我不需要写，关闭写端
        bts = os.read(fd_tuple2[0], 1024)
        print("[子进程1]", bts.decode())

        exit(0)  # 退出后就不执行下面代码块语句了
    # 子进程2
    elif i == 1:
        print("[子进程2]pid：%d，ppid：%d" % (os.getpid(), os.getppid()))

        os.close(fd_tuple1[1])  # 进程2读，则关闭下写端
        bts = os.read(fd_tuple1[0], 1024)
        print("[子进程2]", bts.decode())

        # 不读的我关闭掉：
        os.close(fd_tuple2[0])  # 进程2写，关闭读端
        msg_str = "进程2说：可以可以～"
        os.write(fd_tuple2[1], msg_str.encode())  # 把字符串xxx转换成bytes

        exit()  # 不加参数默认是None
    # 父进程
    elif i == 2:
        print("[父进程]pid：%d，ppid：%d" % (os.getpid(), os.getppid()))

        # 父进程不读不写，就看看
        close_fd(fd_tuple1, fd_tuple2)

        # 收尸ing
        while True:
            try:
                wpid, status = os.wait()
                print("[父进程～收尸]子进程PID：%d 的状态status：%d" % (wpid, status))
            except OSError:
                break
    # 子进程都exit()退出了，不会执行这句话了
    print("[父进程遗言]pid：%d,ppid：%d" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    main()

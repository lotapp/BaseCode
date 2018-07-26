import os
import sys
import time


def main():

    read_fd, write_fd = os.pipe()  # 可以思考为啥在上面创建管道（提示.text代码段都一样）

    i = 0
    while i < 2:
        pid = os.fork()
        # 防止子进程生猴子
        if pid == 0:
            break
        i += 1

    # 子进程1
    if i == 0:
        print("[子进程%d]pid=%d，ppid=%d" % (i, os.getpid(), os.getppid()))

        # 准备重定向到写端，所以先关了读端
        os.close(read_fd)
        os.dup2(write_fd, sys.stdout.fileno())  # STDOUT_FILENO == 1 (文件描述符输出，写端)

        # 僵桃李代
        os.execlp("ps", "ps", "-aux")
        # 僵桃李代后，.text代码段都被替换了，自然不会执行
        print("我是不会执行的，不信你看呗")
    elif i == 1:
        print("[子进程%d]pid=%d，ppid=%d" % (i, os.getpid(), os.getppid()))

        # 准备重定向到读端，所以先关了写端
        os.close(write_fd)
        os.dup2(read_fd, sys.stdin.fileno())  # STDIN_FILENO == 0 (文件描述符输入，读端)

        # 僵桃李代  ”bash“是查找关键词，你写你想找的字符串即可
        os.execlp("grep", "grep", "bash", "--color=auto")

        # 僵桃李代后，.text代码段都被替换了，自然不会执行
        print("我是不会执行的，不信你看呗")
    elif i == 2:
        print("[父进程]pid=%d，ppid=%d" % (os.getpid(), os.getppid()))

        # 我不写不读
        os.close(read_fd)
        os.close(write_fd)

        # 为了大家熟练掌握wait系列，这次用waitpid
        while (True):
            info = ()
            try:
                info = os.waitpid(-1, os.WNOHANG)  # 非阻塞的方式回收所有子进程
            except OSError:
                break  # waitpid返回-1的时候，Python会抛出异常

            if info[0] > 0:
                print("父进程收尸成功：pid=%d，ppid=%d，状态status：%d" %
                      (os.getpid(), os.getppid(), info[1]))
            print("父进程做其他事情...")
            time.sleep(0.005)  # 休息 0.005s

    print("[父进程-遗言]pid=%d，ppid=%d" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    main()

import os
import sys


def main():
    # 创建内核缓存区（伪文件）
    read_fd, write_fd = os.pipe()
    print("read_fd:%s\nwrite_fd:%s" % (read_fd, write_fd))

    pid = os.fork()
    if pid > 0:
        print("[父进程]pid=%d,ppid=%d" % (os.getpid(), os.getppid()))

        # 写或者读，则需要关闭另一端（防止自己写自己读）
        os.close(read_fd)
        # dup2(oldfd,newfd) 把写端数据重定向到文件描述符输出端
        os.dup2(write_fd, sys.stdout.fileno())  # STDOUT_FILENO==1 (文件描述符输出，写端)
        # 僵桃李代
        os.execlp("ps", "ps", "aux")

    elif pid == 0:
        print("[子进程]pid=%d,ppid=%d" % (os.getpid(), os.getppid()))

        # 子进程现在需要读，关闭写段
        os.close(write_fd)
        # dup2(oldfd,newfd) 把读端数据重定向到文件描述符输入端
        os.dup2(read_fd, sys.stdin.fileno())  # STDOUT_FILENO == 0 (文件描述符输入，读端)
        # 僵桃李代 （默认是从终端读，重定向后从内核缓冲区读）
        os.execlp("grep", "grep", "python", "--color=auto")


if __name__ == '__main__':
    main()
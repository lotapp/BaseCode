import os
import time


def main():
    r_fd, w_fd = os.pipe2(os.O_NONBLOCK | os.O_CLOEXEC)

    pid = os.fork()
    if pid == 0:
        print("子进程：pid=%d，ppid=%d" % (os.getpid(), os.getppid()))
        time.sleep(0.5)

        # 和父进程进行通信
        os.close(r_fd)
        os.write(w_fd, "老爸，我出去玩了～".encode())

        exit(0)  # 子进程退出
    elif pid > 0:
        print("父进程：pid=%d，ppid=%d" % (os.getpid(), os.getppid()))

        # 读儿子的留言
        os.close(w_fd)
        b_msg = b""
        while True:
            try:
                b_msg = os.read(r_fd, 1)  # 没有数据就出错（一般都是等待一会，也可以和信号联合使用）
            except OSError:
                print("儿子怎么没有留言呢？")

            print("父进程：做其他事情...")
            if len(b_msg) > 0:
                break
            time.sleep(0.1)

        # 继续读剩下的消息
        b_msg += os.read(r_fd, 1024)
        print("儿子留言:", b_msg.decode())

        wpid, status = os.wait()
        print("帮儿子做扫尾工作：pid=%d，status=%d" % (wpid, status))

    print("父进程遗言：pid=%d，status=%d" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    main()

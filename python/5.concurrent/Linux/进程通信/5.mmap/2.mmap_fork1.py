import os
import time
import mmap


def create_file(file_name, size):
    with open(file_name, "wb") as f:
        f.seek(size - 1)
        f.write(b"\0x00")


def main():
    file_name = "temp.bin"
    # mmap映射的时候不能映射空文件，所以我们自己创建一个
    create_file(file_name, 1024)

    fd = os.open(file_name, os.O_RDWR)
    with mmap.mmap(fd, 0) as m:  # m.resize(1024) # 大小可以自己调整的
        pid = os.fork()
        if pid == 0:
            print("[子进程]PID:%d，PPID:%d" % (os.getpid(), os.getppid()))
            m.write("子进程说：老爸，我想出去玩了～\n".encode())
            time.sleep(3)
            print(m.readline().decode().strip())
            exit(0)
        elif pid > 0:
            print("[父进程]PID:%d，PPID:%d" % (os.getpid(), os.getppid()))
            time.sleep(1)  # 和文件一样，非堵塞
            print(m.readline().decode().strip())
            m.write("父进程说：去吧去吧\n".encode())
            wpid, status = os.wait()
            print("[父进程]收尸：PID:%d，Status:%d" % (wpid, status))
            exit(0)


if __name__ == '__main__':
    main()

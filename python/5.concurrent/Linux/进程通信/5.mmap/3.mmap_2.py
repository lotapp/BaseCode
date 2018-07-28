import os
import time
import mmap


def create_file(file_name, size):
    with open(file_name, "wb") as f:
        f.seek(size - 1)
        f.write(b"\0x00")


def main():
    file_name = "temp.bin"

    if not os.path.exists(file_name):
        # mmap映射的时候不能映射空文件，所以我们自己创建一个
        create_file(file_name, 1024)

    fd = os.open(file_name, os.O_RDWR)
    with mmap.mmap(fd, 0) as m:  # m.resize(1024) # 大小可以自己调整的
        print("[进程2]PID:%d，PPID:%d" % (os.getpid(), os.getppid()))
        time.sleep(1)
        print(m.readline().decode().strip())
        m.write("进程2说：为毛不去？\n".encode())
        exit(0)


if __name__ == '__main__':
    main()

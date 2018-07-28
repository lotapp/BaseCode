import os
import time


def main():
    file_name = "fifo_temp"
    if not os.path.exists(file_name):
        os.mkfifo(file_name)

    fd = os.open(file_name, os.O_RDWR)  # 你输入os.O_rw就会有这个选项了，不用硬记
    os.write(fd, "小潘，撸串去不?".encode())

    time.sleep(3)  # 防止自己写的被自己读了

    msg = os.read(fd, 1024).decode()  # 阻塞的方式，不用担心
    print("[进程1]]%s" % msg)


if __name__ == '__main__':
    main()

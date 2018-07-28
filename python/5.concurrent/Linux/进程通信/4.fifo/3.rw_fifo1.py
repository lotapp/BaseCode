import os


def main():
    file_name = "fifo_temp"
    if not os.path.exists(file_name):
        os.mkfifo(file_name)

    fd = os.open(file_name, os.O_RDWR)  # 你输入os.O_rw就会有这个选项了，不用硬记
    msg = os.read(fd, 1024).decode()  # 阻塞的方式，不用担心
    print("[进程2]%s" % msg)
    os.write(fd, "小明啊，你忘记你长几斤肉了?".encode())


if __name__ == '__main__':
    main()

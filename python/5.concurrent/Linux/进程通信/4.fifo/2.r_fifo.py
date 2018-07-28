import os


def main():
    file_name = "fifo_file"
    if not os.path.exists(file_name):
        os.mkfifo(file_name)

    fd = os.open(file_name, os.O_RDONLY)  # 只读（阻塞）
    while True:
        b_msg = os.read(fd, 1024)
        if len(b_msg) > 0:
            print(b_msg.decode())


if __name__ == '__main__':
    main()

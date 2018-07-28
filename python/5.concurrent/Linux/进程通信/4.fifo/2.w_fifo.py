import os
import time


def main():
    file_name = "fifo_file"
    if not os.path.exists(file_name):
        os.mkfifo(file_name)

    fd = os.open(file_name, os.O_WRONLY)  # 只写
    while True:
        time.sleep(1)  # 模拟一下实际生产环境下的 读快写慢
        try:
            os.write(fd, "我是说话有魔性，喝水会长胖的小明同学".encode())  # 写入bytes
        except BrokenPipeError:
            print("如果读端全部关闭，管道破裂，进程自动被终止")
            break


if __name__ == '__main__':
    main()

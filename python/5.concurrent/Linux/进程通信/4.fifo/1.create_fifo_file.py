import os
import time


def main():
    # 文件路径都可以这么判断
    if not os.path.exists("fifo_test"):
        os.mkfifo("fifo_test")  # 创建fifo管道文件
        print("文件fifo_test不存在，已经创建成功")


if __name__ == '__main__':
    main()
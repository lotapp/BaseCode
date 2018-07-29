import os
import mmap


def main():
    with open("temp.bin", "wb") as f:
        f.write("小明同学最爱刷碗\n小潘同学最爱打扫".encode())

    # 打开磁盘二进制文件进行更新（读写）
    with open("temp.bin", "r+b") as f:
        with mmap.mmap(f.fileno(), 0) as m:
            print("postion_index:%d" % m.tell())
            print(m.readline().decode().strip())  # 转成str并去除两端空格
            print("postion_index:%d" % m.tell())
            print(m[:].decode())  # 全部读出来
            print("postion_index:%d" % m.tell())
            m.seek(0)
            print("postion_index:%d" % m.tell())


if __name__ == '__main__':
    main()
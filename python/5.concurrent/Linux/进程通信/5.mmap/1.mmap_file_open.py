import os
import mmap


def main():
    with open("temp", "wb") as f:
        f.write("小明同学最爱刷碗\n小潘同学最爱打扫".encode())

    with open("temp", "r+b") as f:
        with mmap.mmap(f.fileno(), 0) as m:
            print("postion_index:%d" % m.tell())
            print(m.readline().decode())
            print("postion_index:%d" % m.tell())
            print(m[:].decode())  # 全部读出来
            # print(m[5:m.size()].decode())
            print("postion_index:%d" % m.tell())


if __name__ == '__main__':
    main()
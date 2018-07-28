import os
import mmap


def create_file(filename, size):
    """初始化一个文件，并把文件扩充到指定大小"""
    with open(filename, "w") as f:
        f.seek(size - 1)  # 改变流的位置
        f.write("\0")  # 在末尾写个`\0`，如果是wb二进制写入，就写入"\x00"


def main():
    create_file("mmap_file", 4096)  # 创建一个4k的文件
    with mmap.mmap(os.open("mmap_file", os.O_RDWR), 0) as m:  # 创建映射
        print(m.size())  # 查看文件大小
        m.resize(1024)  # 重新设置文件大小
        print(len(m))  # len也一样查看文件大小
        print(m.readline().decode())  # 读取一行，bytes转成str
        print(m.tell())  # 返回 m 对应文件的当前位置
        m.seek(0)  # 修改Postion位置
        print(m.tell())  # 返回 m 对应文件的当前位置
        print(m[0:10])  # 支持切片操作
        print("postion_index:%d" % m.tell())
        m[0:10] = b"1234567890"  # 赋值
        print("postion_index:%d" % m.tell())
        print(m[0:10])  # 取值
        print("postion_index:%d" % m.tell())
        print(m[:].decode())  # 全部读出来


if __name__ == '__main__':
    main()

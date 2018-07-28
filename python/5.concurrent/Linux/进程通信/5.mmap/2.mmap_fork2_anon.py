import os
import time
import mmap


def main():
    # 不记录文件中，直接内存中读写
    m = mmap.mmap(-1, 0)

    m.close()


if __name__ == '__main__':
    main()
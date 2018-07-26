import os


def main():
    try:
        # 创建内核缓存区（伪文件）
        read_fd, write_fd = os.pipe()
        print("read_fd:%s\nwrite_fd:%s" % (read_fd, write_fd))
    except OSError as ex:
        print(ex)


if __name__ == '__main__':
    main()
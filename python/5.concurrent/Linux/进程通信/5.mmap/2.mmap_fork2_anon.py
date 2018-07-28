import os
import time
import mmap


def main():
    # 不记录文件中，直接内存中读写（这个地方len就不能为0了，自己指定一个大小eg：4k）
    with mmap.mmap(-1, 4096) as m:
        pid = os.fork()
        if pid == 0:
            print("[子进程]PID:%d，PPID:%d" % (os.getpid(), os.getppid()))
            m.write("[子进程]老爸我出去嗨了～\n".encode())
            time.sleep(2)
            msg = m.readline().decode().strip()
            print(msg)
            exit(0)
        elif pid > 0:
            print("[父进程]PID:%d，PPID:%d" % (os.getpid(), os.getppid()))
            time.sleep(1)
            msg = m.readline().decode().strip()
            print(msg)
            m.write("[父进程]去吧，皮卡丘～".encode())

            wpid, status = os.wait()
            print("[父进程]收尸：PID:%d，Status:%d" % (wpid, status))
            exit(0)


if __name__ == '__main__':
    main()
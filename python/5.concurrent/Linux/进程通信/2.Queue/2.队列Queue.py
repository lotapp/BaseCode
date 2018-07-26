import os
from multiprocessing import Queue


def main():
    q = Queue(1)  # 创建一个容量为1的队列（只能put接受1条）
    pid = os.fork()
    if pid == 0:
        print("[子进程]:pid:%d,ppid:%d" % (os.getpid(), os.getppid()))
        q.put("父亲大人，我可以出去玩吗？")
        output = q.get()
        print("[子进程]收到父亲大人回复：%s" % output)
    elif pid > 0:
        print("[父进程]:pid:%d,ppid:%d" % (os.getppid(), os.getppid()))
        output = q.get()  # 儿子每天出去都会说，等待ing
        print("[父进程]收到儿子的话：%s" % output)
        q.put("准了")

        wpid, status = os.wait()
        print("[父进程]帮pid:%d收尸，状态：%d" % (wpid, status))

    print("[OVER]:pid:%d,ppid:%d" % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    main()
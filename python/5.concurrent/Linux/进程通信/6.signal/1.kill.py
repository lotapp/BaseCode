import os
import time
import signal


def main():
    pid = os.fork()
    if pid == 0:
        print("[子进程]PID=%d,PPID=%d" % (os.getpid(), os.getppid()))
        while True:
            print("[子进程]孩子老卵，怎么滴吧～")
            time.sleep(1)
    elif pid > 0:
        print("[父进程]PID=%d,PPID=%d" % (os.getpid(), os.getppid()))
        time.sleep(3)
        print("父进程耐心有限，准备杀了儿子")

        # sigkill 相当于kill 9 pid
        os.kill(pid, signal.SIGKILL)  # 发信号

        # 收尸
        wpid, status = os.wait()
        print("父进程收尸：子进程PID=%d,Status=%d" % (wpid, status))


if __name__ == '__main__':
    main()
# signal.pthread_kill(thread_id,signal.SIGKILL))  # 杀死线程

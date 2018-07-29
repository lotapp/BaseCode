import os
import time
import signal


def print_info(signalnum, frame):
    print("信号:%d准备弄我,我是小强我怕谁?(%s)" % (signalnum, frame))


def main():
    signal.signal(signal.SIGINT, print_info)  # 处理Ctrl+C的终止命令(singint)
    signal.signal(signal.SIGQUIT, signal.SIG_IGN)  # 忽略Ctrl+\的终止命令(sigquit)

    while True:
        print("[PID:%d]我很坚强,不退出,等着信号来递达~" % os.getpid())
        time.sleep(3)  # 你要保证进程不会退出才能处理信号,不用担心影响信号（优先级高）


if __name__ == '__main__':
    main()
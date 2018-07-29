import signal


def print_info(signalnum, frame):
    print("死前留言：我被信号%d弄死了，记得替我报仇啊！" % signalnum)


def main():
    signal.signal(signal.SIGINT, print_info)  # 处理Ctrl+C的终止命令(singint)
    signal.signal(signal.SIGQUIT, print_info)  # 处理Ctrl+\的终止命令(singquit)
    signal.siginterrupt(signal.SIGINT, False)
    signal.siginterrupt(signal.SIGQUIT, False)
    signal.pause()  # 设置一个进程到休眠状态直到接收一个信号


if __name__ == '__main__':
    main()
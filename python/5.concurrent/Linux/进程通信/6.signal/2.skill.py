import signal


def main():
    signal.alarm(1)  # 设置终止时间（3s），然后终止进程（sigaltirm）
    i = 0
    while True:
        print(i)
        i += 1  # 别忘记，Python里面没有++哦～


if __name__ == '__main__':
    main()

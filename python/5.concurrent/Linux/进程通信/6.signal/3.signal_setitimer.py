import time
import signal


def say_hai(signalnum, frame):
    print("我会周期性执行哦～")


def main():
    # 捕捉信号（在定时器前后都没事）
    signal.signal(signal.SIGALRM, say_hai)
    # 设置定时器，第一次1s后执行，以后都3s执行一次
    signal.setitimer(signal.ITIMER_REAL, 1, 3)
    # print(signal.getitimer(signal.ITIMER_REAL))

    while True:
        print("我在做其他事情")
        time.sleep(1)


if __name__ == '__main__':
    main()

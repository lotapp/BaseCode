from time import sleep
from threading import Timer


def test(obj):
    print(f"timer开始执行~ {obj}")
    sleep(1)
    print(f"timer执行完毕~ {obj}")


def main():
    t = Timer(2, test, args=("mmd", ))
    t.start()
    # t.join()  # 加这句，主线程就会等待timer执行完毕后退出
    # t.cancel()  # 停止timer
    print("主线程over")


if __name__ == '__main__':
    main()

from time import sleep
from signal import signal, SIGTERM
from multiprocessing import Process


# 可以释放锁、记录日记之类的操作
def save_data(signalnum, frame):
    print(f"[退出前处理]signalnum:{signalnum},frame:{frame}")
    exit(0)


def test():
    # 信号处理
    signal(SIGTERM, save_data)
    print("subProcess start")
    sleep(2)
    print("subProcess over")


def main():
    p = Process(target=test)
    p.start()
    sleep(1)
    p.terminate()  # 进程结束
    p.join()
    print("mainProcess over")


if __name__ == '__main__':
    main()

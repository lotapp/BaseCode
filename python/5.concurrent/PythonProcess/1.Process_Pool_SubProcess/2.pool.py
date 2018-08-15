import os
import time
from multiprocessing import Pool  # 首字母大写


def test(name):
    print("[子进程-%s]PID=%d，PPID=%d" % (name, os.getpid(), os.getppid()))
    time.sleep(1)


def main():
    print("[父进程]PID=%d，PPID=%d" % (os.getpid(), os.getppid()))
    p = Pool(5)  # 设置最多5个进程（不设置就是CPU核数）
    for i in range(10):
        # 异步执行
        p.apply_async(test, args=(i, ))  # 同步用apply（如非必要不建议用）
    p.close()  # 关闭池，不再加入新任务
    p.join()  # 等待所有子进程执行完毕回收资源
    print("over")


if __name__ == '__main__':
    main()
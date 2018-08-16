import time
import random
from multiprocessing import Pool, Manager


def write_info(msg):
    time.sleep(random.randint(1, 3))
    with open("info.log", "a+") as f:
        f.write(msg)


def main():
    pool = Pool()
    lock = Manager().Lock()
    pool.apply_async(write_info, args=("进程1：兄弟，今晚撸串吗？\n", ))
    pool.apply_async(write_info, args=("进程2：兄弟，今晚撸串吗？\n", ))
    pool.apply_async(write_info, args=("进程3：走一个～\n", ))
    pool.apply_async(write_info, args=("进程4：走一个～\n", ))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

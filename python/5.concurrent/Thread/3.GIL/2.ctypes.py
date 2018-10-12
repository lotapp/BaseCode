# from ctypes import CDLL
from ctypes import cdll
from os import cpu_count
from multiprocessing.dummy import Pool


def main():
    # 加载C共享库
    # lib = CDLL("./libtest.so")
    # lib = cdll.LoadLibrary("./libtest.so")
    lib = cdll.LoadLibrary("./libtestgo.so")

    pool = Pool()  # 默认是系统核数
    pool.map_async(lib.test, range(cpu_count()))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

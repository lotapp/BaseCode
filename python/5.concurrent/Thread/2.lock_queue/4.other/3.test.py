from time import sleep
from random import random
from multiprocessing.dummy import Pool as ThreadPool


def get_data(id):
    print(f"正在请求API，ID={id}")
    sleep(random())
    return f"{id}-Data"


def save_data(data):
    print(f"保存数据：{data}")


def main():
    pool = ThreadPool()
    # 每一个执行完毕后处理
    for i in range(10):
        pool.apply_async(get_data, args=(i, ), callback=save_data)
    # 全部执行完毕后执行save_data
    # pool.map_async(get_data, range(10), callback=save_data)
    # pool.apply_async(save_data,)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
import time
from multiprocessing import Pool


def test(x):
    return x * x


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        task = pool.apply_async(test, (10, ))
        print(task.get(timeout=1))

        obj_list = pool.map(test, range(10))
        print(obj_list)
        # 返回一个可迭代的类
        obj_iter = pool.imap(test, range(10))
        print(obj_iter)
        next(obj_iter)
        for i in obj_iter:
            print(i, end=" ")

import time
from multiprocessing import Pool


def test(x):
    """开平方"""
    time.sleep(1)
    return x * x


def main():
    pool = Pool()
    task = pool.apply_async(test, (10, ))
    print(task)
    try:
        print(task.get(timeout=1))
    except Exception:
        print("超时了～")


if __name__ == '__main__':
    main()
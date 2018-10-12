from os import cpu_count
from multiprocessing.dummy import Pool


def test(i):
    print(f"线程{i}开始死循环～")
    while True:
        pass


def main():
    pool = Pool(5)
    pool.map_async(test, range(5))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

from multiprocessing.dummy import Pool as ThreadPool

num = 0  # def global num


def test(i):
    print(f"子进程：{i}")
    global num
    for i in range(100000):
        num += 1


def main():
    p = ThreadPool()
    p.map_async(test, list(range(5)))
    p.close()
    p.join()

    print(num)  # 应该是500000，发生了数据混乱，结果少了很多


if __name__ == '__main__':
    main()

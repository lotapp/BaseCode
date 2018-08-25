from multiprocessing.dummy import Pool as ThreadPool, Lock

num = 0  # def global num
lock = Lock()


def test(i):
    print(f"子进程：{i}")
    global num
    global lock
    for i in range(100000):
        with lock:
            num += 1


def main():
    p = ThreadPool()
    p.map_async(test, list(range(5)))
    p.close()
    p.join()

    print(num)


if __name__ == '__main__':
    main()

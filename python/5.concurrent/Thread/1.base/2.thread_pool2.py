from multiprocessing.dummy import Pool as ThreadPool, current_process


def test(i):
    # 源码：current_process = threading.current_thread
    print(f"[编号{i}]{current_process().name}")


def main():
    p = ThreadPool()
    p.map_async(test, list(range(5)))
    p.close()
    p.join()

    print(f"{current_process().name}")


if __name__ == '__main__':
    main()

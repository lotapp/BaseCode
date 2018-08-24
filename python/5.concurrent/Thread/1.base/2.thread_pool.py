from multiprocessing.dummy import Pool as ThreadPool, current_process


def test(i):
    # 本质调用了：threading.current_thread
    print(f"[编号{i}]{current_process().name}")


def main():
    p = ThreadPool()
    for i in range(5):
        p.apply_async(test, args=(i, ))
    p.close()
    p.join()

    print(f"{current_process().name}")


if __name__ == '__main__':
    main()
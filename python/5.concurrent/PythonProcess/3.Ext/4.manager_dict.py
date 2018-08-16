from multiprocessing import Manager, Process, Lock


def test(dict1, lock):
    for i in range(100):
        with lock:  # 你可以把这句话注释掉，然后就知道为什么加了
            dict1["year"] += 1


def main():
    with Manager() as m:
        lock = Lock()
        dict1 = m.dict({"year": 2000})
        p_list = [Process(target=test, args=(dict1, lock)) for i in range(5)]
        for i in p_list:
            i.start()
        for i in p_list:
            i.join()
        print(dict1)


if __name__ == '__main__':
    main()

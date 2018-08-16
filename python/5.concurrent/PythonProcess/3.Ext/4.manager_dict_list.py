from multiprocessing import Pool, Manager


def test1(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


def test2(d, l):
    print(d)
    print(l)


def main():
    with Manager() as manager:
        dict_test = manager.dict()
        list_test = manager.list(range(10))

        pool = Pool()
        pool.apply_async(test1, args=(dict_test, list_test))
        pool.apply_async(test2, args=(dict_test, list_test))
        pool.close()
        pool.join()


if __name__ == '__main__':
    main()

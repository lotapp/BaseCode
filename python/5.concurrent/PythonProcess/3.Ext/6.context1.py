import multiprocessing as mp


def foo(q):
    q.put('hello')


if __name__ == '__main__':
    mp.set_start_method('spawn')  # 不要过多使用
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q, ))
    p.start()
    print(q.get())
    p.join()
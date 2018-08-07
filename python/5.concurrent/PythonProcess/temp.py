import time
import random
from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import wait


def foo(w):
    for i in range(10):
        w.send((i, current_process().name))
    w.close()


if __name__ == '__main__':
    readers = []

    for i in range(4):
        r, w = Pipe(duplex=False)
        readers.append(r)  # 给父进程
        p = Process(target=foo, args=(w, ))
        p.start()
        w.close()

    while readers:
        for r in wait(readers):
            try:
                msg = r.recv()
            except EOFError:
                readers.remove(r)
            else:
                print(msg)
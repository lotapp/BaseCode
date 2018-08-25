from time import sleep
from multiprocessing.dummy import Pool as ThreadPool, BoundedSemaphore

sem = BoundedSemaphore(5)


def goto_wc(i):
    global sem
    with sem:
        print(f"[线程{i}]上厕所")
        sleep(0.1)


def main():
    p = ThreadPool()
    p.map_async(goto_wc, range(50))
    p.close()
    p.join()


if __name__ == '__main__':
    main()
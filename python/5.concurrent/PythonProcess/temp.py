import logging
from multiprocessing import Pool, Manager


def write_log(lock, items):
    # Do cool stuff
    lock.acquire()

    # Write to stdout or logfile, etc.
    lock.release()


def main():
    pool = Pool()
    lock = Manager().Lock()
    pool.map(write_log, [1, 2, 3, 4, 5])
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
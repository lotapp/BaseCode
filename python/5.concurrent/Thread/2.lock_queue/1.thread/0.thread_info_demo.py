from time import sleep
from multiprocessing.dummy import threading


def main():
    t = threading.Thread(target=sleep, args=(100, ))
    t.start()
    t.join()
    print("over")


if __name__ == '__main__':
    main()
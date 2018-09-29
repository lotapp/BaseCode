from time import sleep
# from multiprocessing import Process
from multiprocessing.dummy import threading  # Process


def test(i):
    sleep(1)
    print(i)


def main():
    # t_list = [Process(target=test, args=(i, )) for i in range(1000)]
    t_list = [threading.Thread(target=test, args=(i, )) for i in range(1000)]
    for t in t_list:
        t.start()


if __name__ == '__main__':
    main()

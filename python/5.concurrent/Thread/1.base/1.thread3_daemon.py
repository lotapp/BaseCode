import time
from threading import Thread, active_count


def test1():
    print("test1")
    time.sleep(1)
    print("test1 ok")


def test2():
    print("test2")
    time.sleep(2)
    print("test2 ok")


def main():
    t1 = Thread(target=test1)
    t2 = Thread(target=test2, daemon=True)
    t1.start()
    t2.start()
    t1.join()
    print(active_count())
    print(t1.is_alive)
    print(t2.is_alive)
    # t2.join() # 除非加这一句才等daemon线程，不然直接不管了


if __name__ == '__main__':
    main()

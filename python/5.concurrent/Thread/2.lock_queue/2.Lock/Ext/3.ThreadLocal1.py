from multiprocessing.dummy import threading

global_local = threading.local()


def show_name():
    print(f"[{threading.current_thread().name}]{global_local.name}")


def task1():
    global_local.name = "小明"
    show_name()


def task2():
    global_local.name = "小张"
    show_name()


def main():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()

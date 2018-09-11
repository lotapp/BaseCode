from multiprocessing.dummy import threading

global_dict = {}


def task1():
    # 根据当前线程查找：
    global_dict[threading.current_thread()] = 10
    global_dict[threading.current_thread()] += 10


def task2():
    # 根据当前线程查找：
    global_dict[threading.current_thread()] = 10
    global_dict[threading.current_thread()] -= 10


def main():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(global_dict)


if __name__ == '__main__':
    main()

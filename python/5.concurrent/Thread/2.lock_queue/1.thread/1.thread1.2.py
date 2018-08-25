from multiprocessing.dummy import threading, Lock

num = 0  # def global num


def test(i, lock):
    print(f"子进程：{i}")
    global num
    for i in range(100000):
        with lock:
            num += 1


def main():
    lock = Lock()
    p_list = [threading.Thread(target=test, args=(i, lock)) for i in range(5)]
    for i in p_list:
        i.start()
    for i in p_list:
        i.join()
    print(num)


if __name__ == '__main__':
    main()

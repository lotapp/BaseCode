from multiprocessing.dummy import threading

num = 0  # def global num


def test(i):
    print(f"子进程：{i}")
    global num
    for i in range(100000):
        num += 1


def main():
    p_list = [threading.Thread(target=test, args=(i, )) for i in range(5)]
    for i in p_list:
        i.start()
    for i in p_list:
        i.join()
    print(num)  # 应该是500000，发生了数据混乱，结果少了很多


if __name__ == '__main__':
    main()

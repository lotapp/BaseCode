from multiprocessing import Process, Value


def proc_test1(value):
    for i in range(1000):
        with value.get_lock():
            value.value += 1
        # if value.acquire():
        #     value.value += 1
        # value.release()


def main():
    value = Value("i", 0)
    p_list = [Process(target=proc_test1, args=(value, )) for i in range(5)]
    # 批量启动
    for i in p_list:
        i.start()
    # 批量资源回收
    for i in p_list:
        i.join()
    print(value.value)


if __name__ == '__main__':
    main()
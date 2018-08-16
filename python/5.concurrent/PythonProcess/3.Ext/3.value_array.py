from multiprocessing import Process, Value, Array


def proc_test1(value, array):
    print("子进程1", value.value)
    array[0] = 10
    print("子进程1", array[:])


def proc_test2(value, array):
    print("子进程2", value.value)
    array[1] = 10
    print("子进程2", array[:])


def main():
    try:
        value = Value("d", 3.14)  # d 类型，相当于C里面的double
        array = Array("i", range(10))  # i 类型，相当于C里面的int
        print(type(value))
        print(type(array))

        p1 = Process(target=proc_test1, args=(value, array))
        p2 = Process(target=proc_test2, args=(value, array))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

        print("父进程", value.value)  # 获取值
        print("父进程", array[:])  # 获取值
    except Exception as ex:
        print(ex)
    else:
        print("No Except")


if __name__ == '__main__':
    main()

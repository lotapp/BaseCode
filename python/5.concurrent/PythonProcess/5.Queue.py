from multiprocessing import Process, Queue


def main():
    q = Queue()
    for i in range(10000):
        print(i)
        q.put("mmd")
    for i in range(10000):
        print(i, q.get())


if __name__ == '__main__':
    main()
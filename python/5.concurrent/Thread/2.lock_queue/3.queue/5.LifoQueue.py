from queue import LifoQueue


def main():
    queue = LifoQueue()

    for i in range(10):
        queue.put(i)

    for i in range(queue.qsize()):
        print(queue.get())


if __name__ == '__main__':
    main()

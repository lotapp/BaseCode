from multiprocessing import Process, Queue


def test(q):
    q.put("[子进程]老爸，我出去嗨了")
    print(q.get())


def main():
    q = Queue()
    p = Process(target=test, args=(q, ))
    p.start()
    msg = q.get()
    print(msg)
    q.put("[父进程]去吧比卡丘～")
    p.join()


if __name__ == '__main__':
    main()
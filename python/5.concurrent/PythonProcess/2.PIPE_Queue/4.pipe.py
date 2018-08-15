from multiprocessing import Process, Pipe


def test(w):
    w.send("[子进程]老爸，老妈回来记得喊我一下～")
    msg = w.recv()
    print(msg)


def main():
    r, w = Pipe()
    p1 = Process(target=test, args=(w, ))
    p1.start()
    msg = r.recv()
    print(msg)
    r.send("[父进程]滚犊子，赶紧写作业，不然我得跪方便面！")
    p1.join()


if __name__ == '__main__':
    main()
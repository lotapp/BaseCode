from multiprocessing import Process, Pipe


def test(w):
    # 只能写
    w.send("[子进程]老爸，咱们完了，老妈一直在门口～")


def main():
    r, w = Pipe(duplex=False)
    p1 = Process(target=test, args=(w, ))
    p1.start()  # 你把这个放在join前面就直接死锁了
    msg = r.recv()  # 只能读
    print(msg)
    p1.join()


if __name__ == '__main__':
    main()
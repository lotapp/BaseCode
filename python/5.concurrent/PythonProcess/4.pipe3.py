from multiprocessing import Pipe, Pool


def proc_test1(conn):
    conn.send("[小明]小张，今天哥们要见一女孩，你陪我呗，我24h等你回复哦～")
    msg = conn.recv()
    print(msg)


def proc_test2(conn):
    msg = conn.recv()
    print(msg)
    conn.send("[小张]不去，万一被我帅气的外表迷倒就坑了～")


def main():
    conn1, conn2 = Pipe()
    p = Pool()
    p.apply_async(proc_test1, (conn1, ))
    p.apply_async(proc_test2, (conn2, ))
    p.close()  # 关闭池，不再接收新任务
    p.join()  # 等待回收


if __name__ == '__main__':
    main()
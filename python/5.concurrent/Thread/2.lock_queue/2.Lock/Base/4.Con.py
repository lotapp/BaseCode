from multiprocessing.dummy import Pool as ThreadPool, Condition

s_list = []
con = Condition()


def Shop(i):
    global con
    global s_list
    # 加锁保护共享资源
    for x in range(5):
        with con:
            s_list.append(x)
            print(f"[生产者{i}]生产商品{x}")
            con.notify_all()  # 通知消费者有货了


def User(i):
    global con
    global s_list
    while True:
        with con:
            if s_list:
                print(f"列表商品：{s_list}")
                name = s_list.pop()  # 消费商品
                print(f"[消费者{i}]消费商品{name}")
                print(f"列表剩余：{s_list}")
            else:
                con.wait()


def main():
    p = ThreadPool()
    # 两个生产者
    p.map_async(Shop, range(2))
    # 五个消费者
    p.map_async(User, range(5))
    p.close()
    p.join()


if __name__ == '__main__':
    main()

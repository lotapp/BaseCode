from multiprocessing.dummy import threading

count = 100  # 库存100件
bar = threading.Barrier(1000, timeout=5)


def shopping(id):
    global count, bar
    try:
        bar.wait()  # Barrier wait
    except threading.BrokenBarrierError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
    # 乐观锁
    if count > 0:  # if count - 1 >= 0:
        count -= 1
        print(f"线程{id}~抢到一件商品\n")


def main():
    t_list = [threading.Thread(target=shopping, args=(i,)) for i in range(1000)]
    print("准备开抢ing")
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    print(f"剩余库存{count}")


if __name__ == '__main__':
    main()

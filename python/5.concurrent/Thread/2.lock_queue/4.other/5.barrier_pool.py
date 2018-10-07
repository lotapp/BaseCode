from multiprocessing.dummy import Pool as ThreadPool, Barrier

count = 100  # 库存100件
bar = Barrier(1000, timeout=5)


def shopping(id):
    global count, bar
    try:
        bar.wait()  # Barrier wait
    except Exception as ex:
        print(ex)
    # 乐观锁
    if count > 0:  # if count - 1 >= 0:
        count -= 1
        print(f"线程{id}~抢到一件商品\n")


def main():
    pool = ThreadPool(1000)  # 一定要指定线程数，不然就坑了自己（自己想为啥）
    print("准备开抢")
    pool.map_async(shopping, range(1000))
    pool.close()
    pool.join()
    print(f"剩余库存{count}")


if __name__ == '__main__':
    main()

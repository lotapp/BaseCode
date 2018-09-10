from multiprocessing.dummy import Pool as ThreadPool, Lock

xiaoming = 8000
xiaozhang = 3000
xiaozhou = 5000


# 小明转账2000给小张
def a_to_b(lock):
    global xiaoming
    global xiaozhang
    with lock:
        xiaoming -= 2000
        xiaozhang += 2000


# 小明转账5000给小周
def a_to_c(lock):
    global xiaoming
    global xiaozhou
    with lock:
        xiaoming -= 5000
        xiaozhou += 5000


def main():
    print(f"[还钱前]小明{xiaoming},小张{xiaozhang},小周{xiaozhou}")
    lock = Lock()
    p = ThreadPool()
    p.apply_async(a_to_b, args=(lock, ))
    p.apply_async(a_to_c, args=(lock, ))
    p.close()
    p.join()
    print(f"[还钱后]小明{xiaoming},小张{xiaozhang},小周{xiaozhou}")


if __name__ == '__main__':
    main()

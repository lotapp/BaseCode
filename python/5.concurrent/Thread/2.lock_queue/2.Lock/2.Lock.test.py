from multiprocessing.dummy import Pool as ThreadPool, Lock

xiaoming = 8000
xiaozhang = 3000
xiaozhou = 5000


def test(lock):
    global xiaoming
    global xiaozhang
    global xiaozhou
    
    print("[开始]小明转账2000给小张")
    lock.acquire()  # 获取锁
    xiaoming -= 2000
    xiaozhang += 2000

    print("[开始]小明转账5000给小周")
    lock.acquire()  # 获取锁
    xiaoming -= 5000
    xiaozhou += 5000
    lock.release()  # 释放锁
    print("[结束]小明转账5000给小周")

    lock.release()  # 释放锁
    print("[开始]小明转账2000给小张")


def main():
    print(f"[还钱前]小明{xiaoming},小张{xiaozhang},小周{xiaozhou}")
    lock = Lock()
    p = ThreadPool()
    p.apply_async(test, args=(lock, ))
    p.close()
    p.join()
    print(f"[还钱后]小明{xiaoming},小张{xiaozhang},小周{xiaozhou}")


if __name__ == '__main__':
    main()

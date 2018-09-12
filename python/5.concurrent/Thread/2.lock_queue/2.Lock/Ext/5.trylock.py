from time import sleep
from random import random
from multiprocessing.dummy import Pool as ThreadPool, Lock


class People(object):
    def __init__(self, name, money=5000):
        self.name = name
        self.lock = Lock()  # 非阻塞等
        self.money = money  # 设置一个初始金额


def transfer(p_from, p_to, money):
    flag = True
    while flag:
        # 尝试获取p_from.lock
        if p_from.lock.acquire(False):  # 非阻塞
            try:
                sleep(1)  # 模拟网络延迟
                # 尝试获取p_to.lock
                if p_to.lock.acquire(False):
                    try:
                        p_from.money -= money
                        p_to.money += money
                        flag = False
                    finally:
                        print("p_to release")
                        p_to.lock.release()  # 释放锁
            finally:
                p_from.lock.release()  # 释放锁
        sleep(random())  # 随机生成[0,1)的小数


def main():
    xiaoming = People("小明")
    xiaozhang = People("小张")
    xiaopan = People("小潘")
    print(f"[互刷前]小明：{xiaoming.money},小张：{xiaozhang.money},小潘：{xiaopan.money}")

    p = ThreadPool()
    for i in range(3):
        p.apply_async(transfer, args=(xiaoming, xiaozhang, 1000))
        if i == 1:
            p.apply_async(transfer, args=(xiaopan, xiaoming, 1000))
        p.apply_async(transfer, args=(xiaozhang, xiaoming, 1000))
    p.close()
    p.join()

    print(f"[互刷后]小明：{xiaoming.money},小张：{xiaozhang.money},小潘：{xiaopan.money}")


if __name__ == '__main__':
    main()

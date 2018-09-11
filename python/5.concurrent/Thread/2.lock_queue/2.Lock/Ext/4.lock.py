from time import sleep
from multiprocessing.dummy import Pool as ThreadPool, Lock


class People(object):
    def __init__(self, name, money=5000):
        self.name = name
        self.lock = Lock()
        self.money = money  # 设置一个初始金额


def transfer(p_from, p_to, money):
    with p_from.lock:
        p_from.money -= money
        sleep(1)  # 模拟网络延迟
        with p_to.lock:
            p_to += money


def main():
    xiaoming = People("小明")
    xiaozhang = People("小张")
    print(f"[互刷前]小明：{xiaoming.money},小张：{xiaozhang.money}")

    p = ThreadPool()
    p.apply_async(transfer, args=(xiaoming, xiaozhang, 1000))
    p.apply_async(transfer, args=(xiaozhang, xiaoming, 1000))
    p.close()
    p.join()

    print(f"[互刷后]小明：{xiaoming.money},小张：{xiaozhang.money}")


if __name__ == '__main__':
    main()

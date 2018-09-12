from time import sleep
from multiprocessing.dummy import Pool as ThreadPool, Lock


class Account(object):
    def __init__(self, name, money=5000):
        self.name = name
        self.lock = Lock()
        self.money = money  # 设置一个初始金额


class Bank(object):
    tie_lock = Lock()

    @classmethod
    def __get_hash(cls, obj):
        return id(obj)  # hash_func(obj)

    @classmethod
    def transfer(cls, p_from, p_to, money):
        """p_from：谁转账,p_to：转给谁,money:转多少"""
        from_hash = cls.__get_hash(p_from)
        to_hash = cls.__get_hash(p_to)

        print(f"from:{p_from.name}to{p_to.name}=>{money}")
        # 规定：谁大先锁谁
        if from_hash > to_hash:
            print("from_hash > to_hash")
            with p_from.lock:
                p_from.money -= money
                sleep(1)  # 模拟网络延迟
                with p_to.lock:
                    p_to.money += money
        elif from_hash < to_hash:
            print("from_hash < to_hash")
            with p_to.lock:
                p_to.money += money
                sleep(1)  # 模拟网络延迟
                with p_from.lock:
                    p_from.money -= money
        # hash出现碰撞时处理：（可能性很低）
        else:
            print("from_hash < to_hash")
            # 平局的时候，大家一起抢一个中间锁，谁抢到谁先转账
            with cls.tie_lock:
                with p_from.lock:
                    p_from.money -= money
                    sleep(1)  # 模拟网络延迟
                    with p_to.lock:
                        p_to.money += money


def main():
    xiaoming = Account("小明")
    xiaozhang = Account("小张")
    xiaopan = Account("小潘")
    print(f"[互刷前]小明：{xiaoming.money},小张：{xiaozhang.money},小潘{xiaopan.money}")

    p = ThreadPool()
    for i in range(3):
        p.apply_async(Bank.transfer, args=(xiaoming, xiaozhang, 1000))
        if i == 1:  # 小潘突然间还了1000给小明
            p.apply_async(Bank.transfer, args=(xiaopan, xiaoming, 1000))
        p.apply_async(Bank.transfer, args=(xiaozhang, xiaoming, 1000))
    p.close()
    p.join()

    print(f"[互刷后]小明：{xiaoming.money},小张：{xiaozhang.money},小潘{xiaopan.money}")


if __name__ == '__main__':
    main()

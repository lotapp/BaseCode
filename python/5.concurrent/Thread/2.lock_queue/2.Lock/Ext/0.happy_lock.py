from multiprocessing.dummy import threading, Condition

count = 100  # 库存100件


# 模拟Java里的CountDownLatch（条件变量模拟）
# 可以理解为赛跑，当运动员全部准备好了，裁判一枪下去，开始比赛
class CountDownLatch(object):
    def __init__(self):
        self.con = Condition()  # 条件变量

    def wait(self):
        with self.con:
            self.con.wait()

    def countDown(self):
        with self.con:
            self.con.notify_all()  # 开枪（唤醒所有线程）


class MyThread(threading.Thread):
    def __init__(self, id, con):
        self.id = id
        self.con = con
        super().__init__()

    def run(self):
        global count
        self.con.wait()
        if count > 0:  # if count - 1 >= 0:
            count -= 1
            print(f"线程{self.id}~抢到一件商品")


def main():
    con = CountDownLatch()  # 条件变量
    t_list = [MyThread(id=i, con=con) for i in range(1000)]
    for t in t_list:
        t.start()
    print("准备开抢")
    con.countDown()  # 唤醒所有
    for t in t_list:
        t.join()
    print(f"剩余库存{count}")


if __name__ == '__main__':
    main()

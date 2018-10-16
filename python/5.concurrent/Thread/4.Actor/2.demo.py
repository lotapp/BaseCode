from BaseActor import BaseActor


class PeopleActor(BaseActor):
    def __init__(self):
        super().__init__()
        self.money = 5000  # 每个人有5000块

    def run(self):
        while True:
            msg = self.recv()
            # 转账msg为负，收账msg为正
            if isinstance(msg, int):
                self.money += msg

    @classmethod
    def transfer(cls, p_from, p_to, money):
        p_from.send(-money)
        p_to.send(money)


def main():
    xiaoming = PeopleActor()
    xiaozhang = PeopleActor()
    xiaopan = PeopleActor()
    # 批量启动
    for actor in (xiaoming, xiaozhang, xiaopan):
        actor.start()

    print(f"[转账前]小张：{xiaozhang.money},小明：{xiaoming.money},小潘：{xiaopan.money}")
    for i in range(5):
        if i == 2:
            # 【测试】转账过程中小潘还了小明500元
            PeopleActor.transfer(xiaopan, xiaoming, 500)
        # 小明转账1000给小张
        PeopleActor.transfer(xiaoming, xiaozhang, 1000)
        # 小张转账1000给小明
        PeopleActor.transfer(xiaozhang, xiaoming, 1000)
        print(f"[本次转账]小张:{xiaozhang.money},小明:{xiaoming.money},小潘:{xiaopan.money}")

    for actor in (xiaoming, xiaozhang, xiaopan):
        actor.close()
        actor.join()
    print(f"[转账后]小张：{xiaozhang.money},小明：{xiaoming.money},小潘：{xiaopan.money}")


if __name__ == '__main__':
    main()

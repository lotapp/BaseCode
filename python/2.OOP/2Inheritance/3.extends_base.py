# 调用父类的方法
class Father(object):
    def eat(self):
        print("文雅的吃饭")


class Son(Father):
    def eat(self):
        # 调用父类方法第1种（super().方法）
        super().eat()


class GrandSon(Son):
    def eat(self):
        # 调用父类方法第2种（记得传self）
        Son.eat(self)


def main():
    xiaoming = Son()
    xiaoming.eat()

    xiaoli = GrandSon()
    xiaoli.eat()


if __name__ == '__main__':
    main()

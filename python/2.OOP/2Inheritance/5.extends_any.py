# 多继承引入
class Father(object):
    def eat(self):
        print("文雅的吃饭")


class Mom(object):
    def run(self):
        print("小碎步")


class Son(Father, Mom):
    pass


def main():
    son = Son()
    son.eat()
    son.run()


if __name__ == '__main__':
    main()

# 如果父类里面有同名方法怎么知道调哪个？
class Father(object):
    def eat(self):
        print("文雅的吃饭")


class Mom(object):
    def eat(self):
        print("开心的吃饭")


class Son(Mom, Father):
    pass


def main():
    son = Son()
    son.eat()
    print(Son.__mro__)  # 一般同名方法都是先看自己有没有，然后看继承顺序，比如这边先看Mom再看Father


if __name__ == '__main__':
    main()

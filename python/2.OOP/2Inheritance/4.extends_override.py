# 重写父类方法==>子类和父类有同名方法
class Father(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s喜欢文雅的吃饭" % self.name)


class Son(Father):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print("%s喜欢大口吃饭大口喝酒" % self.name)


def main():
    xiaoming = Father("小明")
    xiaoming.eat()

    xiaopan = Son("小潘")
    xiaopan.eat()


if __name__ == "__main__":
    main()

# 当子类和父类都存在相同的eat()方法时，我们说，子类的eat()覆盖了父类的eat()，在代码运行的时候，总是会调用子类的eat()。这样，我们就获得了继承的另一个好处：多态

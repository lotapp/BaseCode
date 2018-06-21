class Animal(object):
    # 类属性
    name = '动物'

    def __init__(self):
        # 实例属性
        self.age = 1

    def __bug(self):
        """实例私有方法"""
        print("我是动物类身上的私有方法：bug")

    def eat(self):
        """实例方法"""
        print("我是实例方法，动物会吃哦～")

    @classmethod
    def call(cls):
        """类方法"""
        print("我是类方法，动物会叫哦")

    @staticmethod
    def play():
        """静态方法"""
        print("我是静态方法，动物会玩耍哦")


class Dog(Animal):
    pass


def main():
    dog = Dog()
    # 实例属性
    print(dog.age)
    # 实例方法
    dog.eat()

    # 类属性
    print(dog.name)
    # 类方法
    dog.call()
    Dog.call()
    Animal.call()

    # 静态方法
    dog.play()
    Dog.play()
    Animal.play()


if __name__ == '__main__':
    main()

# 私有的属性方法不会被子类继承

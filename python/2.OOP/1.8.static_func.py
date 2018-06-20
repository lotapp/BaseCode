class Dog(object):
    # 类属性
    name = "小汪"

    # 实例方法
    def __init__(self, age):
        # 实例属性
        self.age = age
        # 打印看看
        print("self id:%s" % id(self))

    # 类方法
    @classmethod
    def show_name(cls):
        # 访问类属性 cls.xxx
        print("我叫%s" % cls.name)
        # 打印看看
        print("cls id:%s" % id(cls))

    # 静态方法
    @staticmethod
    def say_hello():
        print("汪汪汪")


def main():
    # 类名方式访问
    Dog.show_name()
    Dog.say_hello()  # 类名的方式可以访问静态方法

    # 实例对象方式访问
    dog = Dog(2)
    dog.show_name()
    dog.say_hello()


if __name__ == '__main__':
    main()

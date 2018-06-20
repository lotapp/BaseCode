class Dog(object):
    def __init__(self, name):
        self.name = name
        print("初始化完毕")

    def __str__(self):
        return "Dog的名字叫：%s" % self.name

    def __new__(cls, name):
        # 注意参数，是cls，然后其他参数和init保持一致即可
        print("创建对象完毕")
        # 别忘记写返回值哦
        return object.__new__(cls)


def main():
    happy = Dog("Happy")
    print(happy)


if __name__ == '__main__':
    main()

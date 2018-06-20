class Person(object):
    # age为类属性
    age = 1

    def __init__(self, name):
        # name为实例属性
        self.name = name


def main():
    # 类名.类属性
    print(Person.age)
    xiaoming = Person("小明")
    # 对象.类属性
    print(xiaoming.age)


if __name__ == '__main__':
    main()

class Person(object):
    # age为类属性
    age = 1

    def __init__(self, name):
        # name为实例属性
        self.name = name


def main():
    # 类名.类属性
    print(Person.age)

    # 通过对象.类属性修改
    xiaoming = Person("小明")
    xiaoming.age = 100
    print(xiaoming.age)  # 其实，并没有修改成功，只是产生了一个同名age
    print(Person.age)  # 对吧，类属性并没有被修改

    # 通过类名修改
    Person.age = 22  # 如果需要在类外修改类属性，必须通过类对象去引用然后进行修改
    print(xiaoming.age)  # 刚才已经创建一个同名age，所以现在显示的是刚才的值
    print(Person.age)  # 通过类名.类属性 就可以看到值被修改了

    # 如果你还是不信，可以创建一个新对象看看
    xiaopan = Person("小潘")
    print(xiaopan.age)

    # xiaoming实例对象想访问怎么办？
    # 除非del了该实例属性才能正常访问类属性
    del xiaoming.age
    print(xiaoming.age)  # 这时候访问的就是 类属性 了


if __name__ == '__main__':
    main()

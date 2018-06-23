class People(object):
    def eat(self):
        print("人类会吃饭")


class Father(object):
    def eat(self):
        print("优雅的吃饭")


class Teacher(object):
    def eat(self):
        print("赶时间的吃饭")


def eat(obj):
    obj.eat()


def main():
    teacher = Teacher()
    father = Father()
    eat(teacher)
    eat(father)


if __name__ == '__main__':
    main()

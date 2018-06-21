class Animal(object):
    def eat(self):
        print("动物会吃")


class Cat(Animal):
    # 注意一下Python的继承格式
    pass


class Dog(Animal):
    pass


def main():
    cat = Cat()
    dog = Dog()
    cat.eat()
    dog.eat()


if __name__ == "__main__":
    main()

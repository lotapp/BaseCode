# 判断一个变量是否是某个类型 ==> isinstance() or Type
class Animal(object):
    pass


class Dog(Animal):
    pass


def main():
    dog = Dog()
    dog2 = Dog()
    print(type(dog) == Dog)
    print(type(dog) == type(dog2))
    print(type(dog))

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    # arg 2 must be a type or tuple
    # print(isinstance(dog, dog2))


if __name__ == '__main__':
    main()

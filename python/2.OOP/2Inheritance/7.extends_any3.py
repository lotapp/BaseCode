class Animal(object):
    pass


class Flyable(object):
    """飞的方法"""
    pass


class Runable(object):
    """跑的方法"""
    pass


class Dog(Animal, Runable):
    pass


class Cat(Animal, Runable):
    pass


class Bird(Animal, Flyable):
    pass


class Dack(Animal, Runable, Flyable):
    """鸭子会飞也会跑"""
    pass

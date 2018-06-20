# 装饰器，让方法和属性一样方便
# Python内置的@property装饰器就是负责把一个方法变成属性调用的，来个例子


class Student(object):
    def __init__(self, name, age):
        # 一般需要用到的属性都直接放在__init__里面了
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("age must > 0")

    def show(self):
        print("name:%s,age:%s" % (self.name, self.age))


xiaoming = Student("小明", 22)
xiaoming.name = "小潘"
xiaoming.age = -2
xiaoming.show()
class Student(object):
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("age must > 0")

    def show(self):
        self.__sleep(1)
        print("name:%s,age:%d" % (self._name, self._age))

    def __sleep(self, time):
        pass


zhangsan = Student("张三", 20)
zhangsan.show()  # name:张三,age:20

# 私有方法就是在方法前面加两个下划线__
# zhangsan.__sleep(1)# 私有的方法没法调 NameError:name '_Student__sleep' is not defined
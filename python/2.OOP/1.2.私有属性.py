class Student:
    def __init__(self, name, age):
        # self.set_name(name)
        self._name = name
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
        print("name:%s,age:%d" % (self._name, self._age))


zhangsan = Student("张三", 20)  # ("张三",-20)
zhangsan.age = -1  # 同样的代码，只是属性前面加了下划线（私有方法就是在方法前面加两个下划线__）
zhangsan.show()  # name:张三,age:20
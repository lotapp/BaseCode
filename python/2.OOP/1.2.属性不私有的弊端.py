class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("age must > 0")

    def show(self):
        print("name:%s,age:%d" % (self.name, self.age))


zhangsan = Student("张三", -20)
zhangsan.show()  # name:张三,age:-20
zhangsan.age = -1  # set_age方法形同虚设，我完全可以直接访问字段了（python引入私有属性的方式有点怪异，在属性前面加_，eg:1.3）
zhangsan.show()  # name:张三,age:-1

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self别忘记写了
    def __str__(self):
        return "姓名：%s，年龄：%s" % (self.name, self.age)


lisi = Student("李四", 22)
print(lisi)
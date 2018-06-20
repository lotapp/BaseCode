class Student(object):
    def __init__(self, name, age):
        self.__name = name
        # 一般需要用到的属性都直接放在__init__里面了
        # self.__age = age
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("age must > 0")

    def show(self):
        print("name:%s,age:%s" % (self.__name, self.__age))


zhangsan = Student("张三", -20)
zhangsan.__age = -1  # 同样的代码，只是属性前面加了下划线
zhangsan.show()

# 搞事情
zhangsan._Student__age = -1
zhangsan.show()

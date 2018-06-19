# # 类名首字母大写
# class Student(object):
#     """创建一个学生类"""

#     # 没有属性定义，直接使用即可
#     # 定义一个方法，方法里面必须有self（相当于C#的this）
#     def show(self):
#         print("name:%s age:%d" % (self.name, self.age))

# # 实例化一个张三
# zhangsan = Student()
# # 给name，age属性赋值
# zhangsan.name = "张三"
# zhangsan.age = 22
# # 调用show方法
# zhangsan.show()

# # 打印一下类和类的实例
# print(Student)
# print(zhangsan)  # 张三实例的内存地址：0x7fb6e8502d30


class Student:
    # 初始化赋值
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("name:%s age:%d" % (self.name, self.age))


# 有了__init__方法，在创建实例的时候，就不能传入空的参数了
# lisi=Student()

# 创建一个正确的实例
xiaowang = Student("小王", 22)
xiaowang.show()

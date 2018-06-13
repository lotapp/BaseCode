# 没有属性定义，直接用的时候定义赋值 =_=!尴尬
# class Student:
#     # 构造函数
#     def __init__(self):
#         print("默认构造函数")
#     def show(self):
#         print("name:%s age:%d"%(self.name,self.age))

# xiaowang=Student()
# xiaowang.name="小王"
# xiaowang.age=22
# xiaowang.show()

class Student:
    # 构造函数(初始化赋值)
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print("name:%s age:%d"%(self.name,self.age))

xiaowang=Student("小王",22)
xiaowang.show()

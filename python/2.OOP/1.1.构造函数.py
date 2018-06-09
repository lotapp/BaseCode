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

# #TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# xiaoli=Student() #如果不定义默认的无参构造函数也一样报错（和C#一样）
# xiaoli.name="小李"
# xiaoli.age=18
# xiaoli.show()
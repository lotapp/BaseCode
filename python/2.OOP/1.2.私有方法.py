class Student:
    def __init__(slef):
        pass
    def __init__(slef,name,age):
        slef.set_name(name)
        slef.set_age(age)
    
    def get_name(slef):
        return slef._name
    
    def set_name(slef,name):
        slef._name=name

    def get_age(slef):
        return slef._age
    
    def set_age(slef,age):
        if age>0:
            slef._age=age
        else:
            print("age must > 0")
    
    def show(slef):
        slef.__sleep(1)
        print("name:%s,age:%d"%(slef._name,slef._age))
    
    def __sleep(slef,time):
        pass
    
zhangsan=Student("张三",20)
zhangsan.show() #name:张三,age:20

# 私有方法就是在方法前面加两个下划线__
# zhangsan.__sleep(1)# 私有的方法没法调 NameError: name '_Student__sleep' is not defined
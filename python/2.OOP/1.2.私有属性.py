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
        print("name:%s,age:%d"%(slef._name,slef._age))
    
zhangsan=Student("张三",20) # ("张三",-20)
zhangsan.age=-1 #同样的代码，只是属性前面加了下划线（私有方法就是在方法前面加两个下划线__）
zhangsan.show() #name:张三,age:20
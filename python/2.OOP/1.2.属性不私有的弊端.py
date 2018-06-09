class Student:
    def __init__(slef):
        pass
    def __init__(slef,name,age):
        slef.name=name
        slef.age=age
    
    def get_name(slef):
        return slef.name
    
    def set_name(slef,name):
        slef.name=name

    def get_age(slef):
        return slef.age
    
    def set_name(slef,age):
        if age>0:
            slef.age=age
        else:
            print("age must > 0")
    def show(slef):
        print("name:%s,age:%d"%(slef.name,slef.age))
    
zhangsan=Student("张三",-20)
zhangsan.show() # name:张三,age:-20
zhangsan.age=-1 #set_age方法形同虚设，我完全可以直接访问字段了（python引入私有属性的方式有点怪异，在属性前面加_，eg:1.3）
zhangsan.show() # name:张三,age:-1

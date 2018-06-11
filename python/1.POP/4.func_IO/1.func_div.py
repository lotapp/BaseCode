# 函数
# 定义一个无参函数
def get_name():
    print("我叫张三")

# 定义一个含参数的函数（name和age都是形参）
def show_infos(name,age):
    """打印name和age"""
    print("我叫",name,"我的年龄是",age)#这种输出方式会自动以空格连接字符串

# 定义一个默认参数的函数
def default_param(name,age=23):
    """age默认为23"""
    print("我叫",name,"我的年龄是",age)#这种输出方式会自动以空格连接字符串

# 定义有返回值的函数
def div_have_return(a,b):
    """计算a+b，返回计算结果"""#函数文档说明
    return a+b

# 定义含有多个返回值的函数（利用了元组）
def div_have_returns(a,b):
    """计算a+b的和，计算a-b，并返回两个结果"""
    return (a+b),(a-b)

# 调用一个无参函数
get_name()

# 调用一个含参数的函数
show_infos("李四",22)#实参

# 定义一个默认参数的函数
default_param("张三")

# 调用有返回值的函数
result=div_have_return(1,2)
print("计算结果为",result)

# 调用含有多个返回值的函数
sum,dvalue=div_have_returns(1,2)
print("sum:",result,"D-value:",dvalue)

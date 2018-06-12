# 函数
# 定义一个无参函数
def get_name():
    print("我叫张三")

# 定义一个含参数的函数（name和age都是形参）
def show_infos(name,age):
    """打印name和age"""
    print("我叫",name,"我的年龄是",age)#这种输出方式会自动以空格连接字符串

# 定义一个默认参数(缺省参数)的函数
# 默认参数(缺省参数)必须指向不变对象，比如定义一个List。改变了内容，则下次调用时，默认参数(缺省参数)的内容就变了，不再是函数定义时的值了
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

##############################################################
# 传入多个参数系列（引用传参）
# 通过元组、列表实现
def default_some_params(nums):
    """借助Tuple和list"""
    sum=0
    for item in nums:
        sum+=item
    return sum
    
# 定义一个可变参数的函数(名字一般都是*args)
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，接收到的参数是一个tuple。调用该函数时，可以传入任意个参数（包括0个参数）
def default_params(*args):
    """定义一个可变参数,用来求所有参数的总和"""
    sum=0
    for item in args:
        sum+=item
    return sum

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 关键字参数允许你传入0个或任意个含key-value的参数，自动组装为一个dict
def default_kv_params(name,age=23,**kv):
    """输出输出用户传参"""
    print("我叫",name,"我的年龄是",age,"dict:",kv)


# 同时定义可变参数+关键字参数
def default_god_params(name,age=23,*args,**kv):
    """同时有可变参数+关键字参数的使用方法"""
    print("我叫",name,"我的年龄是",age,"list:",args,"dict:",kv)

###################################################################

# 调用一个无参函数
get_name()

# 调用一个含参数的函数
show_infos("李四",22)#实参

# 调用一个默认参数(缺省参数)的函数
default_param("张三")

# 调用有返回值的函数
result=div_have_return(1,2)
print("计算结果为",result)

# 调用含有多个返回值的函数
sum,dvalue=div_have_returns(1,2)
print("sum:",result,"D-value:",dvalue)

############# 传入多个参数系列 #############
# 元组传入
default_some_params((1,2,3,4,5))

# 列表传入
default_some_params(list(range(1,6)))

# 调用一个可变参数的函数
default_params(1,2,3,4,5)

# 传一个list或者Tuple
# # range(1,6) ==> [1,6)
default_params(*list(range(1,6)))

test_tuple=(1,2,3,4,5)
default_params(*test_tuple)

# 调用关键字参数
default_kv_params("dnt",web="www.baidu.com",qq=110)

# 调用可变参数+关键字参数
#完整调用(有名字给kv,没名字给args)
default_god_params("dnt",24,1,2,3,4,5,web="www.baidu.com",qq=110)
#只调用可变参数
default_god_params("dnt",24,1,2,3,4,5)
# 只调用关键字参数
default_god_params("dnt",24,web="www.baidu.com",qq=110)

# 传元组和字典
test_tuple=(1,2,3,4,5)
test_dict={"web":"www.baidu.com","qq":110}

default_god_params(*test_tuple,**test_dict)
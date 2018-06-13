####################### 函数递归 ###################################
# 函数递归调用其实就是自己调用自己，关键点只要考虑什么时候跳出，其他的交给程序即可(没有跳出就是死循环)
# 阶乘案例 n!
def factorial(n):
    if n==1:
        return n #跳出
    return n*factorial(n-1) #规律公式

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
# 跳出点==> 第一个字符和最后一个字符不是空格
def my_trim(input_str):
    if input_str[0] != " " and input_str[-1] != " ":
        return input_str
    elif input_str[0]==" ":
        return my_trim(input_str[1:])
    elif input_str[-1]==" ":
        return my_trim(input_str[:-1])

print(factorial(3))

print(my_trim("我去  "))
print(my_trim("  我去"))
print(my_trim("  我去  "))

####################### 匿名函数 ###################################
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数
# lambda 参数: 表达式
# 来个简单求和案例:
sum=lambda a,b: a+b
sum(1,2) #调用一下看看(有点js的感觉,函数可以直接赋值给变量,然后直接用)

# 来个实际案例,还记得list的排序吗?
# 这次按照指定key排序(有点 SQL 里面 order by 的感觉)
data_list=[
    {"name":"张三","age":20},
    {"name":"李四","age":21},
    {"name":"王五","age":22}]

# help(data_list.sort)
# 按照age排序
data_list.sort(key=lambda x:x["age"])
print(data_list)

# 按照name排序
data_list.sort(key=lambda x:x["name"])
print(data_list)

# 当函数的参数传递(有时候需要传一个匿名方法去函数中处理某些事情)
def sum(a,b,func):
   return func(a,b)

print(sum(1,2,lambda x,y: x+y))

# ##############################################################
# # 可变类型全局变量，不可变型全局变量：
a=100

def set_num(num):
    a=120

print(a)
set_num(a)
print(a)

# 在函数中不使用global声明全局变量不能修改全局变量==>本质是不能修改全局变量的指向，即不能将全局变量指向新的数据
# 对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量
# 对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量

####################### 验证系列 ###################################
# 自摸索阶段:(之前很多资料说不能调用print函数,自己测试下)
# 定义一个无参匿名函数
printf=lambda:print("I Love You")
printf()

# 可变类型与不可变类型的变量分别作为函数参数时
# 感到疑惑可以看之前的运算符扩展（https://www.cnblogs.com/dotnetcrazy/p/9155310.html#ext）
def default_some_params(nums):
    nums+=nums

test_num=1
default_some_params(test_num)
print(test_num)

test_list=list(range(1,6))
default_some_params(test_list)
print(test_list)

# # Python中函数参数是引用传递。对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。

# ##############################################################
# 函数名能不能重复的问题（能不能重载：具有不同的参数的类型或参数的个数）
def test():
    pass

def test(a,b):
    return a+b

test(1,2)
# # TypeError: test() missing 2 required positional arguments: 'a' and 'b'
# test() #前一个直接被后一个覆盖掉了
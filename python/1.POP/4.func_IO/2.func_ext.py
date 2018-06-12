# 递归案例
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
# def trim(s):
#     if s[:1] != ' ' and s[-1:] != ' ':
#         return s
#     elif s[:1] == ' ':
#         return trim(s[1:])
#     else：
#         return trim(s[:-1])

# 可变类型与不可变类型的变量分别作为函数参数时
#
def default_some_params(nums):
    

test_list=list(range(1,6))
default_some_params(test_list)
print(test_list)

# Python中函数参数是引用传递。对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。

##############################################################

# 可变类型全局变量，不可变型全局变量：


# 在函数中不使用global声明全局变量不能修改全局变量==>本质是不能修改全局变量的指向，即不能将全局变量指向新的数据
# 对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量
# 对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量

##############################################################

# 函数名不能重复
def test():
    pass

def test(a,b):
    return a+b
#TypeError: test() missing 2 required positional arguments: 'a' and 'b'
test() #前一个直接被后一个覆盖掉了
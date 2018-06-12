###################### List切片系列 ##############################
# 列表的切片操作很有用，主要跟数据相关，实际应用中和dict（后面会讲）联合使用
top100=list(range(1,101)) #[1,101) => 1~100
print(top100)

# 取前10个元素

# 取最后10个元素

# 前11~20（eg：第二页）

# 取80~90（eg:倒数第二页）

# 前10个，间隔取（eg:隔行换样式）

# 每10个取一个（eg:test的时候十里挑一）

# 补充概念，str和tuple 也可以用切片操作，只是因为他们不可变，所以结果是一个新的str和tuple

###################### 迭代系列 ##############################
# 参考链接：http://t.cn/RK0f82P
# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

from collections import Iterable

isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代 False

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

############################## 列表生成系列 ##############################
# 参考链接：http://t.cn/RK03rgI
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成[1x1, 2x2, 3x3, ..., 10x10]
#以前：
div_list = []
for x in range(1, 11):
    div_list.append(x * x)

# 现在(列表生成式则可以用一行语句代替循环生成上面的list)：
div_list=[x * x for x in range(1, 11)]

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
[x * x for x in range(1, 11) if x % 2 == 0] #[4, 16, 36, 64, 100]

# 为数学而生（还可以使用两层循环，可以生成全排列）：
[m + n for m in 'ABC' for n in 'XYZ'] #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下的所有文件和目录名
import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()] #['y=B', 'x=A', 'z=C']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

# 注意：如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'

# 使用内建的isinstance函数可以判断一个变量是不是字符串
x = 'abc'
y = 123
isinstance(x, str) #True
isinstance(y, str) #False

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
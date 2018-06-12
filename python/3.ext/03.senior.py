# 参考链接：http://sina.lt/f7Pv
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
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成[1x1, 2x2, 3x3, , 10x10]
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

############################## 列表生成系列 ##############################
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
# <generator object <genexpr> at 0x1022ef630>

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
# next(g)
# next(g)
# 
# next(g) #最后一个
# next(g)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
# 我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
# 正确的方法是使用for循环，因为generator也是可迭代对象
g = (x * x for x in range(10))
for n in g:
    print(n)

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'ok'
# 注意，赋值语句： a, b = b, a + b
# 相当于：
# tuple = (b, a + b)
# a = t[0]
# b = t[1]
# 但不必显式写出临时变量t就可以赋值。

# 上面的函数可以输出斐波那契数列的前N个数：
fib(6)

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'ok'

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
f = fib(6)
# f <generator object fib at 0x104feaaa0>

# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

# 举个简单的例子，定义一个generator，依次返回数字1，3，5：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
o = odd()
next(o)
# step 1
# 1
next(o)
# step 2
# 3
next(o)
# step 3
# 5
next(o)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# 可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来
# 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
for n in fib(6):
    print(n)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generator return value: ok
# 练习：杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles():
    pass

# 小结
# generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

# 请注意区分普通函数和generator函数，普通函数调用直接返回结果：

r = abs(6)
r#6
# generator函数的“调用”实际返回一个generator对象：
g = fib(6)
g#<generator object fib at 0x1022ef948>

####################### 迭代器 ##################################
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

# 可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
isinstance([], Iterable)# True
isinstance({}, Iterable)# True
isinstance('abc', Iterable)# True
isinstance((x for x in range(10)), Iterable)# True
isinstance(100, Iterable)# False

# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

# 可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
isinstance((x for x in range(10)), Iterator)
# True
isinstance([], Iterator)
# False
isinstance({}, Iterator)
# False
isinstance('abc', Iterator)
# False

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)#True
isinstance(iter('abc'), Iterator)#True

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass

# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
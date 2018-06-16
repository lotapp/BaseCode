'''三个单引号多行注释：
print("Hello World!")
print("Hello World!")
print("Hello World!")'''
"""三个双引号多行注释：
print("Hello World!")
print("Hello World!")
print("Hello World!")"""

# 单行注释 输出
print("Hello World!")

# 定义一个变量并输出
name = "小明"
print(name)

print("x" * 10)

print("dnt.dkill.net/now", end='')
print("带你走进中医经络")

print("dnt.dkill.net/now", end="")
print("带你走进中医经络")

# 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
print("I\'m \"OK\"!")

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''我请你吃饭吧～
晚上吃啥？
去厕所，你说呢？''')
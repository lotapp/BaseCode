from my_class import Student

s1 = Student()
s2 = s1

del s1
del s2
print("-" * 10)

# 你被干掉了
# ----------

# # 程序退出的时候，在他运行期间所有占用资源归还操作系统
# # 引用计数
# import sys
# s1=Student()
# sys.getrefcount(s1) #（结果比实际引用大1）【你测也算进去了】

# s2=s1
# print(sys.getrefcount(s1))
# print(sys.getrefcount(s2))

# del s1
# print(sys.getrefcount(s2))
# # sys.getrefcount(s1)#被删掉自然没有了

# del s2
# print("-"*10)

# # del obj
# # sys.getrefcount(obj)

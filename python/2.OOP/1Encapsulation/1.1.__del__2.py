from my_temp import Temp

# t1 = Temp()
# t2 = t1

# del t1
# del t2
# print("-" * 10)

# # 你被干掉了
# # ----------

# 程序退出的时候，在他运行期间所有占用资源归还操作系统
# 引用计数
import sys
t1 = Temp()
print(sys.getrefcount(t1))  #（结果比实际引用大1）【object也会占1个引用计数】

t2 = t1
print(sys.getrefcount(t1))
print(sys.getrefcount(t2))

del t1
print(sys.getrefcount(t2))
# sys.getrefcount(t1)#被删掉自然没有了

del t2
print("-" * 10)

# del obj
# sys.getrefcount(obj)

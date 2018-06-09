# # 只能查询，其他操作和列表差不多（不可变）
# test_tuple=("萌萌哒",1,3,5,"加息","加息")


# # count index
# print(test_tuple.count("加息"))
# print(test_tuple.index("萌萌哒"))#没有find方法
# # 注意是左闭右开区间==>[1,4)
# # print(test_tuple.index("加息", 1, 4))#查不到报错：ValueError: tuple.index(x): x not in tuple

# #下标取
# print(test_tuple[0])

# # 遍历
# for item in test_tuple:
#     print(item)

# i=0
# while i<len(test_tuple):
#     print(test_tuple[i])
#     i+=1

# # 扩展：
# test_tuple1=(1,) #(1)就不是元祖了
# test_tuple2=(2)
# print(type(test_tuple1))
# print(type(test_tuple2))

# # # ==============================================
# # 扩展：（后面讲字典遍历的时候会再提一下的）
# a=(1,2)
# b=a#把a的引用给b
# #a里面两个值,直接给左边两个变量赋值了（有点像拆包了）
# c,d=a #不是把a分别赋值给c和d，等价于：c=a[0] d=a[1]

# print(a)
# print(b)
# print(c)
# print(d)

# 扩展：多维元组
some_tuples=[(2,"萌萌哒"),(4,3)]
some_tuples[0]
some_tuples[0][1]
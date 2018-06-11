# 定义一个列表，列表虽然可以存不同类型，一般我们把相同类型的值存列表里面，不同类型存字典里（key，value）
infos_list=["C#","JavaScript"]#[]

# ###########################################################
# # 遍历 for while
# for item in infos_list:
#     print(item)

# i=0
# while i<len(infos_list):
#     print(infos_list[i])
#     i+=1
# ###########################################################
# # 增加
# # 末尾追加
# infos_list.append("Java")
# print(infos_list)

# # 指定位置插入
# infos_list.insert(0,"Python")
# print(infos_list)

# temp_list=["test1","test2"]
# infos_list.insert(0,temp_list)
# print(infos_list)

# # 添加一个列表
# infos_list2=["张三",21]#python里面的列表类似于List<object>
# infos_list.extend(infos_list2)
# print(infos_list)

# # help(infos_list.extend)#可以查看etend方法描述
# ###########################################################
# # 删除
# # pop()删除最后一个元素，返回删掉的元素
# # pop(index) 删除指定下标元素
# print(infos_list.pop())
# print(infos_list)
# print(infos_list.pop(0))
# # print(infos_list.pop(10)) #不存在就报错
# print(infos_list)

# # remove("")删除指定元素
# infos_list.remove("张三")
# # infos_list.remove("dnt") #不存在就报错
# print(infos_list)

# # del xxx[index] 删除指定下标元素
# del infos_list[1] #没有返回值
# print(infos_list)
# # del infos_list[10] #不存在就报错

# # del infos_list #删除集合（集合再访问就不存在了）
# ###########################################################
# # 修改 xxx[index]=xx
# # 注意：一般不推荐在for循环里面修改
# print(infos_list2)
# infos_list2[1]="PHP" #只有下标修改一种方式
# # infos_list2[3]="GO" #不存在则异常
# print(infos_list2)

# # 想按值修改需要先查下标再修改
# infos_list2.index("张三")
# infos_list2[0]="GO"
# print(infos_list2)
# # infos_list2.index("dnt")#不存在则异常

# # 知识面拓展： https://www.zhihu.com/question/49098374
# # 为什么python中不建议在for循环中修改列表？
# # 由于在遍历的过程中，删除了其中一个元素，导致后面的元素整体前移，导致有个元素成了漏网之鱼。
# # 同样的，在遍历过程中，使用插入操作，也会导致类似的错误。这也就是问题里说的无法“跟踪”元素。
# # 如果使用while，则可以在面对这样情况的时候灵活应对。

###########################################################
# # 查询 in, not in, index, count
# # # for扩展：https://www.cnblogs.com/dotnetcrazy/p/9102030.html#forelse

# names_list=["张三","李四","王二麻子"]

# # #张三在列表中执行操作
# if "张三" in names_list:
#     names_list.remove("张三")
# print(names_list)

# # #查看"大舅子"不在列表中执行操作
# if "大舅子" not in names_list:
#     names_list.append("大舅子")
# print(names_list)

# # #查询王二麻子的索引
# print(names_list.index("王二麻子"))

## 统计
# print(names_list.count("大舅子")) 
# print(names_list.count("逆天")) 
###########################################################
# # 排序(sort, reverse 逆置)
# num_list=[1,3,5,88,7]

# #倒序
# num_list.reverse()
# print(num_list)

# # 从小到大排序
# num_list.sort()
# print(num_list)

# # 从大到小
# num_list.sort(reverse=True)
# print(num_list)
# # ###########################################################

# # #列表嵌套(列表也是可以嵌套的)
# num_list2=[33,44,22]
# num_list.append(num_list2)
# print(num_list)
# # for item in num_list:
# #     print(item,end="")

# print(num_list[5])
# print(num_list[5][1])
# # ###########################################################

# # # 引入Null==>None
# # a=[1,2,3,4]
# # b=[5,6]
# # a=a.append(b)#a.append(b)没有返回值
# # print(a)#None

# range扩展～创建一个整数列表
# range(5)生成的序列是从0开始小于5的整数～[0,5)
# range(1,5)生成的序列是从1开始小于5的整数～[0,5)
range_list=list(range(1,5))
print(range_list)
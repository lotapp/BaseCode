# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，so，在set中，没有重复的值
# help(set)
#   #set(iterable) -> new set object #列表就比较合适了
my_set=set([1,2,1,"mmd"])
# 遍历 my_set
for item in my_set:
    print(item)
# 添加元素
my_set.add("add") #没有返回值
print(my_set)

# 删除元素
my_set.remove("mmd") #没有返回值
print(my_set)
# my_set.remove("mmd") #不存在则报错

#利用运算符+set 实现数学方面的扩展
set1=set([1,2,5])
set2=set([2,4,6])

#交集
print(set1 & set2)

#并集
print(set1 | set2)

# 其他内容可以直接查看help
# ----------------------------------

# test_str="www.baidu.com"
# test_list=[1,"d",5]
# test_dict={"name":"dnt","wechat":"xxx"}

# # # 运算符扩展：
# # test_list1=[2,4,"n","t",3]

# # # + 合并 (不支持字典)
# # print(test_str+test_str)
# # print(test_list+test_list1)

# # # * 复制 (不支持字典)
# # print(test_str*2)
# # print(test_list*2)

# # # in 是否存在（字典是查key）
# # print("d" in test_str)          #True
# # print("d" in test_list)         #True
# # print("d" in test_dict)         #False
# # print("name" in test_dict)      #True

# # # not in 是否不存在（字典是查key）
# # print("z" not in test_str)      #True
# # print("z" not in test_list)     #True
# # print("z" not in test_dict)     #True
# # print("name" not in test_dict)  #False


# # 先说说Python的内置函数
# # len(item)	        计算容器中元素个数

# len(test_str)
# len(test_list)
# len(test_dict)

# # max(item)	        返回容器中元素最大值
# max(test_str)
# test_list=[1,3,5,7,9,2]
# max(test_list) 
# max(test_dict) #比较key

# # min(item) 返回容器中元素最小值
# print(min(test_str))
# print(min(test_list))
# print(min(test_dict))

# # del(item)	        删除变量
# # del() or del xxx

# # 可以先忽略～cmp(item1, item2)	比较两个值 #Python2里面有 cmp(1,2) #-1 #cmp在比较字典数据时，先比较键，再比较值

infos_dict={"name":"dnt","web":"dkill.net"}

# # 遍历
# for item in infos_dict.keys():
#     print(item)

# #注意，如果你直接对infos遍历，其实只是遍历keys
# for item in infos_dict:
#     print(item)

# for item in infos_dict.values():
#     print(item)

# for item in infos_dict.items():
#     print("Key:%s,Value:%s"%(item[0],item[1]))
# #每一次相当于取一个元组，那可以用之前讲的例子来简化了：c,d=a #等价于：c=a[0] d=a[1]
# for k,v in infos_dict.items():
#     print("Key:%s,Value:%s"%(k,v))

# # 增加 修改 (有就修改，没就添加)
# # 添加
# infos_dict["wechat"]="lll"
# print(infos_dict)

# # 修改
# infos_dict["wechat"]="dotnetcrazy"
# print(infos_dict)

# # 删除
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
infos_dict.pop("wechat") #返回key对应的值
print(infos_dict)
# infos_dict.pop("wechat") #key不存在，则报错

# del infos_dict["name"]
# #del infos_dict["dog"] #不存在就报错
# print(infos_dict)

# #清空字典内容
# infos_dict.clear()
# print(infos_dict)

# # 删除字典
# del infos_dict

# 查询
infos_dict["name"]
# infos_dict["mmd"] #查不到就异常

# 要避免key不存在的错误，有两种办法
# 一是通过in判断key是否存在：
print("mmd" in infos_dict)

# 二是通过dict提供的get()方法
infos_dict.get("name")
print(infos_dict.get("mmd"))#如果key不存在，返回None
print(infos_dict.get("mmd",-1))#也可以返回自己指定的value

# 查看帮助
# help(infos_dict)
len(infos_dict) #有几对key,value 
# infos_dict.has_key("name") #这个是python2里面的

# 补充：dict内部存放的顺序和key放入的顺序是没有关系的
# dict的key必须是不可变对象（dict根据key进行hash算法,来计算value的存储位置
# 如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了）
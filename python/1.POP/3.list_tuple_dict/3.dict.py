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


infos_dict.get("name")
infos_dict.get("mmd")#查不到不会异常

# 查看帮助
# help(infos_dict)
len(infos_dict) #有几对key,value 
# infos_dict.has_key("name") #这个是python2里面的

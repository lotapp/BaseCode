# #输出+类型转换
# user_num1=input("输入第一个数：")
# user_num2=input("输入第二个数：")

# print("两数之和：%d"%(int(user_num1)+int(user_num2)))

# # ------------------------------------------------------------

# #字符串拼接
# user_name=input("输入昵称：")
# user_pass=input("输入密码：")
# user_url="192.168.1.121"

# #拼接输出方式一：
# print("ftp://"+user_name+":"+user_pass+"@"+user_url)

# #拼接输出方式二：
# print("ftp://%s:%s@%s"%(user_name,user_pass,user_url))

# # -------------------------------------------------------------

# # 字符串遍历、下标、切片
# user_str="七大姑曰：工作了吗？八大姨问：买房了吗？异性说：结婚了吗？"

# #遍历
# for item in user_str:
#     print(item,end=" ")

# #长度：len(user_str)
# print(len(user_str))

# #第一个元素：user_str[0]
# print(user_str[0])

# #最后一个元素：user_str[-1]
# print(user_str[-1])
# print(user_str[len(user_str)-1])#其他编程语言写法

# #倒数第二个元素：user_str[-2]
# print(user_str[-2])

# # -------------------------------------------------------------

# 切片:[start_index:end_index:step] （end_index取不到）
# eg:str[1:4] 取str[1]、str[2]、str[3]
# eg:str[2:] 取下标为2开始到最后的元素
# eg:str[2:-1] 取下标为2～到倒数第二个元素（end_index取不到）
# eg:str[1:6:2] 隔着取～str[1]、str[3]、str[5]（案例会详细说）
# eg:str[::-1] 逆向输出（案例会详细说，）

it_str="我爱编程，编程爱它，它是程序，程序是谁？"

#eg:取“编程爱它” it_str[5:9]
print(it_str[5:9])
print(it_str[5:-11]) #end_index用-xx也一样
print(it_str[-15:-11])#start_index用-xx也可以

#eg:取“编程爱它，它是程序，程序是谁？” it_str[5:]
print(it_str[5:])#不写默认取到最后一个

#eg:一个隔一个跳着取（"我编，程它它程，序谁"） it_str[0::2]
print(it_str[0::2])#step=△index（eg:0,1,2,3。这里的step=> 2-0 => 间隔1）

#eg:倒序输出 it_str[::-1]
# end_index不写默认是取到最后一个，是正取（从左往右）还是逆取（从右往左），就看step是正是负
print(it_str[::-1])
print(it_str[-1::-1])#等价于上一个

# # -------------------------------------------------------------

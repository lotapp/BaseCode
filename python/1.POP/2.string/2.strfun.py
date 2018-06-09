test_str="ABCDabcdefacddbdf"

# -------------------------------------------------------------

# # 查找:find,rfind,index,rindex
# # xxx.find(str, start, end)
# print(test_str.find("cd"))#从左往右
# print(test_str.rfind("cd"))#从右往左
# print(test_str.find("dnt"))#find和rfind找不到就返回-1

# # index和rindex用法和find一样，只是找不到会报错（以后用find系即可）
# print(test_str.index("dnt"))

# # -------------------------------------------------------------

# # 计数:count
# # xxx.count(str, start, end)
# print(test_str.count("d"))#4
# print(test_str.count("cd"))#2

# # -------------------------------------------------------------

# # 替换:replace
# # xxx.replace(str1, str2, count_num)
# print(test_str)
# print(test_str.replace("b","B"))#并没有改变原字符串，只是生成了一个新的字符串
# print(test_str)

# # replace可以指定替换几次
# print(test_str.replace("b","B",1))#ABCDaBcdefacddbdf

# # -------------------------------------------------------------

# 分割:split（按指定字符分割）,splitlines(按行分割),partition(以str分割成三部分,str前，str和str后),rpartition
# test_list=test_str.split("a")#a有两个，按照a分割，那么会分成三段，返回类型是列表（List），并且返回结果中没有a
# print(test_list)

# test_input="hi my name is dnt"
# print(test_input.split(" ")) #返回列表格式（后面会说）['hi', 'my', 'name', 'is', 'dnt']
# print(test_input.split(" ",3))#在第三个空格处切片，后面的不管了

# # 按行分割，返回类型为List
# test_line_str="abc\nbca\ncab\n"
# print(test_line_str.splitlines())#['abc', 'bca', 'cab']
# print(test_line_str.split("\n"))#看出区别了吧：['abc', 'bca', 'cab', '']

# # # 没看出来就再来个案例
# test_line_str2="abc\nbca\ncab\nLLL"
# print(test_line_str2.splitlines())#['abc', 'bca', 'cab', 'LLL']
# print(test_line_str2.split("\n"))#再提示一下，最后不是\n就和上面一样效果

# # 扩展：
# print("hi my name is dnt\t\n  m\n\t\n".split())#split()，默认按空字符切割(空格、\t、\n等等，不用担心返回'')

# #partition,返回是元祖类型（后面会说的）,方式和find一样，找到第一个匹配的就罢工了
# print(test_str.partition("cd"))#('ABCDab', 'cd', 'efacddbdf')
# print(test_str.rpartition("cd"))#('ABCDabcdefa', 'cd', 'dbdf')
# print(test_str.partition("感觉自己萌萌哒"))#没找到：('ABCDabcdefacddbdf', '', '')

# # -------------------------------------------------------------

# 连接：join
# separat.join(xxx)
# 错误用法：xxx.join("-")
# print("-".join(test_list))

# # -------------------------------------------------------------

# # 头尾判断:startswith（以。。。开头）,endswith（以。。。结尾）
# # test_str.startswith（以。。。开头）
# start_end_str="http://www.baidu.net"
# print(start_end_str.startswith("https://") or start_end_str.startswith("http://"))
# print(start_end_str.endswith(".com"))
# # -------------------------------------------------------------

# # 大小写系:lower(字符串转换为小写),upper(字符串转换为大写),title(单词首字母大写),capitalize(第一个字符大写，其他变小写)
# print(test_str)
# print(test_str.upper())#ABCDABCDEFACDDBDF
# print(test_str.lower())#abcdabcdefacddbdf
# print(test_str.capitalize())#第一个字符大写，其他变小写

# # -------------------------------------------------------------

# # 格式系列：lstrip（去除左边空格）,rstrip（去除右边空格）,strip（去除两边空格）,ljust,rjust,center
# strip_str=" I Have a Dream "
# print(strip_str.strip()+"|")#我加 | 是为了看清后面空格，没有别的用处
# print(strip_str.lstrip()+"|")
# print(strip_str.rstrip()+"|")

# #这个就是格式化输出，就不讲了
# print(test_str.ljust(50))
# print(test_str.rjust(50))
# print(test_str.center(50))
# # -------------------------------------------------------------

# 验证系列:isalpha（是否是纯字母）,isalnum（是否是数字|字母）,isdigit（是否是纯数字）,isspace（是否是纯空格）

# test_str2="Abcd123"
# test_str3="123456"
# test_str4="  \t"
# test_str5="  \t \n " #isspace() ==>true
# 一张图搞定，其他的自己去试一试吧
# test_str.isalpha()
# test_str.isalnum()
# test_str.isdigit()
# test_str.isspace()
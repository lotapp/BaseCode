import time

# # 时间戳，结果是float类型
# print(time.time())

# # 格式化的时间字符串：年-月-日 小时:分钟:秒
# print(time.strftime("%Y-%m-%d %X"))

# print(time.localtime())  # 本地时区的 struct_time
# print(time.gmtime())  # UTC时区（世界标准时间）的struct_time

# # time.mktime 将一个 struct_time 转化为时间戳
# print(time.mktime(time.localtime()))

# t = time.localtime()
# print(time.asctime(t)) # 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'
# print(time.asctime()) # 不写参数默认就是time.localtime()

# ---

# 时间加减
import datetime

# print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2018-07-03
print(datetime.datetime.now())  # 当前时间 2018-07-03 12:47:03.941925
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分

#
c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))  #时间替换

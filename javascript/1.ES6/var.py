# if 1 < 2:
#     b = 1
# print(b)
# ---------------------------------
# age = 20
# def test():
#     global age
#     print(age)
# test()
# ---------------------------------
# ---------------------------------
# def show(a, b, *args, c):
#     print(a, b, args, c)
#
# # 1 2 (4, 5, 6) 3
# show(1, 2, 4, 5, 6, c=3)
# ---------------------------------
# ---------------------------------
# nums = (1, 2, 3, 4)
# nums2 = (0, *nums, 5, 6)
# print(nums2) # (0, 1, 2, 3, 4, 5, 6)
# ---------------------------------
# num_list = [1,2,3,4]
# num_list2 = [0,*num_list,5,6]
# # [0, 1, 2, 3, 4, 5, 6]
# print(num_list2)
# ---------------------------------
# num_list = [1,2,3,4]
# num_list2 = [0,5,6]
# # [1, 2, 3, 4, 0, 5, 6]
# num_list.extend(num_list2)
# # # [1, 2, 3, 4, [0, 5, 6]]
# # num_list.append(num_list2)
# print(num_list)
# ---------------------------------
# ---------------------------------
# scor_list = [100, 28, 38, 64]
# result_list = map(lambda item: item >= 60, scor_list)
# # [True, False, False, True]
# print(list(result_list)) # 不改变scor_list内容，生成新数组
# print(scor_list)
# ---------------------------------
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums2 = filter(lambda item: item % 2 == 0, nums)
# # [2, 4, 6, 8, 10]
# print(list(nums2)) # nums2：PY2返回的是列表
# ---------------------------------
# import functools
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = functools.reduce(lambda x, y: print(x, y), nums)
# print(result)
# # 1 2
# # None 3
# # None 4
# # None 5
# # None 6
# # None 7
# # None 8
# # None 9
# # None 10
# # None
# ---------------------------------
# import functools
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = functools.reduce(lambda x, y: x + y, nums)
# print(result / len(nums))  # 5.5
# ---------------------------------
# import functools
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = functools.reduce(avg, nums)
# print(result)
# ---------------------------------
# 字符串
# name, age = "小明", 23
# # 我叫小明,今年23
# print(f"我叫{name},今年{age}")
# print("""我叫：
# 小明
# 今年：
# 23
# """)
# ---------------------------------
# url = "https://www.baidu.com"
# if url.startswith("https://") or url.startswith("http://"):
#     print("B/S")
# if url.endswith(".com"):
#     print(".com")
# ---------------------------------
# ---------------------------------
# OOP
# class People(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"我叫：{self.name}，今年：{self.age}")

#     @classmethod
#     def hello(cls):
#         print("Hello World!")

# xiaoming = People("小明", 23)
# xiaoming.show()  # 我叫：小明，今年：23
# # 这个虽然可以访问到，但我一直都不建议这么用（不然用其他语言会混乱崩溃的）
# xiaoming.hello()  # Hello World!
# People.hello()  # Hello World!
# ---------------------------------
# class Teacher(People):
#     def __init__(self, name, age, work):
#         self.work = work
#         super().__init__(name, age)

#     def show_job(self):
#         print(f"我是做{self.work}工作的")

# xiaozhang = Teacher("小张", 25, "思想教育")
# xiaozhang.show()  # 我叫：小张，今年：25
# xiaozhang.show_job()  # 我是做思想教育工作的
# Teacher.hello()  # Hello World!
# ---------------------------------
# class Animal(object):
#     def __init__(self, name):
#         self.name = name

#     def run(self):
#         print(f"{self.name}会跑")

# class Dog(Animal):
#     def run(self):
#         print(f"{self.name}会飞快的跑着")

# # 借助一个方法来实现多态
# def run(obj):
#     obj.run()

# run(Animal("动物"))  # 动物会跑
# run(Dog("小狗"))  # 小狗会飞快的跑着
# ---------------------------------
# def show():
#     yield "1"
#     yield "2"
#     return "d"

# gen = show()

# while True:
#     try:
#         print(next(gen))
#     except StopIteration as ex:
#         print(f"返回值：{ex.value}")
#         break

# for item in show():
#     print(item)  # 1 2
# ---------------------------------
# def show():
#     a = yield "111"
#     print(a)
#     b = yield a
#     print(b)
#     c = yield b
#     print(c)
#     return "over"

# gen = show()
# # 第一个不传参
# print(next(gen))  # gen.send(None)
# print(gen.send("aaa"))
# print(gen.send("bbb"))
# try:
#     print(gen.send("ccc"))
# except StopIteration as ex:
#     print(ex.value)
# ---------------------------------
# import asyncio

# # 模拟一个异步操作
# async def show():
#     await asyncio.sleep(1)
#     return "写完文章早点睡觉哈~"

# # 定义一个异步方法
# async def test(msg):
#     print(msg)
#     return await show()

# # Python >= 3.7
# result = asyncio.run(test("这是一个测试"))
# print(result)

# # Python >= 3.4
# # loop = asyncio.get_event_loop()
# # result = loop.run_until_complete(test("这是一个测试"))
# # print(result)
# # loop.close()
# ---------------------------------
# ---------------------------------
# user = {"name": "dnt", "age": 25, "wechat": "dotnetcrazy"}

# for key in user.keys():
#     print(key)  # name age wechat

# for value in user.values():
#     print(value)  # dnt 25 dotnetcrazy

# for key, value in user.items():
#     print(key, value)  # name dnt  age 25  wechat dotnetcrazy
# ---------------------------------
# ---------------------------------
# 格式系列：lstrip（去除左边空格）,rstrip（去除右边空格）,strip（去除两边空格）美化输出系列：ljust,rjust,center
strip_str = " I Have a Dream "
print("["+strip_str.strip()+"]")
print("["+strip_str.lstrip()+"]")
print("["+strip_str.rstrip()+"]")

test_str = "ABCDabcdefacddbdf"
print("["+test_str.ljust(50)+"]")
print("["+test_str.rjust(50)+"]")
print("["+test_str.center(50)+"]")

# 输出：
# [I Have a Dream]
# [I Have a Dream ]
# [ I Have a Dream]
# [ABCDabcdefacddbdf                                 ]
# [                                 ABCDabcdefacddbdf]
# [                ABCDabcdefacddbdf                 ]

# ---------------------------------

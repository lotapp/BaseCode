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
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------

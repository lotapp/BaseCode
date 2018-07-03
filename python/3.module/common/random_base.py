import random

# print(random.random())  # 大于0且小于1之间的小数

# print(random.randint(1, 3))  # [1,3]    大于等于1且小于等于3之间的整数

# print(random.randrange(1, 3))  # [1,3)    大于等于1且小于3之间的整数

# print(random.choice([4, 'a', [1, 2]]))  # 随机返回三者之一

# # 从list中随机获取N个元素，作为一个片断返回
# old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = random.sample(old_list, 5)  # 从list中随机获取5个元素，作为一个片断返回
# print(old_list)
# print(new_list)  # 原有序列并没有改变

# print(random.uniform(1, 3))  # 大于1小于3的小数，如1.927109612082716

# test_list = [1, 3, 5, 7, 9]
# random.shuffle(test_list)  # 打乱test_list的顺序
# print(test_list)
# 编译器推荐多行导入
# import test1, test2

# print(test1.test_str)

# print(test2.test_str)

# test1.show()

# test2.show()

from test1 import show as show1, test_str as test_str1
from test2 import show as show2, test_str as test_str2

print(test_str1)
print(test_str2)

show1()
show2()


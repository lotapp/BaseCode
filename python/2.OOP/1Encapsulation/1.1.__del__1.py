from my_temp import Temp

# 对象被s1和s2引用
s1 = Temp()
s2 = s1

del s1  # 只删除s1，新创建的对象并没有被删除
print("-" * 10)

# ----------
# 你被干掉了 ==> 程序退出了
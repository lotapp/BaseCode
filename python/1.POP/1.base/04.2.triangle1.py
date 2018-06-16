i = 1
# 输出一个三角形
while i < 6:
    j = 1
    while j <= i:
        print("*", end="")  # 不换行输出
        j += 1
    print("")  # 下一行
    i += 1

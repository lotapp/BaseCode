class Student:
    def __del__(slef):
        print("你被干掉了")

s1=Student()
s2=s1

del s1
print("-"*10)

# ----------
# 你被干掉了
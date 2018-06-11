# python里面都是传引用，来验证一下
def update_value(a,b):
    a=a+1
    b+=1

num1=1
num2=2
update_value(num1,num2)
print(num1,num2)
#while循环一般通过数值是否满足来确定循环的条件
#for循环一般是对能保存多个数据的变量，进行遍历
name="https://pan.baidu.com/s/1weaF2DGsgDzAcniRzNqfyQ#mmd"

for i in name:
    if i=='#':
        break
    print(i,end='')#另一种写法：print("%s"%i,end="")
print('\n end ...')

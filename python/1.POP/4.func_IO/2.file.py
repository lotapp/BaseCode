import os

file=open("1.txt","w")
file.write("mmd\rmmd\rdnt")
file.close()

f=open("1.txt","r")
lines=f.readlines()
f.close()
print(lines)
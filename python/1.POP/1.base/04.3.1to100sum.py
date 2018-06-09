i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)

# why not have ++ ?
a=5
b=5

print(id(a))
print(id(b))
print(a is b)
a+=1

print(id(a))
print(id(b))
print(a is b)

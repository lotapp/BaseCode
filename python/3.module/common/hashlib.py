# https://docs.python.org/3/library/hashlib.html
import hashlib

pass_str = "123456"

# m = hashlib.sha256()

# m.update(pass_str.encode("utf-8"))

# pass_str_new = m.hexdigest()

# print(pass_str_new)
# print(len(pass_str_new))

# 简写
# hashlib.sha256(pass_str.encode("utf-8")).hexdigest()

# 简写这么方便为什么要像上面例子那么复杂呢？
m = hashlib.sha256()

m.update(pass_str.encode("utf-8"))

m.update("你设置的key".encode("utf-8"))

pass_str_new = m.hexdigest()

print(pass_str_new)
print(len(pass_str_new))

# python 还有一个`hmac`模块，它内部对我们创建`key`和`pass`进行处理后再加密
# https://docs.python.org/3/library/hmac.html
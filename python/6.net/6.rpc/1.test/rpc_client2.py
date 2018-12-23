import zerorpc

client = zerorpc.Client("tcp://192.168.36.144:5438")
# 这时候的Client，就是当时注册进去的对象
result = client.say_hi("RPC")
print(result)
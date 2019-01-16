import zerorpc

client = zerorpc.Client("tcp://192.168.36.144:5438")
result = client.say_hi("RPC")
print(result)
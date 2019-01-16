from xmlrpc.client import ServerProxy

server = ServerProxy("http://192.168.36.123:50051")
result = server.sum(1, 2)
print(f"1+2={result}")

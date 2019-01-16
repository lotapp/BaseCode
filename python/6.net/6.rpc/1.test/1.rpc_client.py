from xmlrpc.client import ServerProxy

stub = ServerProxy("http://192.168.36.123:50051")
result = stub.sum(1, 2)
print(f"1+2={result}")

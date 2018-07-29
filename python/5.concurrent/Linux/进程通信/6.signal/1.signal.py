import mmap

b = "mmd\0".encode()
print(b.translate(None, "\0".encode()).decode())

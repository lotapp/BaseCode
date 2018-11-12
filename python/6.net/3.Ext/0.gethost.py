import socket

if __name__ == "__main__":
    with socket.socket() as tcp_socket:
        host = "cnblogs.com"
        ip = socket.gethostbyname(host)
        print(f"Host：{host}，IP：{ip}")

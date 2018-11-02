from socket import socket
from multiprocessing.dummy import Pool


def wait_client(client_socket, ip_port):
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            print(f"[来自{ip_port}的消息]:\n{data.decode('utf-8')}")
            client_socket.send(b"I Know")  # bytes类型


def main():
    with socket() as tcp_socket:
        # 绑定端口
        tcp_socket.bind(('', 8080))
        # 服务器监听
        tcp_socket.listen()

        print("TCP Server is Running...")  # 运行后提示

        p = Pool()
        while True:
            # 等待客户端连接
            client_socket, client_addr = tcp_socket.accept()
            ip_port = f"{client_addr[0]}:{client_addr[1]}"
            print(f"客户端{ip_port}已连接")
            # 响应多个客户端则需要多个线程来处理
            p.apply_async(wait_client, args=(client_socket, ip_port))


if __name__ == '__main__':
    main()

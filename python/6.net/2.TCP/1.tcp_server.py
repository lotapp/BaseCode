from socket import socket


def main():
    with socket() as tcp_socket:
        # 绑定端口（便于客户端找到）
        tcp_socket.bind(('', 8080))
        # 变成被动接收消息（监听）
        tcp_socket.listen()  # 不指定连接最大数则会设置默认值

        print("TCP Server is Running...")  # 运行后提示

        # 等待客户端发信息
        client_socket, client_addr = tcp_socket.accept()

        with client_socket:
            # 客户端连接提示
            print(f"[来自{client_addr[0]}:{client_addr[1]}的消息]\n")

            # 接收客户端消息
            data = client_socket.recv(1024)
            print(data.decode("utf-8"))

            # 回复客户端
            client_socket.send("知道了".encode("utf-8"))


if __name__ == '__main__':
    main()

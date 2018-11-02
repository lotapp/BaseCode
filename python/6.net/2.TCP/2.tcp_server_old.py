from socket import socket


def main():
    with socket() as tcp_socket:
        # 服务端绑定端口
        tcp_socket.bind(('', 8080))
        # 服务端监听
        tcp_socket.listen()

        print("TCP Server is Running...")  # 运行后提示

        while True:
            # 服务端等待客户端
            client_socket, client_addr = tcp_socket.accept()
            # 客户端连接后提示
            print(f"[来自{client_addr[0]}:{client_addr[1]}的消息：]")
            with client_socket:
                # 接收客户端发来的消息
                data = client_socket.recv(1024)
                print(data.decode("utf-8"))
                # 发消息给客户端
                client_socket.send(b"I Kown")


if __name__ == '__main__':
    main()

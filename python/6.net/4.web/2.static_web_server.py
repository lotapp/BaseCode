from socket import socket, SOL_SOCKET, SO_REUSEADDR


def main():
    with socket() as tcp_socket:
        # 防止端口占用
        tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定端口
        tcp_socket.bind(('', 8080))
        # 监听
        tcp_socket.listen()
        # 等待客户端连接
        client_socket, client_addr = tcp_socket.accept()
        with client_socket:
            print(f"[来自{client_addr}的消息：")
            # while True:
            data = client_socket.recv(2048)
            if data:
                print(data.decode("utf-8"))
            client_socket.send(
                b"HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n"
            )


if __name__ == "__main__":
    main()

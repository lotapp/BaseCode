from socket import socket, SOL_SOCKET, SO_REUSEADDR


def main():
    with socket() as tcp_socket:
        # 防止端口占用
        tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定端口
        tcp_socket.bind(('', 8080))
        # 监听
        tcp_socket.listen()
        # 等待
        client_socket, address = tcp_socket.accept()
        # 收发消息
        with client_socket:
            print(f"[来自{address}的消息：\n")
            msg = client_socket.recv(2048)
            if msg:
                print(msg.decode("utf-8"))
            client_socket.send(
                """HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n<h1>哈哈哈</h1>"""
                .encode("utf-8"))


if __name__ == "__main__":
    main()

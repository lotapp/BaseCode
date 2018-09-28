import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.bind(("", 5438))  # 绑定本地端口
        tcp_socket.listen(4)  # 使服务器接受连接，3.5后可以不填
        new_socket, address = tcp_socket.accept()
        with new_socket:
            while True:
                data = new_socket.recv(1024)
                if len(data):
                    print(f"[{address}]{data}")
                else:
                    break
                # 发消息给客户端
                new_socket.send(input("输入回复").encode())


if __name__ == '__main__':
    main()

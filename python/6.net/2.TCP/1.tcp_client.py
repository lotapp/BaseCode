from socket import socket


def main():
    # 默认就是创建TCP Socket
    with socket() as tcp_socket:
        # 连接服务器（没有返回值）
        tcp_socket.connect(("127.0.0.1", 8080))

        print("Connected TCP Server...")  # 连接提示

        # 发送消息（返回发送的字节数）
        tcp_socket.send("小张生日快乐～\n".encode("utf-8"))
        # 接收消息
        msg = tcp_socket.recv(1024)
        print(f"服务器：{msg.decode('utf-8')}")


if __name__ == '__main__':
    main()

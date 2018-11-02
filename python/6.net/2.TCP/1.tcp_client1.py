from socket import socket


def get_buffer(tcp_socket):
    buffer_list = []
    while True:
        b = tcp_socket.recv(1024)
        if b:
            buffer_list.append(b)
        else:
            break
    # 拼接在一起
    return b''.join(buffer_list)


def main():
    with socket() as tcp_socket:
        # 连接服务器
        tcp_socket.connect(("dotnetcrazy.cnblogs.com", 80))
        # 发送消息（模拟HTTP，\r\n和Connection:close很重要）
        tcp_socket.send(
            b'GET / HTTP/1.1\r\nHost: dotnetcrazy.cnblogs.com\r\nConnection: close\r\n\r\n'
        )
        # 以"\r\n\r\n"分割一次
        header, data = get_buffer(tcp_socket).split(b"\r\n\r\n", 1)
        print(header.decode("utf-8"))
        with open("test.html", "wb") as f:
            f.write(data)
    print("over")


if __name__ == '__main__':
    main()

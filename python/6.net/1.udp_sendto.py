import socket


def main():

    # AF_INET ==> IPV4 SOCK_STREAM ==> 类型是TCP，stream 流
    # SOCK_DGRAM ==> 类型是UDP，dgram 数据报、数据报套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
        udp_sock.sendto("大兄弟，你好啊".encode("utf-8"), ("192.168.36.235", 8080))

    print("over")
    # 创建 udp_sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送 udp_sock.sendto(内容，(IP,Port))
    # 关闭 udp_sock.close()


if __name__ == '__main__':
    main()

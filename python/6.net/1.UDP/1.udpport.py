import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        # 绑定固定端口
        udp_socket.bind(('', 5400))
        # 发送消息
        udp_socket.sendto("小明，你知道小张的生日吗？\n".encode("utf-8"),
                          ("192.168.36.235", 8080))
    print("over")


if __name__ == '__main__':
    main()
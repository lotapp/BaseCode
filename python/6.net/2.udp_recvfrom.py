from socket import socket, AF_INET, SOCK_DGRAM


def main():
    with socket(AF_INET, SOCK_DGRAM) as udp_socket:
        # 绑定端口
        udp_socket.bind(('', 5400))
        while True:
            udp_socket.sendto("你可以给我离线留言了\n".encode("utf-8"),
                              ("192.168.36.235", 8080))
            data, info = udp_socket.recvfrom(1024)
            print(f"[来自{info[0]}:{info[1]}的消息]：\n{data.decode('utf-8')}")


if __name__ == '__main__':
    main()

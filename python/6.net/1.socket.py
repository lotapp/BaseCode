import socket


def main():
    # socket.AF_INET ==> IP V4
    # socket.socket()  # 默认使用IP V4 和 TCP
    # TCP：socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # UDP：socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as udp_socket:
        udp_socket.sendto(input("输入内容：").encode(), ("192.168.36.235", 5438))
    print("over")


if __name__ == '__main__':
    main()
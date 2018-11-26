from socket import socket, AF_INET, SOCK_DGRAM


def main():
    with socket(AF_INET, SOCK_DGRAM) as udp_socket:
        udp_socket.sendto("小明，今晚去喝碗羊肉汤？".encode("utf-8"), ('', 8080))
        data, addr = udp_socket.recvfrom(1024)
        print(f"[来自{addr}的消息：]\n")
        if data:
            print(data.decode("utf-8"))


if __name__ == "__main__":
    main()

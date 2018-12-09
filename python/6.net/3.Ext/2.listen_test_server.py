import socket


def main():
    with socket.socket() as tcp_server:
        # 防止端口占用
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind(('', 8080))
        tcp_server.listen()
        while True:
            client_socket, client_addr = tcp_server.accept()
            print(client_addr)
            print(client_socket.recv(2048))


if __name__ == "__main__":
    main()

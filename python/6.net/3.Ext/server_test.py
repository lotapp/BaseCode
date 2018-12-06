import socket


def main():
    with socket.socket() as tcp_socket:
        tcp_socket.bind(('', 8080))
        tcp_socket.listen()
        while True:
            client_socket, client_address = tcp_socket.accept()
            print(f"[来自{client_address}的连接]")
            with client_socket:
                data = client_socket.recv(1024)
                print(data)
                client_socket.send(
                    "HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n<h1>小明，晚上吃羊肉汤吗？</h1>"
                    .encode("utf-8"))


if __name__ == "__main__":
    main()

import socket
import select


def main():
    with socket.socket() as tcp_server:
        # epoll是linux独有的
        select.epoll()


if __name__ == "__main__":
    main()

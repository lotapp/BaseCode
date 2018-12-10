import socket
import select


def main():
    with socket.socket() as tcp_server:
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind(('', 8080))
        tcp_server.listen()

        # epoll是linux独有的
        epoll = select.epoll()
        # tcp_server注册到epoll中
        epoll.register(tcp_server.fileno(), select.EPOLLIN | select.EPOLLET)

        # key-value
        fd_socket_dict = dict()

        # 回调需要自己处理
        while True:
            # 返回可读写的socket fd 集合
            poll_list = epoll.poll()
            for fd, event in poll_list:
                # 服务器的socket
                if fd == tcp_server.fileno():
                    client_socket, client_addr = tcp_server.accept()
                    fd = client_socket.fileno()
                    fd_socket_dict[fd] = (client_socket, client_addr)
                    # 把客户端注册进epoll中
                    epoll.register(fd, select.EPOLLIN | select.EPOLLET)
                else:  # 客户端
                    client_socket, client_addr = fd_socket_dict[fd]
                    data = client_socket.recv(2048)
                    print(
                        f"[来自{client_addr}的消息，当前连接数：{len(fd_socket_dict)}]\n")
                    if data:
                        print(data.decode("utf-8"))
                        client_socket.send(
                            b"HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n<h1>Web Server Test</h1>"
                        )
                    else:
                        del fd_socket_dict[fd]
                        print(
                            f"[{client_addr}已离线，当前连接数：{len(fd_socket_dict)}]\n"
                        )
                        # 从epoll中注销
                        epoll.unregister(fd)
                        client_socket.close()


if __name__ == "__main__":
    main()

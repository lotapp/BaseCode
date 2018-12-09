import time
import socket


def select(socket_addr_list):
    for client_socket, client_addr in socket_addr_list:
        try:
            data = client_socket.recv(2048)
            if data:
                print(f"[来自{client_addr}的消息：]\n")
                print(data.decode("utf-8"))
                # 等会压测用
                client_socket.send(
                    b"HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n<h1>Web Server Test</h1>"
                )
            else:
                # 没有消息是触发异常，空消息是断开连接
                client_socket.close()  # 关闭客户端连接
                socket_addr_list.remove((client_socket, client_addr))
                print(f"[客户端{client_addr}已断开连接，当前连接数：{len(socket_addr_list)}]")
        except Exception:
            pass


def main():
    # 存放客户端集合
    socket_addr_list = list()

    with socket.socket() as tcp_server:
        # 防止端口绑定的设置
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind(('', 8080))
        tcp_server.listen()
        tcp_server.setblocking(False)  # 服务端非阻塞
        while True:
            try:
                client_socket, client_addr = tcp_server.accept()
                client_socket.setblocking(False)  # 客户端非阻塞
                socket_addr_list.append((client_socket, client_addr))
            except Exception:
                pass
            else:
                print(f"[来自{client_addr}的连接，当前连接数：{len(socket_addr_list)}]")
            # 防止客户端断开后出错
            if socket_addr_list:
                # 轮询查看客户端有没有消息
                select(socket_addr_list)  # 引用传参
                time.sleep(0.01)


if __name__ == "__main__":
    main()

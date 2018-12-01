import time
import socket


def select(socket_addr_dict):
    for client_socket, client_addr in socket_addr_dict.items():
        try:
            data = client_socket.recv(2048)
            if data:
                print(f"[来自{client_addr}的消息：]\n")
                print(data.decode("utf-8"))
        except Exception:
            pass


def main():
    # 存放客户端集合
    socket_addr_dict = dict()

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
                socket_addr_dict[client_socket] = client_addr
            except Exception:
                pass
            # 轮询查看客户端有没有消息
            select(socket_addr_dict)
            time.sleep(0.01)


if __name__ == "__main__":
    main()

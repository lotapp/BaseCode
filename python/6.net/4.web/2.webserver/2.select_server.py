import select
import socket


def main():
    with socket.socket() as tcp_server:
        tcp_server.bind(('', 8080))
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.listen()
        socket_info_dict = dict()
        socket_list = [tcp_server]  # 监测列表
        while True:
            # 劣势：select列表数量有限制
            read_list, write_list, error_list = select.select(
                socket_list, [], [])
            for item in read_list:
                # 服务端迎接新的连接
                if item == tcp_server:
                    client_socket, client_address = item.accept()
                    socket_list.append(client_socket)
                    socket_info_dict[client_socket] = client_address
                    print(f"[{client_address}已连接，当前连接数：{len(socket_list)-1}]")
                # 客户端发来
                else:
                    data = item.recv(2048)
                    if data:
                        print(data.decode("utf-8"))
                        item.send(b"ok")
                    else:
                        item.close()
                        socket_list.remove(item)
                        info = socket_info_dict[item]
                        print(f"[{info}已断开，当前连接数：{len(socket_list)-1}]")


if __name__ == "__main__":
    main()

from socket import socket, AF_INET, SOCK_DGRAM
from multiprocessing.dummy import Pool as ThreadPool


def get_port(msg):
    """获取用户输入的端口号"""
    while True:
        port = input(msg)
        try:
            port = int(port)
        except Exception as ex:
            print(ex)
        else:
            return port  # 没有错误就退出死循环


def recv_msg(udp_socket):
    """接收消息"""
    while True:
        data, info = udp_socket.recvfrom(1024)
        print(f"[来自{info[0]}:{info[1]}的消息]：\n{data.decode('utf-8')}")


def send_msg(udp_socket):
    """发送消息"""
    ip = input("请输入对方IP：")
    port = get_port("请输入对方端口号：")
    while True:
        msg = input("请输入发送的消息：\n")
        udp_socket.sendto(msg.encode("utf-8"), (ip, port))


def main():

    with socket(AF_INET, SOCK_DGRAM) as udp_socket:
        # 绑定端口
        udp_socket.bind(('', get_port("请输网络助手的端口号：")))
        # 创建一个线程池
        pool = ThreadPool()
        # 接收消息
        pool.apply_async(recv_msg, args=(udp_socket, ))
        # 发送消息
        pool.apply_async(send_msg, args=(udp_socket, ))

        pool.close()
        pool.join()


if __name__ == '__main__':
    main()

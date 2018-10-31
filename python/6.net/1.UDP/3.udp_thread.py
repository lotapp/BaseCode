from socket import socket, AF_INET, SOCK_DGRAM
from multiprocessing.dummy import Pool as ThreadPool


def send_msg(udp_socket):
    while True:
        msg = input("输入需要发送的消息：\n")
        udp_socket.sendto(msg.encode("utf-8"), ("192.168.36.235", 8080))


def recv_msg(udp_socket):
    while True:
        data, info = udp_socket.recvfrom(1024)
        print(f"[来自{info[0]}:{info[1]}的消息]：\n{data.decode('utf-8')}")


def main():
    # 创建一个Socket
    with socket(AF_INET, SOCK_DGRAM) as udp_socket:
        # 绑定端口
        udp_socket.bind(('', 5400))

        # 创建一个线程池
        pool = ThreadPool()

        # 接收消息
        pool.apply_async(recv_msg, args=(udp_socket, ))

        # 发送消息
        pool.apply_async(send_msg, args=(udp_socket, ))

        pool.close()  # 不再添加任务
        pool.join()  # 等待线程池执行完毕
    print("over")


if __name__ == '__main__':
    main()

from socket import socket
from multiprocessing.dummy import Pool

ip = "127.0.0.1"


def tcp_port(port):
    """IP：服务端IP，Port：服务端Port"""
    with socket() as tcp_socket:
        try:
            tcp_socket.connect((ip, port))
            print(f"[TCP Port:{port} is open]")
        except Exception:
            pass


def main():
    # 查看系统本地可用端口极限值 cat /proc/sys/net/ipv4/ip_local_port_range
    max_port = 60999
    global ip
    ip = input("请输入要扫描的IP地址：")
    print(f"正在对IP：{ip}进行端口扫描...")

    pool = Pool()
    pool.map_async(tcp_port, range(max_port))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

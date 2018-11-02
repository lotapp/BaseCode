from time import sleep
from socket import socket
from multiprocessing.dummy import Pool


def send_msg(tcp_socket):
    with tcp_socket:
        while True:
            try:
                tcp_socket.send("小明同志\n".encode("utf-8"))
                sleep(2)  # send是非阻塞的
                print("向服务器问候了一下")
            except Exception as ex:
                print("服务端连接已断开:", ex)
                break


def recv_msg(tcp_socket):
    with tcp_socket:
        while True:
            # 这边可以不捕获异常：
            #    服务端关闭时，send_msg会关闭，然后这边也就关闭了
            try:
                data = tcp_socket.recv(1024)
                if data:
                    print("服务端回复：", data.decode("utf-8"))
            except Exception as ex:
                print("tcp_socket已断开:", ex)
                break


def main():
    with socket() as tcp_socket:
        # 连接TCP Server
        tcp_socket.connect(("192.168.36.235", 8080))
        print("Connected TCP Server...")  # 连接提示

        pool = Pool()
        pool.apply_async(send_msg, args=(tcp_socket,))
        pool.apply_async(recv_msg, args=(tcp_socket,))
        pool.close()
        pool.join()


if __name__ == '__main__':
    main()

import socket
import selectors

# Linux下使用epoll，Win下使用select
Selector = selectors.DefaultSelector()


class Task(object):
    def __init__(self):
        # 存放客户端fd和socket键值对
        self.fd_socket_dict = dict()

    def run(self):
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('', 8080))
        self.server.listen()
        # 把Server注册到epoll
        Selector.register(self.server.fileno(), Selector._EVENT_READ,
                          self.connected)

    def connected(self, key):
        """客户端连接时处理"""
        client_socket, client_address = self.server.accept()
        fd = client_socket.fileno()
        self.fd_socket_dict[fd] = (client_socket, client_address)
        # 注册一个客户端读的事件（服务端去读消息）
        Selector.register(fd, selectors.EVENT_READ, self.call_back_reads)
        print(f"{client_address}已连接，当前连接数：{len(self.fd_socket_dict)}")

    def call_back_reads(self, key):
        """客户端可读时处理"""
        # 一个fd只能注册一次，监测可写的时候需要把可读给注销
        Selector.unregister(key.fd)
        client_socket, client_address = self.fd_socket_dict[key.fd]
        print(f"[来自{client_address}的消息:]\n")
        data = client_socket.recv(2048)
        if data:
            print(data.decode("utf-8"))
            # 注册一个客户端写的事件（服务端去发消息）
            Selector.register(key.fd, selectors.EVENT_WRITE,
                              self.call_back_writes)
        else:
            client_socket.close()
            del self.fd_socket_dict[key.fd]
            print(f"{client_address}已断开，当前连接数：{len(self.fd_socket_dict)}")

    def call_back_writes(self, key):
        """客户端可写时处理"""
        Selector.unregister(key.fd)
        client_socket, client_address = self.fd_socket_dict[key.fd]
        client_socket.send(b"ok")
        Selector.register(key.fd, selectors.EVENT_READ, self.call_back_reads)


def main():
    t = Task()
    t.run()
    while True:
        ready = Selector.select()
        for key, obj in ready:
            # 需要自己回调
            call_back = key.data
            call_back(key)


if __name__ == "__main__":
    main()

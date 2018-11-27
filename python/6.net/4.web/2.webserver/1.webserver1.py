from socket import socket, SOL_SOCKET, SO_REUSEADDR


class WebServer(object):
    def __init__(self):
        with socket() as tcp_socket:
            # 保存变量
            self.tcp_socket = tcp_socket
            # 防止端口占用
            tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            # 绑定端口
            tcp_socket.bind(('', 8080))
            # 监听
            tcp_socket.listen()
            # 等待客户端连接
            while True:
                self.client_socket, self.client_addr = self.tcp_socket.accept()
                self.handle()

    def handle(self):
        with self.client_socket:
            print(f"[来自{self.client_addr}的消息：")
            data = self.client_socket.recv(2048)
            if data:
                print(data.decode("utf-8"))
                self.client_socket.send(
                    b"HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf-8\r\n\r\n<h1>Web Server Test</h1>"
                )


if __name__ == "__main__":
    WebServer()

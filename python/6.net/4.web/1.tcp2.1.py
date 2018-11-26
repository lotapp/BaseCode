import socket
from socketserver import TCPServer, StreamRequestHandler


class MyHandler(StreamRequestHandler):
    # 可选设置（下面的是默认值）
    timeout = 5  # 所有socket超时时间
    rbufsize = -1  # 读缓冲区大小
    wbufsize = 0  # 写缓冲区大小
    disable_nagle_algorithm = False  # 设置TCP无延迟选项

    def handle(self):
        print(f"[来自{self.client_address}的消息：]\n")
        # 接受来自客户端的IO流(类似于打开IO，等待对方写)
        try:
            for line in self.rfile:  # 阻塞等
                print(f"接受到的数据：{line}")
                # 发送给客户端（类似于写给对方）
                self.wfile.write(line)
        except socket.timeout as ex:
            print("---" * 10, "网络超时", "---" * 10)
            print(ex)
            print("---" * 10, "网络超时", "---" * 10)


def main():
    with TCPServer(('', 8080), MyHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()

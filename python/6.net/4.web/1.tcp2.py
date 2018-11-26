from time import sleep
from socketserver import TCPServer, StreamRequestHandler


# `SocketServer.StreamRequestHandler`中对客户端发过来的数据是用`rfile`属性来处理的
# `rfile`是一个`类file对象`.有缓冲.可以按行分次读取;发往客户端的数据通过`wfile`属性来处理
# `wfile`不缓冲数据,对客户端发送的数据需一次性写入
class MyHandler(StreamRequestHandler):
    def handle(self):
        print(f"[来自{self.client_address}的消息：]\n")
        # 接受来自客户端的IO流( 类似于打开IO，等待对方写)
        # self.rfile = self.request.makefile('rb', self.rbufsize)
        for line in self.rfile:  # 阻塞等
            print(f"接受到的数据：{line}")
            # 发送给客户端（类似于写给对方）
            self.wfile.write(line)
            sleep(0.3)  # 为了演示方便而加


def main():
    with TCPServer(('', 8080), MyHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()

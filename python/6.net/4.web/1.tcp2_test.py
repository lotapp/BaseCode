from time import sleep
from socket import socket, SOL_SOCKET, SO_REUSEADDR


def main():
    with socket() as tcp_socket:
        tcp_socket.connect(('', 8080))
        with open("1.tcp.py", "rb") as fs:
            while True:
                data = fs.readline()
                if data:
                    tcp_socket.send(data)
                else:
                    break
        while True:
            data = tcp_socket.recv(2048)
            if data:
                print(data.decode("utf-8"))
                sleep(0.3)  # 为了演示方便而加


if __name__ == "__main__":
    main()

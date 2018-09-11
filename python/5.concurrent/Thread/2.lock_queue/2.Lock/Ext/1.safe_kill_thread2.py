from time import sleep
from socket import socket
from multiprocessing.dummy import threading


class IOTask:
    def __init__(self):
        self.__running = True

    def terminate(self):
        self.__running = False

    def run(self, socket):
        socket.settimeout(3)  # 设置超时时间
        while self.__running:
            try:
                print("正在忙.....")
                socket.recv(8192)
                sleep(1)
                break
            except Exception:
                print("超时处理")
                break
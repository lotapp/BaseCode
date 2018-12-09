import time
import socket


def main():
    for i in range(1000):
        with socket.socket() as tcp_client:
            tcp_client.connect(('127.0.0.1', 8080))
            if i % 100 == 0:
                tcp_client.send(b"-" * 10)
                time.sleep(1)


if __name__ == "__main__":
    main()

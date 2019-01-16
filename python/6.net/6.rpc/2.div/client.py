from client_stub import ClientStub


def main():
    stub = ClientStub(("192.168.36.123", 50051))

    result = stub.get("sum", (1, 2))
    print(f"1+2={result}")

    result = stub.get("sum", (1.1, 2))
    print(f"1.1+2={result}")

    time_str = stub.get("get_time")
    print(time_str)


if __name__ == "__main__":
    main()

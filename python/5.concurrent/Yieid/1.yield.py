def fibona(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for i in fibona(10):
        print(i)


if __name__ == "__main__":
    main()

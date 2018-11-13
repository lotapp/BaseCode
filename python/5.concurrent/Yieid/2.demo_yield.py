from time import sleep


def test1():
    while True:
        print("test1")
        sleep(0.2)
        yield


def test2():
    while True:
        print("test2")
        sleep(0.2)
        yield


def main():
    while True:
        next(test1())
        next(test2())


if __name__ == "__main__":
    main()

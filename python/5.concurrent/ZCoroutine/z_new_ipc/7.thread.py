import concurrent.futures

num = 0


def test(i):
    global num
    for _ in range(10000000):
        num += i


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("start submit...")
        future1 = executor.submit(test, 1)
        future2 = executor.submit(test, -1)
        concurrent.futures.wait([future1, future2])  # wait some time
        print("end submit...")
    global num
    print(num)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"time:{time.time()-start_time}")

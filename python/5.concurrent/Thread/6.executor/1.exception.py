import concurrent.futures


def test1(name):
    print(name)
    return "姓名：" + name


def test2(name):
    raise Exception("我发送异常了！")


def call_back(future):
    ex = future.exception()
    if ex:
        print(ex)
    else:
        print(future.result())


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(test1, "小明")
        future2 = executor.submit(test2, "小张")
        future1.add_done_callback(call_back)
        future2.add_done_callback(call_back)


if __name__ == "__main__":
    main()

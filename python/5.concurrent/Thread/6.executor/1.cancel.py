import time
from concurrent.futures import ThreadPoolExecutor


def test(name, age):
    print(name, age)
    time.sleep(2)
    return "test over"


def main():
    with ThreadPoolExecutor(1) as executor:
        # 也可以这么写：(*kwargs) submit(test, name="小明", age=23)
        future1 = executor.submit(test, "小明", 23)
        future2 = executor.submit(test, "小张", 25)

        print(f"任务1是否完成：{future1.done()}，任务2是否完成：{future2.done()}")
        print(f"任务2取消成功：{future2.cancel()}")
        print(f"任务1是否完成：{future1.done()}，任务2是否完成：{future2.done()}")

        result = future1.result()
        print(result)
        print(f"任务1是否完成：{future1.done()}，任务2是否完成：{future2.done()}")


if __name__ == "__main__":
    main()

import time
from concurrent.futures import ThreadPoolExecutor


def test(name, age):
    # print(name, age)
    time.sleep(2)
    return "test over"


def main():
    with ThreadPoolExecutor() as executor:
        # 也可以这么写：(*kwargs) submit(test, name="小明", age=23)
        future = executor.submit(test, "小明", 23)
        print(future.done())
        result = future.result()
        print(result)
        print(future.done())


if __name__ == "__main__":
    main()

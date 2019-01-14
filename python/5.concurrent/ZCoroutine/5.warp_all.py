import time
import asyncio
import concurrent.futures


# 模拟一个耗时操作
def test(n):
    return sum(i * i for i in range(10**n))


async def main():
    loop = asyncio.get_running_loop()
    time1 = time.time()

    # 在协程中创建的默认池中运行
    result = await loop.run_in_executor(None, test, 6)
    print("默认线程池：", result)

    time2 = time.time()
    print(time2 - time1)

    # 在自己定义的线程池中运行
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, test, 6)
        print("自定义线程池：", result)

    time3 = time.time()
    print(time3 - time2)

    # # 在自己定义的进程池中运行
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(pool, test, 6)
    #     print("自定义进程池：", result)

    # time4 = time.time()
    # print(time4 - time3)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio


# 模拟一个耗时操作
def test(n):
    return sum(i * i for i in range(10**n))


async def main():
    # 获取loop
    loop = asyncio.get_running_loop()

    # 新版兼任代码
    result = await loop.run_in_executor(None, test, 7)
    print(result)


if __name__ == "__main__":
    import time

    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)
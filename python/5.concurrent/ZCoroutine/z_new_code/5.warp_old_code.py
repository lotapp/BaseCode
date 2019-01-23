import asyncio
import concurrent.futures


# 模拟一个耗时操作
def test(n):
    return sum(i * i for i in range(10**n))


# # old main
# def main():
#     with concurrent.futures.ThreadPoolExecutor() as pool:
#         # 注意：future和asyncio.future是不一样的
#         future = pool.submit(test, 7)
#         result = future.result()
#         print(result)


async def main():
    # 获取loop
    loop = asyncio.get_running_loop()

    with concurrent.futures.ThreadPoolExecutor() as pool:
        # 新版兼任代码
        result = await loop.run_in_executor(pool, test, 7)
        print(result)
    

if __name__ == "__main__":
    import time

    start_time = time.time()

    # main()  # old
    asyncio.run(main())  # new

    print(time.time() - start_time)

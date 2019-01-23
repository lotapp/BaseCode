import asyncio
import concurrent.futures

num = 0


def test(i):
    global num
    for _ in range(10000000):
        num += i


async def main():
    # 获取当前loop
    loop = asyncio.get_running_loop()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("start submit...")
        future1 = loop.run_in_executor(executor, test, 1)
        future2 = loop.run_in_executor(executor, test, -1)
        # await asyncio.wait([future1,future2])
        await asyncio.gather(future1, future2)
        print("end submit...")
    global num
    print(num)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(f"time:{time.time()-start_time}")

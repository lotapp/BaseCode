import asyncio

num = 0


async def test(i):
    global num
    for _ in range(10000000):
        num += i


async def main():
    print("start tasks...")
    task1 = asyncio.create_task(test(1))
    task2 = asyncio.create_task(test(-1))
    await asyncio.gather(task1, task2)
    print("end tasks...")

    global num
    print(num)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(f"time:{time.time()-start_time}")

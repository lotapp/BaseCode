import asyncio

sem = None


# 模拟api请求
async def api_test(i):
    async with sem:
        await asyncio.sleep(1)
        print(f"The Task {i} is done")


async def main():
    global sem
    sem = asyncio.Semaphore(5)  # 设置并发数为5
    tasks = [asyncio.create_task(api_test(i)) for i in range(20)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

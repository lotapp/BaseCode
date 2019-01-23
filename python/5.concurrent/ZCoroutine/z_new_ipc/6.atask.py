import asyncio


# 不是协程就加个装饰器
@asyncio.coroutine
def test():
    print("this is a test")


async def test_async():
    print("this is a async test")
    await asyncio.sleep(1)


async def main():
    # 传入一个协程对象，返回一个task
    task1 = asyncio.create_task(test())
    task2 = asyncio.create_task(test_async())
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

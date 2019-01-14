import asyncio


def test(name):
    print(f"start {name}...")
    print(f"end {name}...")


async def main():
    # 正在执行某个任务
    loop = asyncio.get_running_loop()

    # 插入一个更要紧的任务
    # loop.call_later(0, callback, *args)
    task1 = loop.call_soon(test, "task1")

    # 多少秒后执行
    task2 = loop.call_later(2, test, "task2")

    # 内部时钟时间
    task3 = loop.call_at(loop.time() + 3, test, "task3")

    print(type(task1))
    print(type(task2))
    print(type(task3))

    # 保证loop在执行完毕后才关闭
    await asyncio.sleep(5)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

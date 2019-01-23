import asyncio

async def test():
    print("start...")
    await asyncio.sleep(10)
    print("end...")

async def main():
    task = asyncio.create_task(test())

    await asyncio.sleep(1)

    # 取消task任务
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print(f"任务已经被取消：{task.cancelled()}")
        print(f"任务是因为异常而完成：{task.done()}")

if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)
import asyncio


async def test(i):
    print(f"start...task{i}")
    if i == 2 or i == 5:
        raise asyncio.CancelledError("game over for task")
        return
    await asyncio.sleep(i)
    return f"end...task{i}"


# 第一个任务执行完成则结束此批次任务
async def main():
    tasks = [asyncio.create_task(test(i)) for i in range(10)]

    # 阻塞到发生第一个异常
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_EXCEPTION)

    for task in pending:
        # 把其他没完成的任务取消
        print(task.cancel())

    result = await asyncio.gather(*done, return_exceptions=True)
    print(result)

    # for task in done:
    #     if task.cancelled():
    #         print(f"{task}被取消")
    #     else:
    #         print(await task)
    # try:
    #     print(await task)
    # except asyncio.CancelledError as ex:
    #     print(ex)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

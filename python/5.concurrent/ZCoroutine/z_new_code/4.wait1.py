import asyncio


async def test(i):
    print(f"start...task{i}")
    await asyncio.sleep(i)
    print(f"end...task{i}")
    return "ok"


# 第一个任务执行完成则结束此批次任务
async def main():
    tasks = [asyncio.create_task(test(i)) for i in range(10)]

    # 项目里经常有这么一个场景：同时调用多个同效果的API，有一个返回后取消其他请求
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # print(await asyncio.gather(*done))
    for task in done:
        print(await task)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

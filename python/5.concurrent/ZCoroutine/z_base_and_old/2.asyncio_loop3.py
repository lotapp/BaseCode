import asyncio


# 模拟一个耗时操作
async def test(i):
    print("start...")
    # 不能再使用以前阻塞的暂停了
    await asyncio.sleep(2)
    print("end...")
    return i


async def main():
    tasks = [test(i) for i in range(10)]
    # await task 可以得到返回值
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == '__main__':
    import time

    start_time = time.time()

    # old推荐使用
    loop = asyncio.get_event_loop()
    result_list = loop.run_until_complete(main())
    print(result_list)
    # 2.0259485244750977
    print(time.time() - start_time)

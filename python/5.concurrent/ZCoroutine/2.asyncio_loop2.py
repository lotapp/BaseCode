import asyncio


# 模拟一个耗时操作
async def test(i):
    print("start...")
    # 不能再使用以前阻塞的暂停了
    await asyncio.sleep(2)
    print("end...")
    # return i


if __name__ == '__main__':
    import time

    start_time = time.time()

    tasks = [test(i) for i in range(10)]

    # # >=python3.4
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    # python3.7
    # result_list = asyncio.gather(*tasks)

    print(time.time() - start_time)

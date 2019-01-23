import asyncio


# 模拟一个耗时操作
async def test(i):
    print("start...")
    # 不能再使用以前阻塞的暂停了
    await asyncio.sleep(2)
    print("end...")
    return i


if __name__ == '__main__':
    import time

    start_time = time.time()

    # # >=python3.4
    loop = asyncio.get_event_loop()
    # 注意：是loop的方法，而不是asyncio的，不然就会引发RuntimeError：no running event loop
    tasks = [loop.create_task(test(i)) for i in range(10)]
    loop.run_until_complete(asyncio.gather(*tasks))
    for task in tasks:
        print(task.result()) # 上面把协程对象转换成task对象（协程和future相互转换的中间层）
    
    # 2.016972780227661
    print(time.time() - start_time)

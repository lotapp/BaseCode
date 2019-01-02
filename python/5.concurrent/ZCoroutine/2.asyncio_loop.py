import asyncio


# import uvloop

# 模拟一个耗时操作
async def test():
    print("start...")
    # 不能再使用以前阻塞的暂停了
    await asyncio.sleep(2)
    print("end...")
    return "ok"


if __name__ == '__main__':
    # 把asyncio的事件循环策略设置为uvloop的
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    import time
    start_time = time.time()

    # >=python3.4
    # 返回asyncio的事件循环
    # loop = asyncio.get_event_loop()
    # 运行事件循环，直到指定的future运行完毕
    # result = loop.run_until_complete(test())

    # python3.7
    result = asyncio.run(test())
    print(result)

    print(time.time() - start_time)

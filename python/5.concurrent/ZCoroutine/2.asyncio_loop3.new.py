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
    # 给 协程/futures 返回一个future聚合结果
    return await asyncio.gather(*tasks) # 记得加*来解包


if __name__ == '__main__':
    import time

    start_time = time.time()

    # python3.7
    result_list = asyncio.run(main())
    print(result_list)
    # 2.00840163230896
    print(time.time() - start_time)

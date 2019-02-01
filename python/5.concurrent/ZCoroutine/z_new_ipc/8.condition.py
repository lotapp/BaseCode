import asyncio

cond = None


def div_init():
    # do something
    return True


# 等待普通方法func返回ture后继续执行
async def test(func):
    async with cond:
        await cond.wait_for(func)
        print("do something...")


async def main():
    global cond
    cond = asyncio.Condition()  # 初始化condition

    await asyncio.gather(test(div_init))


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

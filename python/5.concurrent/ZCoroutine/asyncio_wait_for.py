import asyncio


async def test(n):
    await asyncio.sleep(n)
    print(n)


async def main():
    # 有些方法不支持超时，所以要结合asyncio.wait_for来实现
    await asyncio.wait_for(test(2), 2)  # 超时会引发异常


if __name__ == "__main__":
    asyncio.run(main())

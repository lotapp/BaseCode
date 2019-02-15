import asyncio
from async_timeout import timeout


# 兼容async的超时的上下文管理器
async def test(n):
    await asyncio.sleep(n)
    print(n)


async def main():
    # 有些方法不支持超时，所以要结合asyncio.wait_for来实现
    # 在使用aiohttp的时候会依赖async_timeout，而这个模块使用起来特别方便
    async with timeout(2):
        await test(2)  # 超时会引发异常


if __name__ == "__main__":
    asyncio.run(main())

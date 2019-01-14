import asyncio


async def test():
    print("start ...")
    await asyncio.sleep(2)
    print("end ...")


# 如果你用这个方法就不要和旧代码`loop.run_until_complete`混用
# # loop = asyncio.get_running_loop()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())

# # 如果和旧版本混用，就应该这么写了（麻烦）
# try:
#     loop = asyncio.get_running_loop()
# except RuntimeError as ex:
#     loop = asyncio.get_event_loop()
# ...
# asyncio.run(test())

async def main():
    # 这种方式获取loop
    loop = asyncio.get_running_loop()
    await test()


if __name__ == "__main__":
    asyncio.run(main())
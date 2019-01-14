import asyncio


async def main():
    reader, writer = await asyncio.open_connection("http://www.baidu.com", 80)
    # reader, writer = await asyncio.open_unix_connection("http://www.baidu.com")
    async for line in reader:
        print(line.decode("utf-8"))


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

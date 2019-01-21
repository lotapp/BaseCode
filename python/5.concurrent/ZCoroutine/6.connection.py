import asyncio


async def get_html(url, port=80):
    reader, writer = await asyncio.open_connection(url, port)
    writer.write("人生若只如初见,何事秋风悲画扇\n等闲变却故人心,却道故人心易变\n".encode("utf-8"))
    # 可以这么写是因为类实现了`__anext__`(协程方法)
    # await reader.readline()
    lines = []
    async for line in reader:
        lines.append(line.decode("utf-8"))  # \n为分割符
    return "\n".join(lines)


async def main():
    # 出错重试
    for _ in range(3):
        try:
            result = await get_html("127.0.0.1", 8080)
            print(result)
        except Exception as ex:
            print(ex)
            await asyncio.sleep(2)
        else:
            break  # 没有错误


if __name__ == "__main__":
    import time

    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

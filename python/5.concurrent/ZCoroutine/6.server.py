import asyncio


async def handler(client_reader, client_writer):

    # while True:
    #     line = await client_reader.readline()  # 读取一行数据
    #     if line:
    #         print(line.decode("utf-8"))
    #     else:
    #         break
    async for line in client_reader:
        print(line.decode("utf-8"))

    client_writer.write("骊山语罢清宵半,泪雨霖铃终不怨\n何如薄幸锦衣郎,比翼连枝当日愿\n".encode("utf-8"))
    await client_writer.drain()
    client_writer.close()  # 关闭connection


async def main():
    server = await asyncio.start_server(handler, "127.0.0.1", 8080)
    # 实现了协程方法`__aenter__`和`__aexit__`的可以使用`async with`
    async with server:
        # async def serve_forever(self):pass ==> use await
        await server.serve_forever()


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

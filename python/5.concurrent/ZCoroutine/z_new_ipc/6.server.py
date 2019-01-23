import asyncio


async def handler(client_reader, client_writer):
    # 没有数据就阻塞等（主线程做其他事情去了）
    data = await client_reader.read(2048)
    print(data.decode("utf-8"))
    
    client_writer.write("骊山语罢清宵半,泪雨霖铃终不怨\n何如薄幸锦衣郎,比翼连枝当日愿".encode("utf-8"))
    await client_writer.drain()  # 等待缓冲区（缓冲区没占满就直接返回）
    client_writer.close()  # 关闭连接


async def main():
    server = await asyncio.start_server(handler, "127.0.0.1", 8080)
    print("Server已经启动，端口：8080")
    # 实现了协程方法`__aenter__`和`__aexit__`的可以使用`async with`
    async with server:
        # async def serve_forever(self):pass ==> use await
        await server.serve_forever()  # 异步方法


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)
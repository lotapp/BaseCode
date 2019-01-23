import asyncio


async def get_html(host):
    print("get_html %s..." % host)
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write(f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode('utf-8'))
    await writer.drain()  # 等待缓冲区

    html_list = []
    async for line in reader:
        html_list.append(line.decode("utf-8"))

    writer.close()  # 关闭连接
    return "".join(html_list)


async def main():
    tasks = [
        asyncio.create_task(get_html(url))
        for url in ['dotnetcrazy.cnblogs.com', 'dunitian.cnblogs.com']
    ]
    html_list = await asyncio.gather(*tasks)
    print(html_list)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

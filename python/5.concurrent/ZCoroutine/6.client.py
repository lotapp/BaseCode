import asyncio


async def main():
    reader, writer = await asyncio.open_connection("127.0.0.1", 8080)
    writer.write("人生若只如初见,何事秋风悲画扇\n等闲变却故人心,却道故人心易变".encode("utf-8"))
    data = await reader.read(2048)
    if data:
        print(data.decode("utf-8"))


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

import asyncio


async def test(time):
    print("start...")
    await asyncio.sleep(time)
    print("end...")
    return time


async def main():
    task = asyncio.create_task(test(3))
    try:
        result = await asyncio.wait_for(task, timeout=2)
        print(result)
    except asyncio.CancelledError:
        print("Cancel")
    except asyncio.TimeoutError:
        print("超时取消")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

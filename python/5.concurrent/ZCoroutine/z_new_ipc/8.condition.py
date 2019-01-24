import asyncio

con = None


async def main():
    global con
    con = asyncio.Condition()
    


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

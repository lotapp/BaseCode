import random
import asyncio


async def producer(q, i):
    for i in range(5):
        num = random.random()
        await q.put(num)
        print(f"[生产者{i}]商品{num}出厂了")
        await asyncio.sleep(num)


async def consumer(q, i):
    while True:
        data = await q.get()
        print(f"[消费者{i}]商品{data}抢光了")


async def main():
    queue = asyncio.Queue(10)  # 为了演示，我这边限制一下

    p_tasks = [asyncio.create_task(producer(queue, i)) for i in range(2)]  # 两个生产者
    c_tasks = [asyncio.create_task(consumer(queue, i)) for i in range(5)]  # 五个消费者
    await asyncio.gather(*p_tasks, *c_tasks)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

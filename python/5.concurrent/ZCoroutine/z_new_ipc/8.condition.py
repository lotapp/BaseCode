import asyncio

cond = None
p_list = []


# 生产者
async def producer(n):
    for i in range(5):
        async with cond:
            p_list.append(f"{n}-{i}")
            print(f"[生产者{n}]生产商品{n}-{i}")
            # 通知任意一个消费者
            cond.notify()  # 通知全部消费者：cond.notify_all()
        # 摸拟一个耗时操作
        await asyncio.sleep(0.01)


# 消费者
async def consumer(i):
    while True:
        async with cond:
            if p_list:
                print(f"列表商品：{p_list}")
                name = p_list.pop()  # 消费商品
                print(f"[消费者{i}]消费商品{name}")
                print(f"列表剩余：{p_list}")

                # 摸拟一个耗时操作
                await asyncio.sleep(0.01)
            else:
                await cond.wait()


async def main():
    global cond
    cond = asyncio.Condition()  # 初始化condition
    p_tasks = [asyncio.create_task(producer(i)) for i in range(2)]  # 两个生产者
    c_tasks = [asyncio.create_task(consumer(i)) for i in range(5)]  # 五个消费者
    await asyncio.gather(*p_tasks, *c_tasks)


if __name__ == "__main__":
    asyncio.run(main())

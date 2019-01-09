import asyncio


async def test(time):
    print("start...")
    await asyncio.sleep(time)
    print("end...")
    return time


async def main():
    tasks = [asyncio.create_task(test(i)) for i in range(10)]

    # 已完成的任务（包含异常），未完成的任务
    done, pending = await asyncio.wait(tasks, timeout=2)
    # 任务总数（我用了3种表示）PS：`all_tasks()`的时候记得去除main的那个
    print(
        f"任务总数：{len(tasks)}=={len(done)+len(pending)}=={len(asyncio.Task.all_tasks())-1}"
    )
    # 所有未完成的task：asyncio.all_tasks()，记得去掉run(main())
    print(f"未完成Task:{len(pending)}=={len(asyncio.all_tasks()) - 1}")

    print(await asyncio.gather(*done))
    # for task in done:
        # print(await task)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

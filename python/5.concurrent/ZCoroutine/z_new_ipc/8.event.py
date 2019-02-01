import asyncio

event = None
html_dict = {}


async def updates():
    # event.wait()是协程方法，需要await
    await event.wait()
    # 入库操作省略 html_dict >> DB
    return "html_dict >> DB done"


async def get_html(url):
    # 摸拟网络请求
    await asyncio.sleep(2)
    html_dict[url] = f"<h1>{url}</h1>"  # 可以暂时写入临时文件中

    event.set()  # 标记完成，普通方法
    return f"{url} done"


async def main():
    global event
    event = asyncio.Event()  # 初始化 event 对象

    # 创建批量任务
    tasks = [
        asyncio.create_task(get_html(f"www.mmd.com/a/{i}"))
        for i in range(1, 10)
    ]
    # 批量更新操作
    tasks.append(asyncio.create_task(updates()))

    result = await asyncio.gather(*tasks)
    print(result)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

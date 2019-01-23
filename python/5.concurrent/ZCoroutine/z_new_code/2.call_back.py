import asyncio


async def get_html(url):
    print(f"get {url} ing")
    # if url == "https://www.asp.net":
    #     raise Exception("Exception is over")
    await asyncio.sleep(2)
    return f"<h1>This is a test for {url}</h1>"


def callback_func(task):
    print(type(task))
    if task.done():
        print(f"done")  # print(task.result())


async def main():
    urls = [
        "https://www.baidu.com", "https://www.asp.net",
        "https://www.python.org", "https://www.sogou.com"
    ]
    # asyncio.create_task来创建一个Task
    tasks = [asyncio.create_task(get_html(url)) for url in urls]
    # 给每个任务都加一个回调函数
    for task in tasks:
        task.add_done_callback(callback_func)
    # 批量执行任务
    result = await asyncio.gather(*tasks)
    print(result)  # 返回 result list


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

# Task所有方法：['add_done_callback', 'all_tasks', 'cancel', 'cancelled', 'current_task', 'done', 'exception', 'get_loop', 'get_stack', 'print_stack', 'remove_done_callback', 'result', 'set_exception', 'set_result']
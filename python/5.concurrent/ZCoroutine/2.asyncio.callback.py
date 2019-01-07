# 低级API示例
import asyncio


async def get_html(url):
    print(f"get {url} ing")
    await asyncio.sleep(2)
    return f"<h1>This is a test for {url}</h1>"


def call_back(task):
    # do something
    print(type(task))
    print(task.result())


if __name__ == "__main__":
    import time
    start_time = time.time()

    urls = [
        "https://www.baidu.com", "https://www.sogou.com",
        "https://www.python.org", "https://www.asp.net"
    ]
    tasks = set()  # 任务集合
    loop = asyncio.get_event_loop()
    for url in urls:
        # task = asyncio.ensure_future(get_html(url))
        task = loop.create_task(get_html(url))
        # 【核心代码】设置回调函数
        task.add_done_callback(call_back)
        # 添加到任务集合中
        tasks.add(task)
    # 批量执行
    loop.run_until_complete(asyncio.gather(*tasks))

    print(time.time() - start_time)

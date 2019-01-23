import asyncio
import functools


async def get_html(url):
    await asyncio.sleep(2)
    return "This is a test for"


# 注意一个东西：通过偏函数传过来的参数在最前面
def call_back(url, task):
    # do something
    print(type(task))
    print(task.result(), url)


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
        # 设置回调函数 （不支持传参数，我们就利用偏函数来传递）
        task.add_done_callback(functools.partial(call_back, url))
        # 添加到任务集合中
        tasks.add(task)
    # 批量执行
    loop.run_until_complete(asyncio.gather(*tasks))

    print(time.time() - start_time)

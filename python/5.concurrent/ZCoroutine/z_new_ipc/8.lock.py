import asyncio

# 用来存放页面缓存
cache_dict = {}
lock = None  # asyncio.Lock()


# 模拟一个获取html的过程
async def fetch(url):
    # 每次网络访问，时间其实不确定的
    import random
    time = random.randint(2, 5)
    print(time)

    await asyncio.sleep(time)
    return f"<h2>{url}</h2>"


async def get_html(url):
    async with lock:
        # 如果缓存存在，则返回缓存的页面
        for url in cache_dict:
            return cache_dict[url]
        # 否则获取页面源码并缓存
        html = await fetch(url)
        cache_dict[url] = html
        return html


async def parse_js(url):
    html = await get_html(url)
    # do somthing
    return len(html)


async def parse_html(url):
    html = await get_html(url)
    # do somthing
    return html


async def main():
    global lock
    lock = asyncio.Lock()  # 如果在开头就定义，那么lock的loop和方法的loop就会不一致了

    # 提交两个Task任务
    task1 = asyncio.create_task(parse_js("www.baidu.com"))
    task2 = asyncio.create_task(parse_html("www.baidu.com"))
    # 等待任务结束
    result_list = await asyncio.gather(task1, task2)
    print(result_list)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

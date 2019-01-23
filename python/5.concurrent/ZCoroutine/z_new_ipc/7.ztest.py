import asyncio

# 用来存放页面缓存
cache_dict = {}


async def get_html(url):
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


async def parse_html(url):
    html = await get_html(url)
    # do somthing


async def main():
    # 举个例子，baidu一开始没缓存，那解析js和解析html的任务提交的时候，dict里面是没有缓存的
    # 而网络IO又是一个比较耗时的任务，这样就导致了请求了两次（更容易触发反爬虫机制）
    url = "www.baidu.com"
    # 提交两个Task任务
    task1 = asyncio.create_task(parse_js(url))
    task2 = asyncio.create_task(parse_html(url))
    # 等待任务结束
    result_list = await asyncio.gather(task1, task2)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

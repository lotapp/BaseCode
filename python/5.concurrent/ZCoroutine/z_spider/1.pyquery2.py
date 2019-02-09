import asyncio
import aiohttp
from pyquery import PyQuery

error_urls = set()


# 获取页面html
async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            error_urls.add(url)  # 待处理的url集合


# 详情页获取测试
async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session,
                           "http://www.biquge.cm//12/12097/7563949.html")
        pq = PyQuery(html)
        print(pq("#content").text())
        # results = [item.text() for item in pq.items("#content")]
        # print(results)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

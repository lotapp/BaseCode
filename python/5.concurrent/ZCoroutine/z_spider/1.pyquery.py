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


# 阻塞方法
def saves(results):
    with open("www.biquge.cm.txt", "a+", encoding="utf-8") as fs:
        fs.writelines(results)
        print("ok")


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://www.biquge.cm/12/12097/")
        pq = PyQuery(html)

        results = [
            item.text() + ":" + item.attr("href") + "\n"
            for item in pq.items("dd a")
        ]
        # print(pq("dd a").text())

        # 兼容阻塞旧代码
        await asyncio.get_running_loop().run_in_executor(None, saves, results)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)

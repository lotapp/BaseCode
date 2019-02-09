import asyncio
import aiohttp
from pyquery import PyQuery

sem = None
error_urls = set()


# 获取html
async def fetch(session, url):
    async with sem:
        async with session.get(url) as response:
            if response.status == 200:
                # aiohttp遇到非法字符的处理
                return await response.text("gbk", "ignore")  # 忽略非法字符
            else:
                error_urls.add(url)  # 待处理的url集合


# 获取文章正文
async def get_text(session, url):
    # 把相对路径改成域名+路径
    if not url.startswith("http://www.biquge.cm"):
        url = "http://www.biquge.cm" + url
    html = await fetch(session, url)
    pq = PyQuery(html)
    return pq("#content").text()


# 普通阻塞方法
def save(title, text):
    with open("恐怖复苏.md", "a+", encoding="gbk") as fs:
        fs.write(f"## {title}\n\n{text}\n\n")
        print(f"{title} done...")


async def main():
    global sem
    sem = asyncio.Semaphore(3) # 控制并发数反而更快
    loop = asyncio.get_running_loop()

    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://www.biquge.cm/12/12097/")
        pq = PyQuery(html)
        for item in pq.items("dd a"):
            title = item.text()
            text = await get_text(session, item.attr("href"))
            # 兼容阻塞旧代码
            await loop.run_in_executor(None, save, title, text)
    print("task over")


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)
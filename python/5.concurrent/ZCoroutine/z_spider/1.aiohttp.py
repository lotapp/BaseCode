import asyncio
import aiohttp

error_urls = set()


# 获取页面html
async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            error_urls.add(url)  # 添加到待处理集合中


# 阻塞方法
def save(text):
    with open("data.txt", "a+", encoding="utf-8") as fs:
        fs.write("\n" + text)
        print("ok")


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://www.biquge.cm/12/12097/")
        if html:  # 获取到html
            print(len(html))

            # 新版兼任代码
            await asyncio.get_running_loop().run_in_executor(None, save, html)


if __name__ == "__main__":
    import time
    start_time = time.time()

    asyncio.run(main())

    print(time.time() - start_time)
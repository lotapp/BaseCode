import asyncio


async def get_html(url):
    print(f"get url for{url}")
    await asyncio.sleep(2)
    return f"<h1>This is a test for {url}</h1>"


async def main():
    urls1 = ["https://www.baidu.com", "https://www.asp.net"]
    urls2 = ["https://www.python.org", "https://www.sogou.com"]

    tasks1 = [asyncio.create_task(get_html(url)) for url in urls1]
    tasks2 = [asyncio.create_task(get_html(url)) for url in urls2]
    
    # 等待两组都完成，然后返回聚合结果
    result = await asyncio.gather(*tasks1, *tasks2)
    print(result)


if __name__ == "__main__":
    import time
    start_time = time.time()

    try:
        asyncio.run(main())
    except Exception as ex:
        print(ex)

    print(time.time() - start_time)

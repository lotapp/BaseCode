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

    group1 = asyncio.gather(*tasks1)
    group2 = asyncio.gather(*tasks2)
    
    # 分组2因为某原因被取消任务了（模拟）
    group2.cancel()

    # 等待两组都完成，然后返回聚合结果
    result = await asyncio.gather(group1, group2, return_exceptions=True)
    print(result)


if __name__ == "__main__":
    import time
    start_time = time.time()

    try:
        asyncio.run(main())
    except Exception as ex:
        print(ex)

    print(time.time() - start_time)

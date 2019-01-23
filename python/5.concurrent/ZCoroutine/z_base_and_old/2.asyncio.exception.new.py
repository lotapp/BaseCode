import asyncio


async def get_html(url):
    print(f"get {url} ing")
    if url == "https://www.asp.net":
        raise Exception("Exception is over")
    await asyncio.sleep(2)
    return f"<h1>This is a test for {url}</h1>"


async def main():
    urls = [
        "https://www.baidu.com", "https://www.asp.net",
        "https://www.python.org", "https://www.sogou.com"
    ]
    tasks = [get_html(url) for url in urls]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time
    start_time = time.time()

    try:
        asyncio.run(main())
    except Exception as ex:
        print(ex)

    print(time.time() - start_time)

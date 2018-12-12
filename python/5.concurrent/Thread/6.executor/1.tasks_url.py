import time
import urllib.request
import concurrent.futures

url_list = [
    "https://www.baidu.com", "https://www.qq.com", "https://www.sogou.com",
    "https://www.cnblogs.com"
]


def get_html(url, timeout=10):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 用字典可以通过返回的 future 拿到 url
        tasks = {executor.submit(get_html, url): url for url in url_list}
        # 遍历完成的 future 对象
        for task in concurrent.futures.as_completed(tasks):
            url = tasks[task]
            try:
                result = task.result()
            except Exception as ex:
                print(ex)
            else:
                print(url, len(result))

    print(time.time() - start_time)


if __name__ == "__main__":
    main()

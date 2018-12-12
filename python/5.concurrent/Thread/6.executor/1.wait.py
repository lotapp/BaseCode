import time
import urllib.request
import concurrent.futures


def get_html(url):
    with urllib.request.urlopen(url) as conn:
        return conn.read()


def main():
    url_list = [
        "https://www.baidu.com", "https://www.qq.com", "https://www.sogou.com",
        "https://www.cnblogs.com"
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = {executor.submit(get_html, url): url for url in url_list}
        # 等待全部完成
        concurrent.futures.wait(tasks)
        # 我们来看看状态
        for task in tasks:
            print(task.done())
        # for task in concurrent.futures.as_completed(tasks):
        #     url = tasks[task]
        #     try:
        #         result = task.result()
        #     except Exception as ex:
        #         print(url, ex)
        #     else:
        #         print(url, len(result))


if __name__ == "__main__":
    main()

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

        # FIRST_COMPLETED：等待第一个完成就返回
        done_set, no_done_set = concurrent.futures.wait(
            tasks, return_when=concurrent.futures.FIRST_COMPLETED)

        # 返回值是 `done=true的set集合` 和 `done=false的set` 组成的元组
        print(done_set)  # 可以根据对应的set，进行相应处理
        print(no_done_set)  # 可以根据对应的set，进行相应处理

        # 我们来看看状态
        for task in tasks:
            print(task.done())


if __name__ == "__main__":
    main()

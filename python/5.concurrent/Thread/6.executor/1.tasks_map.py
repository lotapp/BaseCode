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
        for result in executor.map(get_html, url_list):
            print(len(result))

    print(time.time() - start_time)


if __name__ == "__main__":
    main()

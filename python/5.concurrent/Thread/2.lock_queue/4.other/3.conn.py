from time import sleep
from multiprocessing.dummy import Pool as ThreadPool, Event

event = Event()


def conn_redis():
    n = 1
    time_out = 0.5
    # 重试机制
    while not event.is_set():
        if n == 4:  # 自定义重试次数
            raise TimeoutError("\033[41mRedis连接超时，请重试\033[0m")
        event.wait(time_out * n)  # 公共组件，设置超时机制
        print(f"[第{n}次尝试]Redis当前连接超时，正在重试～")
        n += 1
    print("\033[42mRedis连接成功\033[0m")


def update_config():
    print("正在配置中心获取最新配置～")
    sleep(3)  # 模拟网络延迟
    event.set()  # 同步后标记一下


def error_callback(data):
    print(data)


def main():
    pool = ThreadPool()
    pool.apply_async(update_config, error_callback=error_callback)
    pool.apply_async(conn_redis, error_callback=error_callback)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

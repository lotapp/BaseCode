import time
import gevent
from gevent import monkey

# 打个兼容补丁
monkey.patch_all()


def test(name):
    while True:
        print(f"name:{name},{gevent.getcurrent()}")
        time.sleep(0.5)


def main():
    # 等待全部完成
    gevent.joinall([
        gevent.spawn(test, "小明"),
        gevent.spawn(test, "小张"),
        gevent.spawn(test, "小潘")
    ])


if __name__ == "__main__":
    main()

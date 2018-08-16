from multiprocessing import Queue
from multiprocessing.managers import BaseManager


def main():
    # 用来身份验证的
    key = b"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
    get_zhang_queue = Queue()  # 小张消息队列
    get_ming_queue = Queue()  # 小明消息队列

    # 把Queue注册到网络上, callable参数关联了Queue对象
    BaseManager.register("get_zhang_queue", callable=lambda: get_zhang_queue)
    BaseManager.register("get_ming_queue", callable=lambda: get_ming_queue)

    # 实例化一个Manager对象。绑定ip+端口, 设置验证秘钥
    manager = BaseManager(address=("192.168.36.235", 5438), authkey=key)
    # 运行serve
    manager.get_server().serve_forever()


if __name__ == '__main__':
    main()

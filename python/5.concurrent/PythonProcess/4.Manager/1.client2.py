from multiprocessing.managers import BaseManager


def main():
    """客户端2"""
    key = b"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
    
    # 注册对应方法的名字（从网络上获取Queue）
    BaseManager.register("get_ming_queue")
    BaseManager.register("get_zhang_queue")

    # 实例化一个Manager对象。绑定ip+端口, 设置验证秘钥
    m = BaseManager(address=("192.168.36.235", 5438), authkey=key)
    # 连接到服务器
    m.connect()

    q1 = m.get_zhang_queue()  # 获取小张说的话
    print(q1.get())

    q2 = m.get_ming_queue()  # 在自己队列里面留言
    q2.put("[小明]这几天咱们终于可以不加班了(>_<)")

if __name__ == '__main__':
    main()

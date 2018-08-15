import os
import time
from multiprocessing import Pool  # 首字母大写


def test(name):
    print("[子进程%s]PID=%d，PPID=%d" % (name, os.getpid(), os.getppid()))
    time.sleep(1)
    return name


def error_test(name):
    print("[子进程%s]PID=%d，PPID=%d" % (name, os.getpid(), os.getppid()))
    raise Exception("[子进程%s]啊，我挂了～" % name)


def callback(result):
    """成功之后的回调函数"""
    print("[子进程%s]执行完毕" % result)  # 没有返回值就为None


def error_callback(msg):
    """错误之后的回调函数"""
    print(msg)


def main():
    print("[父进程]PID=%d，PPID=%d" % (os.getpid(), os.getppid()))
    p = Pool()  # CPU默认核数
    for i in range(5):
        # 搞2个出错的看看
        if i > 2:
            p.apply_async(
                error_test,
                args=(i, ),
                callback=callback,
                error_callback=error_callback)  # 异步执行
        else:
            # 异步执行，成功后执行callback函数（有点像jq）
            p.apply_async(test, args=(i, ), callback=callback)
    p.close()  # 关闭池，不再加入新任务
    p.join()  # 等待所有子进程执行完毕回收资源
    print("over")


if __name__ == '__main__':
    main()
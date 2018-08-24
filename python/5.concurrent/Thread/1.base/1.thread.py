import os
from threading import Thread, current_thread


def test(name):
    # current_thread()返回当前线程的实例
    thread_name = current_thread().name  # 获取线程名
    print(f"[编号：{name}]，ThreadName：{thread_name}\nPID：{os.getpid()}，PPID：{os.getppid()}")


def main():
    t_list = [Thread(target=test, args=(i, )) for i in range(5)]
    for t in t_list:
        t.start()  # 批量启动
    for t in t_list:
        t.join()  # 批量回收
    # 主线程
    print(f"[Main]，ThreadName：{current_thread().name}\nPID：{os.getpid()}，PPID：{os.getppid()}")


if __name__ == '__main__':
    main()

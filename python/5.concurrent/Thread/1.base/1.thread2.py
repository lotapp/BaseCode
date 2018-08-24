from threading import Thread, current_thread


def test():
    # current_thread()返回当前线程的实例
    print(f"ThreadName：{current_thread().name}")


def main():
    t1 = Thread(target=test, name="小明")
    t2 = Thread(target=test)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 主线程
    print(f"[Main]，ThreadName：{current_thread().name}")


if __name__ == '__main__':
    main()

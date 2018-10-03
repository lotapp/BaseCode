from time import sleep
from multiprocessing.dummy import Pool as ThreadPool, Event

event = Event()


def click():
    # event.clear()  # 设置标准为假（默认是False）
    print("用户在修改网页表单")
    sleep(2)
    print("点击了修改案例")
    event.set()  # 设置标准为真


def update():
    print(f"事件状态：{event.is_set()}")
    event.wait()  # 等待到标志为真
    print("修改成功")
    print(f"事件状态：{event.is_set()}")


def main():
    pool = ThreadPool()
    pool.apply_async(click)
    pool.apply_async(update)
    pool.apply_async(click)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

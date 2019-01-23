import asyncio


# 回调函数一般都是普通函数
def test(name):
    print(name)


if __name__ == "__main__":
    import time
    start_time = time.time()

    # loop = asyncio.get_running_loop() 不要和旧代码混用
    # `asyncio.get_running_loop()`和`asyncio.run()`成对出现
    loop = asyncio.get_event_loop()

    # 新版本限制了时间不能超过24h（防止有些人当定时任务来乱用）
    # 这个执行过程会安装时间排个先后顺序，然后再批次运行
    task4 = loop.call_later(4, test, "task2-4")
    task2 = loop.call_later(2, test, "task2-2")
    task3 = loop.call_later(3, test, "task2-3")
    task1 = loop.call_later(1, test, "task2-1")
    # 取消测试
    task4.cancel()
    # close是直接丢弃任务然后关闭loop
    loop.call_later(4, loop.stop)  # 等任务执行完成结束任务 loop.stop()

    # run内部运行的是run_until_complete，而run_until_complete内部运行的是run_forever
    loop.run_forever()
    print(time.time() - start_time)
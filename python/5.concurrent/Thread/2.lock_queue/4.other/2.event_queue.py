from multiprocessing.dummy import Pool as ThreadPool, Queue, Event


def producer(queue):
    for i in range(10):
        event = Event()
        queue.put((event, i))
        print(f"[生产者]生产了产品{i}")
        event.wait()  # 等待消费者通知
        print(f"生产者已经收到消费情况的反馈{i}")


def consumer(queue):
    while True:
        evt, data = queue.get()
        print(f"[消费者]消费了产品{data}")
        evt.set()  # 通知生产者


def main():
    queue = Queue()
    pool = ThreadPool()
    pool.apply_async(consumer, args=(queue, ))
    pool.apply_async(producer, args=(queue, ))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

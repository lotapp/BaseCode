from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        # 设个坑，你可以自行研究下
        super().__init__()  # 放在后面就报错了
        self.name = name

    def run(self):
        print(self.name)


def main():
    t = MyThread(name="小明")
    t.start()
    t.join()


if __name__ == '__main__':
    main()

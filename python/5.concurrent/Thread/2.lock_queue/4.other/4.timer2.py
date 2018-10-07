from threading import Timer


def test(name):
    print(f"我是牛逼牛逼哄哄的~{name}")
    timer = Timer(2, test, args=("小明",))
    timer.start()


if __name__ == "__main__":
    t = Timer(2, test, ("小明",))  # Thread(target=test, args=("小明",))
    t.start()

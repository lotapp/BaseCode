from BaseActor import BaseActor


class TagActor(BaseActor):
    def run(self):
        while True:
            tag, *args = self.recv()
            getattr(self, 'do_' + tag)(*args)

    def do_A(self, x):
        print('方法A', x)

    def do_B(self, x, y):
        print('方法B', x, y)


if __name__ == '__main__':
    a = TagActor()
    a.start()
    a.send(('A', 1))  # Invokes do_A(1)
    a.send(('B', 2, 3))  # Invokes do_B(2,3)
    a.close()
    a.join()

# from collections import Iterable, Iterator # 现在已经不推荐使用了（3.8会弃用）
from collections.abc import Iterable, Iterator

# # 可迭代
# class MyArray(object):
#     def __iter__(self):
#         pass


class MyIterator(Iterator):
    def __next__(self):
        pass


class MyArray(Iterable):
    def __iter__(self):
        return MyIterator()


def main():
    # list转迭代器
    print(isinstance(iter([]), Iterator))

    # 可迭代
    print(isinstance(MyArray(), Iterable))
    # 迭代器也是可迭代的
    print(isinstance(MyIterator(), Iterable))
    # 是迭代器
    print(isinstance(MyIterator(), Iterator))


if __name__ == '__main__':
    main()

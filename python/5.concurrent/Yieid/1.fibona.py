from collections.abc import Iterable, Iterator


class FibonaIterator(Iterator):
    def __init__(self, n):
        self.__a = 0
        self.__b = 1
        self.__n = n  # 获取多少个
        self.__index = 0  # 当前索引

    def __next__(self):
        if self.__index < self.__n:
            self.__index += 1
            # 生成下一波
            self.__a, self.__b = self.__b, self.__a + self.__b
            return self.__a
        else:
            raise StopIteration


def main():
    print(FibonaIterator(10))
    for i in FibonaIterator(10):
        print(i)


if __name__ == "__main__":
    main()

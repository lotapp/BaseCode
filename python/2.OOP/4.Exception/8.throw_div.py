# 抛出自定义异常
class DntException(BaseException):
    pass


def get_age(num):
    if num <= 0:
        raise DntException("num must>0")
    else:
        print(num)


def main():
    get_age(-1)
    get_age(22)  # 程序崩了，这句话不会被执行了


if __name__ == '__main__':
    main()
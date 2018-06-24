# 捕获异常后再丢出，eg：在线运行的用户Code
def main():
    try:
        1 / 0  # ZeroDivisionError: division by zero
    except ZeroDivisionError as ex:
        print(ex)  # 写个日志，回头出问题可以深究
        raise


if __name__ == '__main__':
    main()

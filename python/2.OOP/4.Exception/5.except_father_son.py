# 如果把父类放第一个，那么ZeroDivisionError永远也不会被执行了，其实你如果装了 代码规范提示插件会提示你的
def main():
    try:
        1 / 0  # ZeroDivisionError: division by zero
    except BaseException as ex:
        print("base:", ex)
    except ZeroDivisionError as ex:
        print(ex)


if __name__ == '__main__':
    main()

# 多个异常捕获的简写
def main():
    try:
        print(xiaopan)  # NameError: name 'xiaopan' is not defined
        1 / 0  # ZeroDivisionError: division by zero
    except (NameError, ZeroDivisionError) as ex:
        print(ex)


if __name__ == '__main__':
    main()

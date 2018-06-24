# 异常捕获全格式
def test(input_str):
    try:
        eval(input_str)
    except ZeroDivisionError as ex:
        print("except:", ex)
    else:
        print("else：没有异常就奖励100块～")
    finally:
        print("finally：小明是傻子～")


def main():
    test("1/0")
    print("-" * 10)
    test("print('小明啊小明你调坑里了～')")


if __name__ == '__main__':
    main()

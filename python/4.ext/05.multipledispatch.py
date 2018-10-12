from multipledispatch import dispatch


@dispatch(str, int)
def test(name, age):
    # 必须用%s占位符的输出方式 +_+
    return ("Name:%s,Age:%s" % (name, age))


def main():
    test_str = test("小明", 23)
    print(test_str)
    # test(["小明"], "23")


if __name__ == '__main__':
    main()

# https://multiple-dispatch.readthedocs.io
# https://github.com/mrocklin/multipledispatch
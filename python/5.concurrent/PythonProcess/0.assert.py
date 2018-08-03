def test(a, b):
    assert b != 0, "哥哥，分母不能为0啊"
    return a / b


def main():
    test(1, 0)


if __name__ == '__main__':
    main()
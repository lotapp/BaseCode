def get_value(value):
    yield value


# 这个async和await替换成yield from
def get_name(name):
    # 一系列逻辑处理
    yield from get_value(name)


if __name__ == '__main__':
    gen = get_name("小明")
    print(gen.send(None))

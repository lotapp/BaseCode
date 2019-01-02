import types


# 和生成器完全分开了，不过可以理解为yield from
@types.coroutine
def get_value(value):
    yield value


async def get_name(name):
    # 一系列逻辑处理
    return await get_value(name)


if __name__ == '__main__':
    gen = get_name("小明")
    print(gen.send(None))
# 直接混用会报错：TypeError: object generator can't be used in 'await' expression

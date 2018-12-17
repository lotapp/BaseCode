import itertools


def main():
    # 模拟分表后的两个查询结果
    user1 = [{"name": "小张"}, {"name": "小明"}]
    user2 = [{"name": "小潘"}, {"name": "小周"}]
    user3 = [{"name": "test1"}, {"name": "test2"}]
    # 需求：合并并遍历
    for item in itertools.chain(user1, user2, user3):
        # 一般都是直接在这里进行处理
        for key, value in item.items():
            print(value)


if __name__ == '__main__':
    main()

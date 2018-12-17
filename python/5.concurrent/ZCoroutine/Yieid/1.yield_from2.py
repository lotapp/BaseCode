def my_chain(*args, **kwargs):
    for my_iterable in args:
        # 如果是字典类型就返回value
        if isinstance(my_iterable, dict):
            my_iterable = my_iterable.values()
        for item in my_iterable:
            yield item


def main():
    # 模拟分表后的两个查询结果
    user1 = ["小张", "小明"]
    user2 = ["小潘", "小周"]
    # dict只能遍历key（这种情况需要自己封装合并方法并处理下）
    user3 = {"name": "test1", "name1": "test2"}
    # 需求：合并并遍历
    for item in my_chain(user1, user2, user3):
        print(item)


if __name__ == '__main__':
    main()

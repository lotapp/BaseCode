# 生成新的dict数据
def get_new_item(item):
    prices = item["price"]
    item["avg"] = sum(prices) / len(prices)
    item["max"] = max(prices)
    item["min"] = min(prices)
    yield item


def get_new_data(data):
    for item in data:
        yield from get_new_item(item)


def main():
    # 需求：生成绘图的数据（max,min,avg）
    products = [{
        "id": 2344,
        "title": "御泥坊补水面膜",
        "price": [89, 76, 120, 99]
    }, {
        "id": 2345,
        "title": "御泥坊火山泥面膜",
        "price": [30, 56, 70, 89]
    }]
    new_products = list()
    for item in get_new_data(products):
        new_products.append(item)
    print(new_products)

    # 如果需要返回值就捕获StopIteration异常
    # gen = get_new_data(products)
    # while True:
    #     try:
    #         new_item = next(gen)
    #         new_products.append(new_item)
    #     except StopIteration as ex:
    #         print(ex.value)
    #         break


if __name__ == "__main__":
    main()
# new_products = [{
#     "id": 2344,
#     "title": "御泥坊补水面膜",
#     "price": [89, 76, 120, 99],
#     "max": 120,
#     "min": 76,
#     "avg": 96.0
# },
# {
#     "id": 2345,
#     "title": "御泥坊火山泥面膜",
#     "price": [30, 56, 70, 89],
#     "max": 89,
#     "min": 30,
#     "avg": 61.25
# }]
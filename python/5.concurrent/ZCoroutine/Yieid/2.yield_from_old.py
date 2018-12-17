# 生成新的dict数据
def get_new_item(item):
    prices = item["price"]
    item["avg"] = sum(prices) / len(prices)
    item["max"] = max(prices)
    item["min"] = min(prices)
    return item


def get_new_data(data):
    newdata = []
    for item in data:
        new_item = get_new_item(item)
        # print(new_item) # 处理后的新dict
        newdata.append(new_item)
    return newdata


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

    new_products = get_new_data(products)
    print(new_products)


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
# 生成新的数据
def get_new_data(data):
    for item in data:
        prices = item["price"]
        item["avg"] = sum(prices) / len(prices)
        item["max"] = max(prices)
        item["min"] = min(prices)
        yield item


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


if __name__ == "__main__":
    main()
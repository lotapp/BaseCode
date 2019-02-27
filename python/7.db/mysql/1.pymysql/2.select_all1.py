import pymysql


def main():
    # 托管的时候enter方法直接返回了cursor对象
    with pymysql.Connect(
            host="192.168.36.123",
            port=3306,
            user="dnt",
            password="dnt",
            database="dotnetcrazy",
            charset="utf8") as cursor:

        n = cursor.execute("select * from students")
        print(f"受影响行数：{n}")

        # 遍历输出
        # 通过go-sniffer监控可以知道：与数据库之后发生一次交互
        for _ in range(n):
            result = cursor.fetchone()
            print(result)
    print("over")


if __name__ == "__main__":
    main()

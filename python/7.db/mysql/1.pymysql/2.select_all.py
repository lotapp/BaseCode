import pymysql


def main():
    # 托管的时候enter方法直接返回了cursor对象
    with pymysql.connect(
            host="192.168.36.123",
            port=3306,
            user="dnt",
            password="dnt",
            database="dotnetcrazy",
            charset="utf8") as cursor:

        n = cursor.execute("select * from students")
        print(f"受影响行数：{n}")

        # 遍历输出
        for item in cursor.fetchall():
            print(item)
    print("over")


if __name__ == "__main__":
    main()

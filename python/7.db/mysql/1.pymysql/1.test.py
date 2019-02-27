import pymysql


def main():
    # 获取连接对象
    conn = pymysql.Connect(
        host='192.168.36.123',
        port=3306,
        user='dnt',
        password='dnt',
        database='dotnetcrazy',
        charset='utf8')
    # 获取游标对象
    cursor = conn.cursor()

    # 执行SQL语句
    n = cursor.execute("select * from students")

    print(n)  # 影响行数

    # 获取所有查询语句
    print(cursor.fetchall())

    print("over")


if __name__ == "__main__":
    main()

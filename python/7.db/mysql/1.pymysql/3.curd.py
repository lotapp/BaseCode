import pymysql

# +-------------+---------------------+------+-----+--------------+----------------+
# | Field       | Type                | Null | Key | Default      | Extra          |
# +-------------+---------------------+------+-----+--------------+----------------+
# | id          | int(10) unsigned    | NO   | PRI | NULL         | auto_increment |
# | name        | varchar(25)         | NO   | MUL |              |                |
# | age         | tinyint(3) unsigned | NO   |     | 0            |                |
# | work        | varchar(20)         | NO   |     | 普通学生     |                |
# | create_time | datetime            | NO   |     | NULL         |                |
# | datastatus  | tinyint(4)          | NO   |     | 0            |                |
# +-------------+---------------------+------+-----+--------------+----------------+


def main():
    conn = pymysql.connect(
        host="192.168.36.123",
        port=3306,
        user="dnt",
        password="dnt",
        database="dotnetcrazy",
        charset="utf8")
    # 获取游标
    cursor = conn.cursor()
    # cursor.callproc("存储过程名称",(xx,...))

    # insert or update
    sql = "insert into students(name,age,work,create_time,datastatus) values(%s,%s,%s,now(),1)"
    n = cursor.execute(sql, ("李四", 27, "体育课代表"))
    print(f"影响行数：{n}")

    # 可以这么理解：增删改因为改变了DB的内容，所以需要提交
    conn.commit()  # conn的commit方法

    cursor.close()  # 先关闭游标
    conn.close()  # 再关闭连接


if __name__ == "__main__":
    main()

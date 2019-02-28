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
class MySQLHelper(object):
    # 默认值放在后面
    def __init__(self,
                 user,
                 password,
                 database,
                 host="localhost",
                 port=3306,
                 charset="utf8"):
        # 获取连接
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset)
        # 获取游标对象
        self.cursor = self.conn.cursor()

    # 执行SQL语句
    def execute(self, sql, args=None):
        if args:
            return self.cursor.execute(sql, args)
        else:
            return self.cursor.execute(sql)

    # 为事物（多个execute）准备的commit方法
    def commit(self):
        self.conn.commit()

    # 事物回滚
    def rollback(self):
        self.conn.rollback()

    # 查询语句
    def query(self, sql, args=None):
        return (self.execute(sql, args), self.cursor.fetchall())

    # insert update delete 语句
    def __save_changes(self, sql, args):
        n = 0  # 受影响行数
        try:
            n = self.execute(sql, args)
            self.conn.commit()  # 提交更改
        except Exception as ex:
            print(ex)  # todo: 换成写入日记文件
            self.conn.rollback()  # 回滚
        return n

    # 插入数据
    def insert(self, sql, args=None):
        return self.__save_changes(sql, args)

    # 更新数据
    def update(self, sql, args=None):
        return self.__save_changes(sql, args)

    # 删除数据
    def _delete(self, sql, args=None):
        return self.__save_changes(sql, args)

    def __enter__(self):
        return self

    def __exit__(self, exc, value, traceback):
        self.cursor.close()
        self.conn.close()


# 可以这么理解：增删改因为改变了DB的内容，所以需要提交
def main():
    with MySQLHelper(
            host="192.168.36.123",
            port=3306,
            user="dnt",
            password="dnt",
            database="dotnetcrazy",
            charset="utf8") as db:
        # 增
        sql = "insert into students(name,age,work,create_time,datastatus) values(%s,%s,%s,now(),1)"
        n = db.insert(sql, ("老王", 26, "普通学生"))
        print(f"影响行数：{n}")

        # 查
        n, students = db.query(
            "select * from students where name=%s and datastatus=1", "老王")
        for item in students:
            print(item)
        print(f"总共有：{n}行")

        # 改（PS：多条件是,分隔，不是and）
        n = db.update("update students set age=%s, work=%s where name=%s",
                      (24, "文艺委员", '老王'))
        print(f"影响行数：{n}")

        # 查
        n, students = db.query(
            "select * from students where work='文艺委员' and datastatus=1")
        for item in students:
            print(item)
        print(f"总共有：{n}行")

        # 事物（全部使用db.execute方法）
        try:
            db.execute("update students set datastatus=99 where name=%s", "老王")
            sql = "insert into students(name,age,work,create_time,datastatus) values(%s,%s,%s,now(),1)"
            db.execute(sql, ("老王", 26, "普通学生"))
            # 摸拟执行失败 # db.execute(sql, ("老王", 26))
            db.commit()  # 事物提交
            print("不正确的老王信息已经修正~")
        except Exception as ex:
            print(ex)  # todo: 换成写入日记文件
            db.rollback()  # 事物回滚


if __name__ == "__main__":
    main()

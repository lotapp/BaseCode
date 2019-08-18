# 信安之路

## 第03周

### 前言

这周自主研究的任务如下：

![tasks](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190815194735851-1084257194.png)

任务附录的解释：

1. 文件读写在通过数据库注入漏洞获取webshell的时候很有用
2. 系统库和表存放了很多关键信息，在利用注入漏洞获取更多信息和权限的过程很有帮助
    - eg：库信息、表信息、用户信息、权限信息、安装配置信息
3. 用户信息表一般密码都是hash加密过的，可以利用hashcat暴力破解（GPU）

### 1.文件操作相关

需要什么权限才可以进行**文件读写操作**



#### 扩展：system命令

mysql命令行下的`system`摸索过程：
> PS：任意读 + 权限范围内写

渗透思路：

1. 读取某些敏感的配置文件（eg：数据库连接的配置文件）
2. 当有目录越权访问漏洞的时候可以越权执行脚本（权限范围内的目录中写入脚本）

```shell
PS C:\Users\Mao> ssh -l bryan 192.168.0.9
bryan@192.168.0.9 password:
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 5.0.0-23-generic x86_64)

bryan@bryan-pc:~$ mysql -ubryan -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.27-0ubuntu0.18.04.1-log (Ubuntu)

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> select user();
+-----------------+
| user()          |
+-----------------+
| bryan@localhost |
+-----------------+
1 row in set (0.06 sec)

mysql> system ls /home
dnt
mysql> system ls /var/www/html
index.nginx-debian.html  index.php
mysql> system cat /var/www/html/index.php
<?php
  phpinfo();
?>
mysql> system vi /home/bryan/test.py
mysql> system cat /home/bryan/test.py
print("test")
```

### 2.获取系统信息

#### 2.1.获取数据库版本

**`select version();` or `select @@version;`**

![version](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816174244029-818658625.png)

#### 2.2.获取操作系统类型

**`select @@version_compile_os;`**

![os](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816174526041-2071927434.png)

#### 2.3.获取服务器主机名

**`select @@hostname;`**

![hostname](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816175012523-83476110.png)

### 3.获取DB信息

#### 3.1.获取数据库列表

**`select schema_name from information_schema.schemata;`**
> PS：MySQL5.x可以通过schemata表来查询`权限范围内`的数据库

![schemata](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816195225864-1528468325.png)

##### root权限下获取所有DB列表

PS：**root权限**可以使用 **`select schema_name from information_schema.schemata;`** or **`select distinct(db) from mysql.db;`** 来**显示所有数据库**

![root_dbs](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816195940479-98833538.png)

#### 3.2.获取当前数据库

获取正在`use`的数据库：**`select database();`**

![database](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816182448301-1206378743.png)

#### 3.3.获取指定DB有哪些表

**`select table_schema,table_name,table_type,engine from information_schema.tables where table_schema = '数据库名';`**

![tables](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816200202982-865970783.png)

#### 3.4.查询指定表含哪些列

**`select table_schema,table_name,column_name from information_schema.columns where table_schema= '数据库名' and table_name = '表名';`**

![cloumns](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816200500422-1448822446.png)

---

PS：**查询除内置数据库外其他数据库和表**：**`select table_schema,table_name,column_name from information_schema.columns where table_schema != 'mysql' and table_schema != 'information_schema' order by table_schema,table_name;`**

![alll_info](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816200659510-997958128.png)

##### 寻找自己感兴趣的列

**根据特定关键词就可以省去暴力解猜**：**`select table_schema,table_name,column_name from information_schema.columns where column_name like 'pass%' or column_name like 'user%';`**

![key](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816200852287-1758669645.png)

---

#### 3.5.获取目录信息

1. 获取数据库**安装目录**：**`select @@basedir;`**
2. 获取**数据目录**：**`select @@datadir;`**

![dir](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816181223792-1199330919.png)

目录验证：

```shell
mysql> show variables like '%basedir%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| basedir       | /usr/ |
+---------------+-------+
1 row in set (0.00 sec)

mysql> show variables like '%datadir%';
+---------------+-----------------+
| Variable_name | Value           |
+---------------+-----------------+
| datadir       | /var/lib/mysql/ |
+---------------+-----------------+
1 row in set (0.00 sec)

```

![datadir](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816181640497-802858504.png)

---

### 4.获取用户信息

#### 4.1.获取当前用户名

**`select user();` or `select system_user();` or `select current_user;`**

![user](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816175239798-964566117.png)

##### 获取用户信息（含密码）

【root权限】**显示所有用户（含密码）**

MariaDB5.x：**`select user,host,password from mysql.user;`**

![mariadb](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816180101615-1000619390.png)

MySQL5.x：**`select user,host,authentication_string from mysql.user;`**

![mysql](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816180557305-1652622109.png)

PS：系统生成的加密sha字符串是41位（`*`1位+sha40位）
> sha1是40位，但mysql的加密是变种sha1

![sha](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816184744155-2059882406.png)

#### 4.2.查看指定DB的用户权限

**`select grantee, table_schema, privilege_type from information_schema.schema_privileges where table_schema = 'safe_db';`**

![privileges](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816203305531-1863672830.png)

#### 4.3.查询用户权限列表

**`select grantee, privilege_type, is_grantable from information_schema.user_privileges;`**
> PS：也可使用`show grants for bryan;`

![user_privileges](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816204402584-1066633373.png)

PS：root权限查询的更全面

![root_privileges](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816205518422-1770543749.png)

##### root权限通过mysql.user查询更详细权限信息

【root权限】通过mysql.user查询更详细权限信息：**`select host, user, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv, File_priv, Grant_priv, References_priv, Index_priv, Alter_priv, Show_db_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv, Execute_priv, Repl_slave_priv, Repl_client_priv from mysql.user;`**

```shell
MariaDB [safe_db]> select host, user, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv, File_priv, Grant_priv, References_priv, Index_priv, Alter_priv, Show_db_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv, Execute_priv, Repl_slave_priv, Repl_client_priv from mysql.user\G;

*************************** 1. row ***************************
                 host: %
                 user: root
          Select_priv: N
          Insert_priv: N
          Update_priv: N
          Delete_priv: N
          Create_priv: N
            Drop_priv: N
          Reload_priv: N
        Shutdown_priv: N
         Process_priv: N
            File_priv: N
           Grant_priv: N
      References_priv: N
           Index_priv: N
           Alter_priv: N
         Show_db_priv: N
           Super_priv: N
Create_tmp_table_priv: N
     Lock_tables_priv: N
         Execute_priv: N
      Repl_slave_priv: N
     Repl_client_priv: N

。。。。。。

*************************** 5. row ***************************
                 host: %
                 user: bryan
          Select_priv: N
          Insert_priv: N
          Update_priv: N
          Delete_priv: N
          Create_priv: N
            Drop_priv: N
          Reload_priv: N
        Shutdown_priv: N
         Process_priv: N
            File_priv: N
           Grant_priv: N
      References_priv: N
           Index_priv: N
           Alter_priv: N
         Show_db_priv: N
           Super_priv: N
Create_tmp_table_priv: N
     Lock_tables_priv: N
         Execute_priv: N
      Repl_slave_priv: N
     Repl_client_priv: N
*************************** 6. row ***************************
                 host: %
                 user: dnt
          Select_priv: N
          Insert_priv: N
          Update_priv: N
          Delete_priv: N
          Create_priv: N
            Drop_priv: N
          Reload_priv: N
        Shutdown_priv: N
         Process_priv: N
            File_priv: N
           Grant_priv: N
      References_priv: N
           Index_priv: N
           Alter_priv: N
         Show_db_priv: N
           Super_priv: N
Create_tmp_table_priv: N
     Lock_tables_priv: N
         Execute_priv: N
      Repl_slave_priv: N
     Repl_client_priv: N
6 rows in set (0.00 sec)
```

##### 扩展

**查看当前数据库支持哪些权限**：**`show privileges;`**

![show_privileges](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190816205246510-1636756658.png)

**获取列的权限列表**（用的不多）
> `select table_schema, table_name, column_name, privilege_type from information_schema.column_privileges;`

---

### 附录

#### 1.获取系统信息

```shell
# 获取数据库版本
MariaDB [(none)]> select version();
+----------------+
| version()      |
+----------------+
| 5.5.60-MariaDB |
+----------------+
1 row in set (0.00 sec)

MariaDB [(none)]> select @@version;
+----------------+
| @@version      |
+----------------+
| 5.5.60-MariaDB |
+----------------+
1 row in set (0.00 sec)

# 获取操作系统
MariaDB [(none)]> select @@version_compile_os;
+----------------------+
| @@version_compile_os |
+----------------------+
| Linux                |
+----------------------+
1 row in set (0.00 sec)

# 获取主机名
MariaDB [(none)]> select @@hostname;
+-----------------------+
| @@hostname            |
+-----------------------+
| localhost.localdomain |
+-----------------------+
1 row in set (0.00 sec)

mysql> select @@hostname;
+------------+
| @@hostname |
+------------+
| bryan-pc   |
+------------+
1 row in set (0.00 sec)
```

#### 2.获取DB信息

```shell
# 1.MySQL5.x可以通过schemata表来查询`权限范围内`的数据库
MariaDB [safe_db]> select schema_name from information_schema.schemata;
+--------------------+
| schema_name        |
+--------------------+
| information_schema |
| safe_db            |
| work_db            |
+--------------------+
3 rows in set (0.00 sec)

# 验证如下：show databases;
MariaDB [safe_db]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| safe_db            |
| work_db            |
+--------------------+
3 rows in set (0.00 sec)

# 【root】显示所有数据库
MariaDB [(none)]> select schema_name from information_schema.schemata;
+--------------------+
| schema_name        |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| safe_db            |
| test_db            |
| work_db            |
+--------------------+
6 rows in set (0.00 sec)

# 【root】显示所有数据库（只要授权过的数据库都会显示出来）
MariaDB [(none)]> select distinct(db) from mysql.db;
+---------+
| db      |
+---------+
| safe_db |
| test_db |
| work_db |
+---------+
3 rows in set (0.00 sec)

# 获取当前数据库
MariaDB [safe_db]> select database();
+------------+
| database() |
+------------+
| safe_db    |
+------------+
1 row in set (0.00 sec)

# 2.查询safe_db里的表名和视图
MariaDB [safe_db]> select table_schema,table_name,table_type,engine
from information_schema.tables where table_schema = 'safe_db';
+--------------+---------------+------------+--------+
| table_schema | table_name    | table_type | engine |
+--------------+---------------+------------+--------+
| safe_db      | file_records  | BASE TABLE | InnoDB |
| safe_db      | users         | BASE TABLE | InnoDB |
| safe_db      | view_userinfo | VIEW       | NULL   |
+--------------+---------------+------------+--------+
3 rows in set (0.00 sec)

# 3.查询指定表含哪些列
MariaDB [(none)]> select table_schema,table_name,column_name from information_schema.columns
where table_schema= 'safe_db' and table_name = 'users';
+--------------+------------+-------------+
| table_schema | table_name | column_name |
+--------------+------------+-------------+
| safe_db      | users      | id          |
| safe_db      | users      | username    |
| safe_db      | users      | password    |
| safe_db      | users      | email       |
| safe_db      | users      | tel         |
| safe_db      | users      | usercode    |
| safe_db      | users      | createtime  |
| safe_db      | users      | updatetime  |
| safe_db      | users      | datastatus  |
+--------------+------------+-------------+
9 rows in set (0.00 sec)

# 查询除内置数据库外其他数据库和表
MariaDB [(none)]> select table_schema,table_name,column_name from information_schema.columns
where table_schema != 'mysql' and table_schema != 'information_schema' order by table_schema,table_name;
+--------------+---------------+-------------+
| table_schema | table_name    | column_name |
+--------------+---------------+-------------+
| safe_db      | file_records  | id          |
| safe_db      | file_records  | datastatus  |
| safe_db      | file_records  | createtime  |
| safe_db      | file_records  | url         |
| safe_db      | file_records  | ip          |
| safe_db      | file_records  | user_id     |
| safe_db      | file_records  | meta_type   |
| safe_db      | file_records  | md5         |
| safe_db      | file_records  | file_name   |
| safe_db      | users         | datastatus  |
| safe_db      | users         | updatetime  |
| safe_db      | users         | createtime  |
| safe_db      | users         | usercode    |
| safe_db      | users         | tel         |
| safe_db      | users         | email       |
| safe_db      | users         | password    |
| safe_db      | users         | username    |
| safe_db      | users         | id          |
| safe_db      | view_userinfo | datastatus  |
| safe_db      | view_userinfo | tel         |
| safe_db      | view_userinfo | email       |
| safe_db      | view_userinfo | password    |
| safe_db      | view_userinfo | username    |
| safe_db      | view_userinfo | id          |
| work_db      | users         | id          |
| work_db      | users         | user_name   |
| work_db      | users         | pass        |
+--------------+---------------+-------------+
27 rows in set (0.00 sec)

# 寻找自己感兴趣的列
MariaDB [(none)]> select table_schema,table_name,column_name from information_schema.columns
where column_name like 'pass%' or column_name like 'user%';
+--------------------+-----------------+-------------+
| table_schema       | table_name      | column_name |
+--------------------+-----------------+-------------+
| information_schema | PROCESSLIST     | USER        |
| information_schema | USER_STATISTICS | USER        |
| safe_db            | file_records    | user_id     |
| safe_db            | users           | username    |
| safe_db            | users           | password    |
| safe_db            | users           | usercode    |
| safe_db            | view_userinfo   | username    |
| safe_db            | view_userinfo   | password    |
| work_db            | users           | user_name   |
| work_db            | users           | pass        |
+--------------------+-----------------+-------------+
10 rows in set (0.01 sec)

# 获取数据库安装目录
MariaDB [(none)]> select @@basedir;
+-----------+
| @@basedir |
+-----------+
| /usr      |
+-----------+
1 row in set (0.00 sec)

# 获取数据目录
MariaDB [(none)]> select @@datadir;
+-----------------+
| @@datadir       |
+-----------------+
| /var/lib/mysql/ |
+-----------------+
1 row in set (0.00 sec)
```

#### 3.获取用户信息

```shell

# 查看当前用户
MariaDB [(none)]> select user();
+-----------------+
| user()          |
+-----------------+
| bryan@localhost |
+-----------------+
1 row in set (0.00 sec)

MariaDB [(none)]> select system_user();
+-----------------+
| system_user()   |
+-----------------+
| bryan@localhost |
+-----------------+
1 row in set (0.00 sec)

MariaDB [(none)]> select current_user;
+--------------+
| current_user |
+--------------+
| bryan@%      |
+--------------+
1 row in set (0.00 sec)

# MariaDB5.x ~ 【root】显示所有用户（含密码）
MariaDB [(none)]> select user,host,password from mysql.user;
+-------+-----------+-------------------------------------------+
| user  | host      | password                                  |
+-------+-----------+-------------------------------------------+
| root  | localhost | *5E6EF6ECECBC479438947268E744A8097EB19B62 |
| root  | %         |                                           |
| root  | 127.0.0.1 | *5E6EF6ECECBC479438947268E744A8097EB19B62 |
| root  | ::1       | *5E6EF6ECECBC479438947268E744A8097EB19B62 |
| bryan | %         | *F79F429101E0EB00B8132FC6874AEC01315F2088 |
| dnt   | %         | *1132FE0C4288F794EBF0B330344ECAFDCDD01EE9 |
+-------+-----------+-------------------------------------------+

# MySQL5.x ~ 【root】显示所有用户（含密码）
mysql> select user,host,authentication_string from mysql.user;
+------------------+-----------+-------------------------------------------+
| user             | host      | authentication_string                     |
+------------------+-----------+-------------------------------------------+
| root             | localhost |                                           |
| mysql.session    | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| mysql.sys        | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| debian-sys-maint | localhost | *8D894A8D6A636A0B04DAABD0905B58349E106D6E |
| bryan            | %         | *F79F429101E0EB00B8132FC6874AEC01315F2088 |
+------------------+-----------+-------------------------------------------+
5 rows in set (0.02 sec)

# PS：MySQL的sha1是变种加密
MariaDB [safe_db]> select password('xxxx');
+-------------------------------------------+
| password('xxxx')                |
+-------------------------------------------+
| *F79F429101E0EB00B8132FC6874AEC01315F2088 |
+-------------------------------------------+
1 row in set (0.00 sec)

# 查看指定数据库授予用户的权限
MariaDB [(none)]>  select grantee, table_schema, privilege_type from information_schema.schema_privileges where table_schema = 'safe_db';
+-------------+--------------+-------------------------+
| grantee     | table_schema | privilege_type          |
+-------------+--------------+-------------------------+
| 'bryan'@'%' | safe_db      | SELECT                  |
| 'bryan'@'%' | safe_db      | INSERT                  |
| 'bryan'@'%' | safe_db      | UPDATE                  |
| 'bryan'@'%' | safe_db      | DELETE                  |
| 'bryan'@'%' | safe_db      | CREATE                  |
| 'bryan'@'%' | safe_db      | DROP                    |
| 'bryan'@'%' | safe_db      | REFERENCES              |
| 'bryan'@'%' | safe_db      | INDEX                   |
| 'bryan'@'%' | safe_db      | ALTER                   |
| 'bryan'@'%' | safe_db      | CREATE TEMPORARY TABLES |
| 'bryan'@'%' | safe_db      | LOCK TABLES             |
| 'bryan'@'%' | safe_db      | EXECUTE                 |
| 'bryan'@'%' | safe_db      | CREATE VIEW             |
| 'bryan'@'%' | safe_db      | SHOW VIEW               |
| 'bryan'@'%' | safe_db      | CREATE ROUTINE          |
| 'bryan'@'%' | safe_db      | ALTER ROUTINE           |
| 'bryan'@'%' | safe_db      | EVENT                   |
| 'bryan'@'%' | safe_db      | TRIGGER                 |
+-------------+--------------+-------------------------+
18 rows in set (0.00 sec)

# 查询用户权限列表
MariaDB [(none)]> select grantee, privilege_type, is_grantable from information_schema.user_privileges;
+-------------+----------------+--------------+
| grantee     | privilege_type | is_grantable |
+-------------+----------------+--------------+
| 'bryan'@'%' | USAGE          | NO           |
+-------------+----------------+--------------+
1 row in set (0.00 sec)

MariaDB [safe_db]> show grants for bryan;
+-----------------------------------------------------+
| Grants for bryan@%                                 |
+-----------------------------------------------------+
| GRANT USAGE ON *.* TO 'bryan'@'%' IDENTIFIED BY PASSWORD '*F79F429101E0EB00B8132FC6874AEC01315F2088' |
| GRANT ALL PRIVILEGES ON `safe_db`.* TO 'bryan'@'%' |
| GRANT ALL PRIVILEGES ON `work_db`.* TO 'bryan'@'%' |
+-----------------------------------------------------+
3 rows in set (0.00 sec)

# 【root】用户查看全部用户权限列表
MariaDB [safe_db]> select grantee, privilege_type, is_grantable from information_schema.user_privileges;
+--------------------+-------------------------+--------------+
| grantee            | privilege_type          | is_grantable |
+--------------------+-------------------------+--------------+
| 'root'@'localhost' | SELECT                  | YES          |
| 'root'@'localhost' | INSERT                  | YES          |
| 'root'@'localhost' | UPDATE                  | YES          |
| 'root'@'localhost' | DELETE                  | YES          |
| 'root'@'localhost' | CREATE                  | YES          |
| 'root'@'localhost' | DROP                    | YES          |
| 'root'@'localhost' | RELOAD                  | YES          |
| 'root'@'localhost' | SHUTDOWN                | YES          |
| 'root'@'localhost' | PROCESS                 | YES          |
| 'root'@'localhost' | FILE                    | YES          |
| 'root'@'localhost' | REFERENCES              | YES          |
| 'root'@'localhost' | INDEX                   | YES          |
| 'root'@'localhost' | ALTER                   | YES          |
| 'root'@'localhost' | SHOW DATABASES          | YES          |
| 'root'@'localhost' | SUPER                   | YES          |
| 'root'@'localhost' | CREATE TEMPORARY TABLES | YES          |
| 'root'@'localhost' | LOCK TABLES             | YES          |
| 'root'@'localhost' | EXECUTE                 | YES          |
| 'root'@'localhost' | REPLICATION SLAVE       | YES          |
| 'root'@'localhost' | REPLICATION CLIENT      | YES          |
| 'root'@'localhost' | CREATE VIEW             | YES          |
| 'root'@'localhost' | SHOW VIEW               | YES          |
| 'root'@'localhost' | CREATE ROUTINE          | YES          |
| 'root'@'localhost' | ALTER ROUTINE           | YES          |
| 'root'@'localhost' | CREATE USER             | YES          |
| 'root'@'localhost' | EVENT                   | YES          |
| 'root'@'localhost' | TRIGGER                 | YES          |
| 'root'@'localhost' | CREATE TABLESPACE       | YES          |
| 'root'@'127.0.0.1' | SELECT                  | YES          |
| 'root'@'127.0.0.1' | INSERT                  | YES          |
| 'root'@'127.0.0.1' | UPDATE                  | YES          |
| 'root'@'127.0.0.1' | DELETE                  | YES          |
| 'root'@'127.0.0.1' | CREATE                  | YES          |
| 'root'@'127.0.0.1' | DROP                    | YES          |
| 'root'@'127.0.0.1' | RELOAD                  | YES          |
| 'root'@'127.0.0.1' | SHUTDOWN                | YES          |
| 'root'@'127.0.0.1' | PROCESS                 | YES          |
| 'root'@'127.0.0.1' | FILE                    | YES          |
| 'root'@'127.0.0.1' | REFERENCES              | YES          |
| 'root'@'127.0.0.1' | INDEX                   | YES          |
| 'root'@'127.0.0.1' | ALTER                   | YES          |
| 'root'@'127.0.0.1' | SHOW DATABASES          | YES          |
| 'root'@'127.0.0.1' | SUPER                   | YES          |
| 'root'@'127.0.0.1' | CREATE TEMPORARY TABLES | YES          |
| 'root'@'127.0.0.1' | LOCK TABLES             | YES          |
| 'root'@'127.0.0.1' | EXECUTE                 | YES          |
| 'root'@'127.0.0.1' | REPLICATION SLAVE       | YES          |
| 'root'@'127.0.0.1' | REPLICATION CLIENT      | YES          |
| 'root'@'127.0.0.1' | CREATE VIEW             | YES          |
| 'root'@'127.0.0.1' | SHOW VIEW               | YES          |
| 'root'@'127.0.0.1' | CREATE ROUTINE          | YES          |
| 'root'@'127.0.0.1' | ALTER ROUTINE           | YES          |
| 'root'@'127.0.0.1' | CREATE USER             | YES          |
| 'root'@'127.0.0.1' | EVENT                   | YES          |
| 'root'@'127.0.0.1' | TRIGGER                 | YES          |
| 'root'@'127.0.0.1' | CREATE TABLESPACE       | YES          |
| 'root'@'::1'       | SELECT                  | YES          |
| 'root'@'::1'       | INSERT                  | YES          |
| 'root'@'::1'       | UPDATE                  | YES          |
| 'root'@'::1'       | DELETE                  | YES          |
| 'root'@'::1'       | CREATE                  | YES          |
| 'root'@'::1'       | DROP                    | YES          |
| 'root'@'::1'       | RELOAD                  | YES          |
| 'root'@'::1'       | SHUTDOWN                | YES          |
| 'root'@'::1'       | PROCESS                 | YES          |
| 'root'@'::1'       | FILE                    | YES          |
| 'root'@'::1'       | REFERENCES              | YES          |
| 'root'@'::1'       | INDEX                   | YES          |
| 'root'@'::1'       | ALTER                   | YES          |
| 'root'@'::1'       | SHOW DATABASES          | YES          |
| 'root'@'::1'       | SUPER                   | YES          |
| 'root'@'::1'       | CREATE TEMPORARY TABLES | YES          |
| 'root'@'::1'       | LOCK TABLES             | YES          |
| 'root'@'::1'       | EXECUTE                 | YES          |
| 'root'@'::1'       | REPLICATION SLAVE       | YES          |
| 'root'@'::1'       | REPLICATION CLIENT      | YES          |
| 'root'@'::1'       | CREATE VIEW             | YES          |
| 'root'@'::1'       | SHOW VIEW               | YES          |
| 'root'@'::1'       | CREATE ROUTINE          | YES          |
| 'root'@'::1'       | ALTER ROUTINE           | YES          |
| 'root'@'::1'       | CREATE USER             | YES          |
| 'root'@'::1'       | EVENT                   | YES          |
| 'root'@'::1'       | TRIGGER                 | YES          |
| 'root'@'::1'       | CREATE TABLESPACE       | YES          |
| 'root'@'%'         | USAGE                   | NO           |
| 'bryan'@'%'        | USAGE                   | NO           |
| 'dnt'@'%'          | USAGE                   | NO           |
+--------------------+-------------------------+--------------+
87 rows in set (0.00 sec)

# 【root】查询更详细的用户权限
MariaDB [safe_db]> select host, user, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv, File_priv, Grant_priv, References_priv, Index_priv, Alter_priv, Show_db_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv, Execute_priv, Repl_slave_priv, Repl_client_priv from mysql.user\G;

*************************** 1. row ***************************
                 host: %
                 user: root
          Select_priv: N
          Insert_priv: N
          Update_priv: N
          Delete_priv: N
          Create_priv: N
            Drop_priv: N
          Reload_priv: N
        Shutdown_priv: N
         Process_priv: N
            File_priv: N
           Grant_priv: N
      References_priv: N
           Index_priv: N
           Alter_priv: N
         Show_db_priv: N
           Super_priv: N
Create_tmp_table_priv: N
     Lock_tables_priv: N
         Execute_priv: N
      Repl_slave_priv: N
     Repl_client_priv: N

。。。。。。

*************************** 5. row ***************************
                 host: %
                 user: bryan
          Select_priv: N
          Insert_priv: N
          Update_priv: N
          Delete_priv: N
          Create_priv: N
            Drop_priv: N
          Reload_priv: N
        Shutdown_priv: N
         Process_priv: N
            File_priv: N
           Grant_priv: N
      References_priv: N
           Index_priv: N
           Alter_priv: N
         Show_db_priv: N
           Super_priv: N
Create_tmp_table_priv: N
     Lock_tables_priv: N
         Execute_priv: N
      Repl_slave_priv: N
     Repl_client_priv: N
*************************** 6. row ***************************
                 host: %
                 user: dnt
          Select_priv: N
          Insert_priv: N
          Update_priv: N
          Delete_priv: N
          Create_priv: N
            Drop_priv: N
          Reload_priv: N
        Shutdown_priv: N
         Process_priv: N
            File_priv: N
           Grant_priv: N
      References_priv: N
           Index_priv: N
           Alter_priv: N
         Show_db_priv: N
           Super_priv: N
Create_tmp_table_priv: N
     Lock_tables_priv: N
         Execute_priv: N
      Repl_slave_priv: N
     Repl_client_priv: N
6 rows in set (0.00 sec)

# PS：获取列的权限列表（用的不多）
select table_schema, table_name, column_name, privilege_type from information_schema.column_privileges;

# PS：查询数据库支持哪些权限
mysql> show privileges;
+-------------------------+---------------------------------------+-------------------------------------------------------+
| Privilege               | Context                               | Comment                                               |
+-------------------------+---------------------------------------+-------------------------------------------------------+
| Alter                   | Tables                                | To alter the table                                    |
| Alter routine           | Functions,Procedures                  | To alter or drop stored functions/procedures          |
| Create                  | Databases,Tables,Indexes              | To create new databases and tables                    |
| Create routine          | Databases                             | To use CREATE FUNCTION/PROCEDURE                      |
| Create temporary tables | Databases                             | To use CREATE TEMPORARY TABLE                         |
| Create view             | Tables                                | To create new views                                   |
| Create user             | Server Admin                          | To create new users                                   |
| Delete                  | Tables                                | To delete existing rows                               |
| Drop                    | Databases,Tables                      | To drop databases, tables, and views                  |
| Event                   | Server Admin                          | To create, alter, drop and execute events             |
| Execute                 | Functions,Procedures                  | To execute stored routines                            |
| File                    | File access on server                 | To read and write files on the server                 |
| Grant option            | Databases,Tables,Functions,Procedures | To give to other users those privileges you possess   |
| Index                   | Tables                                | To create or drop indexes                             |
| Insert                  | Tables                                | To insert data into tables                            |
| Lock tables             | Databases                             | To use LOCK TABLES (together with SELECT privilege)   |
| Process                 | Server Admin                          | To view the plain text of currently executing queries |
| Proxy                   | Server Admin                          | To make proxy user possible                           |
| References              | Databases,Tables                      | To have references on tables                          |
| Reload                  | Server Admin                          | To reload or refresh tables, logs and privileges      |
| Replication client      | Server Admin                          | To ask where the slave or master servers are          |
| Replication slave       | Server Admin                          | To read binary log events from the master             |
| Select                  | Tables                                | To retrieve rows from table                           |
| Show databases          | Server Admin                          | To see all databases with SHOW DATABASES              |
| Show view               | Tables                                | To see views with SHOW CREATE VIEW                    |
| Shutdown                | Server Admin                          | To shut down the server                               |
| Super                   | Server Admin                          | To use KILL thread, SET GLOBAL, CHANGE MASTER, etc.   |
| Trigger                 | Tables                                | To use triggers                                       |
| Create tablespace       | Server Admin                          | To create/alter/drop tablespaces                      |
| Update                  | Tables                                | To update existing rows                               |
| Usage                   | Server Admin                          | No privileges - allow connect only                    |
+-------------------------+---------------------------------------+-------------------------------------------------------+
31 rows in set (0.00 sec)

```

#### other

```shell
# 获取会话id
MariaDB [(none)]> select connection_id();
+-----------------+
| connection_id() |
+-----------------+
|               6 |
+-----------------+
1 row in set (0.00 sec)

# 获取最后一个插入的id
MariaDB [(none)]> select last_insert_id();
+------------------+
| last_insert_id() |
+------------------+
|                0 |
+------------------+
1 row in set (0.00 sec)

# 返回前一个SQL进行`update、delete、insert`操作所影响的行数
MariaDB [(none)]> select row_count();
+-------------+
| row_count() |
+-------------+
|          -1 |
+-------------+
1 row in set (0.00 sec)
```

#### 参考链接

**国外常用的SQLi备忘录**：

- MySQL：<http://pentestmonkey.net/category/cheat-sheet>
- MSSQL：<http://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet>


--经典案例：查找包含“objs”的表？查找包含“o”的数据库？
select * from sys.objects where name like '%objs%'
select * from sys.databases where name like '%o%'

--查询当前数据库兼容级别
----执行前版本：level:130（SQLServer 2016）120（SQLServer 2014），110（SQLServer 2012），100（SQLServer 2008）
select name,[compatibility_level] from sys.databases where name=DB_Name()
go

--查出所有用户表
select * from sys.objects where type='u'
--C = CHECK 约束　　D = 默认值或 DEFAULT 约束　　F = FOREIGN KEY 约束　　L = 日志　　FN = 标量函数 
--IF = 内嵌表函数 　　P = 存储过程 　　PK = PRIMARY KEY 约束（类型是 K） 　　RF = 复制筛选存储过程 
-- S = 系统表 　　TF = 表函数 　　TR = 触发器 　　U = 用户表 　　UQ = UNIQUE 约束（类型是 K） 
--V = 视图 　　X = 扩展存储过程

--------------------------------------------------------------------------------------------------

--当前数据库文件存放路径
select * from sys.database_files
select * from sys.database_files where type=1 --type=1代表是日记文件
select * from sys.database_files where type=0 --type=0代表是数据文件

--查看文件组
select * from sys.filegroups

--查询当前数据库有哪些表
select table_name from information_schema.tables

--查看分区函数
select * from sys.partition_functions

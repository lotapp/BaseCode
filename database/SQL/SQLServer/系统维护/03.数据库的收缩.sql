use [master]
go
--alter database [BigValues] set recovery simple with no_wait
--go
alter database [BigValues] set recovery simple   --简单模式
go

use [BigValues]

--当前数据库日记的逻辑名列表
select name from sys.database_files where type=1 --type=1代表是日记文件
go
--把该日记文件收缩到5M
dbcc ShrinkFile (N'BigValues_Log2',5, truncateonly) 
go

use [master]
go
--alter database [BigValues] set recovery full with no_wait
--go
alter database [BigValues] set recovery full	--还原为完全模式
go

--http://www.cnblogs.com/dunitian/p/6047709.html
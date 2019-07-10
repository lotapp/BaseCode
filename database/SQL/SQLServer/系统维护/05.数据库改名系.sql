--数据库改名系列（数据库名，逻辑名，物理文件名）
--http://www.cnblogs.com/dunitian/p/6165998.html
---------------------------------------------------

--修改数据库名（Test：修改前，NewTest：修改后）
alter database Test modify name=NewTest
go
--方法二
exec sp_renamedb 'Test','NewTest'
go

---------------------------------------------------

select * from sys.database_files

--修改数据库逻辑名（Test：旧逻辑名，NetTest：新逻辑名）
alter database NewTest modify file(name=N'Test', newname=N'NetTest')
go
alter database NewTest modify file(name=N'Test_log', newname=N'NetTest_log')
go

select * from sys.database_files

---------------------------------------------------
--修改物理文件名
--exec xp_cmdshell 'rename E:\SQL\Test.mdf NewTest.mdf'

--不一定切换到master，但是得切换一下数据库，不然就会出现正在使用不让分离的现象
use master
go
--1.分离
exec sp_detach_db NewTest
go

--2.改名（这一步可以换成手动改名字）
exec sp_configure 'show advanced options',1 --显示高级选项
reconfigure with override--重新配置
	exec sp_configure 'xp_cmdshell',1 --1代表允许，0代表阻止
	reconfigure with override
		exec xp_cmdshell 'rename E:\SQL\Test.mdf NewTest.mdf'
		go
		exec xp_cmdshell 'rename E:\SQL\Test_log.ldf NewTest_log.ldf'
		go
	exec sp_configure 'xp_cmdshell',0
	reconfigure with override
exec sp_configure 'show advanced options',0
reconfigure with override

--3.附加
exec sp_attach_db NewTest,N'E:\SQL\NewTest.mdf',N'E:\SQL\NewTest_log.ldf'

---------------------------------------------------
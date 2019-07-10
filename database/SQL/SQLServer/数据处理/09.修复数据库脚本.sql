--要是附加错误，则新建一个同名数据库，把数据库服务停止后 ==》替换数据库文件。
--然后进行下面步骤：

--1.设置为应急模式 （emergency 应急）
alter database BigData_TestInfo set emergency
go
--2.设置为单用户模式
alter database BigData_TestInfo set single_user
go
--3.快速修复（如果出现问题请试试, [Repair_Rebuild-重建索引并修复] 和 [Repair_Allow_Data_Loss-允许丢失数据的修复方式]）
dbcc checkdb ('BigData_TestInfo', Repair_Fast)
go

--4.恢复为多用户模式（如果出错就把其他查询窗口关掉）
alter database BigData_TestInfo set multi_user
go

--dbcc checkdb用法(手工修复数据库)
--检查数据库完整性
--dbcc checkdb('数据库名')
--go
--快速修复 
--dbcc checkdb ('数据库名', Repair_Fast)
--go
--重建索引并修复 
--dbcc checkdb ('数据库名', REPAIR_REBUILD)
--go
--如果必要允许丢失数据修复 
--dbcc checkdb ('数据库名', Repair_Allow_Data_Loss) 
--go
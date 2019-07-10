--查看当前数据库文件组信息
select * from sys.filegroups

--创建文件组
alter database BigData_TestInfo_PartialData add filegroup Info
go

--添加文件到文件组
alter database BigData_TestInfo_PartialData add file(name=N'TestInfo2006',filename=N'G:\SQLData\BigData_TestInfo2006.ndf') to filegroup Info
go

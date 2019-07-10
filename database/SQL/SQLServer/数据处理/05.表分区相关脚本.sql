--查看分区函数
select * from sys.partition_functions
--查看分区架构
select * from sys.partition_schemes

----------------------------------------------

--1.创建分区函数
if(Exists(select * from sys.partition_functions where name=N'CreatedatePartitionFun'))
	drop partition function CreatedatePartitionFun
create partition function CreatedatePartitionFun(varchar(10)) as range right for values(N'2006-01-01', N'2007-01-01', N'2009-01-01', N'2012-01-01')
go

----------------------------------------------

--2.创建分区方案
if(Exists(select * from sys.partition_functions where name=N'CreatedatePartitionScheme'))
	drop partition function CreatedatePartitionScheme
create partition scheme CreatedatePartitionScheme as partition [CreatedatePartitionFun] TO ([Info], [Info], [Info], [Info], [primary])
go

----------------------------------------------

--3.创建分区表
--3.1尚未创建
create table TestInfo(
	Id int identity(1,1) not null,
	QunNum int NOT NULL,
	MastQQ int,
	CreateDate varchar(10),
	Title varchar(22),
	Class varchar(38),
	QunText varchar(80)
) on CreatedatePartitionScheme(CreateDate) --on 指定分区架构(指定分区列)

--3.2已经存在
--3.2.1	把主键变为非聚集索引
----3.2.1.1先删除聚集索引
alter table Info drop constraint PK__Info__3214EC064B338648
go
----3.2.1.1再创建非聚集索引的主键
alter table Info add constraint PK_Info_Id primary key nonclustered (Id asc)
go

--3.2.2	创建分区聚集索引
create clustered index IX_Info_CreateDate on Info(CreateDate) on CreatedatePartitionScheme(CreateDate)
go

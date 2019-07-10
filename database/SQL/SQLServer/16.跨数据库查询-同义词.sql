--一个服务器，多个数据库
--跨数据库查询
select SId,SName,CName from [TestStudent].[dbo].[StudentInfo] as Student
inner join [TestMain].[dbo].[Class] as Class on Student.SClassId=Class.CId
go
----------------------------------------------------------------
--要是我手动改了数据库名或者表名岂不歇菜？所有就有了同义词
use TestMain
if(exists(select * from sys.synonyms where name='TestMainClass'))
	drop synonym TestMainClass
create synonym TestMainClass for [TestMain].[dbo].[Class]

if(exists(select * from  sys.synonyms where name='TestStudentInfo'))
	drop synonym TestStudentInfo
create synonym TestStudentInfo for [TestStudent].[dbo].[StudentInfo]

--跨数据库查询
use TestMain
select SId,SName,CName from TestStudentInfo as Student
inner join TestMainClass as Class on Student.SClassId=Class.CId
go
----------------------------------------------------------------

--多个服务器，多个数据库
--先链接服务器，再同义词
--跨数据库查询
select SId,SName,CName from [q***257691.my3w.com].[q***257691_db].[dbo].[StudentInfo] as Student
inner join [TestMain].[dbo].[Class] as Class on Student.SClassId=Class.CId
go
----------------------------------------------------------------
--要是我手动改了数据库名或者表名岂不歇菜？所有就有了同义词
use TestMain
if(exists(select * from sys.synonyms where name='TestMainClass'))
	drop synonym TestMainClass
create synonym TestMainClass for [TestMain].[dbo].[Class]

if(exists(select * from  sys.synonyms where name='TestStudentInfo'))
	drop synonym TestStudentInfo
create synonym TestStudentInfo for [q***257691.my3w.com].[q***257691_db].[dbo].[StudentInfo]

--跨数据库查询
use TestMain
select SId,SName,CName from TestStudentInfo as Student
inner join TestMainClass as Class on Student.SClassId=Class.CId
go

----------------------------------------------------------------

----------------------初始化数据----------------------------------
--use master
----测试表A
--if exists(select * from sysdatabases where Name=N'TestStudent')
--	drop database TestStudent
--CREATE DATABASE [TestStudent]
--go
--USE [TestStudent]
--if exists(select * from sysobjects where name=N'StudentInfo')
--	drop table StudentInfo
--CREATE TABLE [dbo].[StudentInfo]
--(
--	[SId] [int] IDENTITY(1,1) primary key,
--	[SName] [nvarchar](50) NOT NULL,
--	[SClassId] [int] NOT NULL
--)
--GO
--SET IDENTITY_INSERT [dbo].[StudentInfo] ON 
--INSERT [dbo].[StudentInfo] ([SId], [SName], [SClassId]) VALUES (1, N'滑头', 1)
--INSERT [dbo].[StudentInfo] ([SId], [SName], [SClassId]) VALUES (2, N'圆头', 2)
--INSERT [dbo].[StudentInfo] ([SId], [SName], [SClassId]) VALUES (3, N'方头', 1)
--SET IDENTITY_INSERT [dbo].[StudentInfo] OFF
--go

----测试表B
--if exists(select * from sysdatabases where Name=N'TestMain')
--	drop database TestMain
--CREATE DATABASE [TestMain]
--go
--USE [TestMain]
--if exists(select * from sysobjects where name=N'Class')
--	drop table Class
--CREATE TABLE [dbo].[Class]
--(
--	[CId] [int] IDENTITY(1,1) primary key,
--	[CName] [nvarchar](50) NOT NULL
--)
--GO
--SET IDENTITY_INSERT [dbo].[Class] ON 

--INSERT [dbo].[Class] ([CId], [CName]) VALUES (1, N'一年级')
--INSERT [dbo].[Class] ([CId], [CName]) VALUES (2, N'二年级')
--INSERT [dbo].[Class] ([CId], [CName]) VALUES (3, N'三年级')
--SET IDENTITY_INSERT [dbo].[Class] OFF
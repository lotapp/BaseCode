use master

--存在就删除
if exists(select * from sysdatabases where Name=N'NetCrazy_Shop')
begin
drop database NetCrazy_Shop
end

--创建数据库
create database NetCrazy_Shop
on primary					--数据库文件，主文件组
(
	name='NetCrazy_Shop_Data', --逻辑名
	size=10mb,				--初始大小
	filegrowth=10%,			--文件增长
	maxsize=1024mb,			--最大值
	filename=N'E:\SQL\NetCrazy_Shop_Data.mdf'--存放路径（包含文件后缀名）
)
log on --日记
(
	name='NetCrazy_Shop_Log',
	size=5mb,
	filegrowth=5%,
	filename=N'E:\SQL\NetCrazy_Shop_Log.ldf'
)
go

use NetCrazy_Shop
--存在就删除
if exists(select * from sysobjects where name=N'SeoTKD')
begin
drop table SeoTKD
end

--创建SeoTKD表
create table SeoTKD
(
	Gid varchar(36) primary key,
	SeoTitle nvarchar(100) default('标题') not null,	--最佳长度: 10 ~ 60 字符
	SeoKeyWords nvarchar(149) not null,
	SeoDescription nvarchar(249) not null,			--最佳长度: 50 ~ 160 字符
	SeoDataStatus tinyint default(0)				--0~255 size:1字节
)


--存在就删除
if exists(select * from sysobjects where name=N'Test')
begin
drop table Test
end

create table Test
(
	Tid int primary key identity,
	Title01 nvarchar(100) default('标题01'),	
	Title02 nvarchar(100) default('标题02'),	
	Title23 nvarchar(100) default('标题03'),
	DataStatus tinyint default(0)				--0~255 size:1字节
)
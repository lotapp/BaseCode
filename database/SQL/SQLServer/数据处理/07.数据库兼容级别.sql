--高版本降级到低版本
--1.导出为SQL脚本

--2.兼容性设置一下
--exec sp_dbcmptlevel BigData_TestInfo,levelNum

----查询版本：level:130（SQLServer 2016）
select name,[compatibility_level] from sys.databases where name=DB_Name()
go

--设置级别为2012【 level:130（SQLServer 2016）120（SQLServer 2014），110（SQLServer 2012），100（SQLServer 2008） 】
exec sp_dbcmptlevel BigData_TestInfo,110

----执行前版本：level:110（SQLServer 2012）
select name,[compatibility_level] from sys.databases where name=DB_Name()
go
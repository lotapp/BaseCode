--获取服务器名
select  @@servername
--删除服务
exec sp_dropserver '原来数据库名',null
--添加新的服务
exec sp_addserver '现在数据库名','LOCAL',null

-- 记得重启一下数据库服务

--http://www.cnblogs.com/dunitian/p/6041824.html

--网上的方法：
--if serverproperty('servername') <> @@servername
--begin
--declare @server sysname
--set @server = @@servername
--exec sp_dropserver @server = @server
--set @server = cast(serverproperty('servername') as sysname)
--exec sp_addserver @server = @server , @local = 'LOCAL'
--end
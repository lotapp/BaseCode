--数据库分离
exec sp_detach_db NewTest
go

--数据库附加（如果日记变动则重新创建日记，此时日记名和逻辑日记名相同）
exec sp_attach_db NewTest,N'E:\SQL\Test.mdf'

--完整写法
exec sp_attach_db NewTest,N'E:\SQL\Test.mdf',N'E:\SQL\Test_log.ldf'

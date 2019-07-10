--1.压缩
--正常备份数据库（完整备份）
backup database MyBlog to disk=N'G:\1.bak' with name=N'完整备份',description=N'2017完整备份'
go
--压缩版的完整备份
backup database MyBlog to disk=N'G:\2.bak' with name=N'完整备份-压缩',description=N'2017完整备份-压缩',compression,checksum
go

-------------------------------------------------

--3.备份检查
--备份是否有效
restore verifyonly from disk=N'G:\1.bak'
go
--检查备份集里面备份了哪些数据库文件
restore filelistonly from disk=N'G:\1.bak'
go
--备份文件信息
restore headeronly from disk=N'G:\1.bak'
go

-------------------------------------------------

--4.还原数据库
--if(Exists(select * from sys.databases where name=N'MyBlog'))
-- drop database MyBlog
restore database MyBlog from disk=N'G:\1.bak'
go

-------------------------------------------------

--5.加密备份
--备份服务主密钥
backup service master key to file='G:\service_master.key' encryption by password='Net@Linux&Core#1'
go

--在数据库上创建主密钥
create master key encryption by password='Net@Linux&Core#1'
go

open master key decryption by password='Net@Linux&Core#1'

--备份master key
backup master key to file='G:\master.key' encryption by password='Net@Linux&Core#1'
go


select * from sys.symmetric_keys

--第一层 服务主密钥 备份服务主密钥
--backup service master key to file='c:\smk.bak'
--encryption by password='P@ssw0rd'
 
--restore service master key from file='c:\smk.bak'
--decryption by password='P@ssw0rd'
 
--第二层 数据库主密钥
--1)必须先在该数据库上创建数据库主密钥才能使用
--create master key encryption by password='P@ssw0rd'
 
--2)使用数据库主密钥
--－如果数据库主密钥使用服务密钥进行保护，则在使用时会自动打开
--open master key decryption by password='P@ssw0rd'
 
--3)查看数据库主密钥状态
--sys.symmetric_keys
 
--4)备份数据库主密钥
--backup master key to file='c:\smk.bak'
--encryption by password='P@ssw0rd'
 
--restore master key from file='c:\smk.bak'
--decryption by password='P@ssw0rd'
--开启发邮件功能
exec sp_configure 'show advanced options', 1
reconfigure with override
go
exec sp_configure 'database mail xps', 1
reconfigure with override
go

--创建邮件帐户信息
exec msdb.dbo.sysmail_add_account_sp
     @account_name ='dunitian', -- 邮件帐户名称
     @email_address ='xxx@163.com', -- 发件人邮件地址
     @display_name ='SQLServer2014_192.168.36.250', -- 发件人姓名
     @MAILSERVER_NAME = 'smtp.163.com', -- 邮件服务器地址
     @PORT =25, -- 邮件服务器端口
     @USERNAME = 'xxx@163.com', -- 用户名
     @PASSWORD = '邮件密码或授权码' -- 密码（授权码）
GO

--数据库配置文件
exec msdb.dbo.sysmail_add_profile_sp
     @profile_name = 'SQLServer_DotNetCrazy', -- 配置名称
     @description = '数据库邮件配置文件' -- 配置描述
go

--用户和邮件配置文件相关联
exec msdb.dbo.sysmail_add_profileaccount_sp
     @profile_name = 'SQLServer_DotNetCrazy', -- 配置名称
     @account_name = 'dunitian', -- 邮件帐户名称
     @sequence_number = 1 -- account 在 profile 中顺序（默认是1）
go

----------------------------------------------------------------------------------------

-- 发邮件测试
exec msdb.dbo.sp_send_dbmail
     @profile_name = 'SQLServer_DotNetCrazy', --配置名称
     @recipients = 'dotnetcrazy@qq.com', --收件邮箱
     @body_format = 'HTML', --内容格式
     @subject = '文章标题', --文章标题
     @body = '邮件内容<br/><h2>This is Test</h2>...'--邮件内容
go
----------------------------------------------------------------------------------------

-- 查询相关
select * from msdb.dbo.sysmail_allitems --查看所有邮件消息
select * from msdb.dbo.sysmail_mailitems --查看邮件消息（更多列）

select * from msdb.dbo.sysmail_sentitems --查看已发送的消息
select * from msdb.dbo.sysmail_faileditems --失败状态的消息
select * from msdb.dbo.sysmail_unsentitems --看未发送的消息

select * from msdb.dbo.sysmail_event_log --查看记录日记
go



















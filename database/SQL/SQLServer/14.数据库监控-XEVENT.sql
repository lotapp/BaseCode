-- 切换到需要监控的数据库
USE [dotnetcrazy]
GO

--收集服务器上逻辑错误的信息
SET QUOTED_IDENTIFIER ON
SET ANSI_NULLS ON
GO

-- 自定义的错误信息表
IF OBJECT_ID('log_error_message') IS NULL
BEGIN
	CREATE TABLE [dbo].[log_error_message]
	(
	[login_message_id] [uniqueidentifier] NULL CONSTRAINT [DF__PerfLogic__Login__7ACA4E21] DEFAULT (newid()),
	[start_time] [datetime] NULL,
	[database_name] [nvarchar] (128) COLLATE Chinese_PRC_CI_AS NULL,
	[message] [nvarchar] (max) COLLATE Chinese_PRC_CI_AS NULL,
	[sql_text] [nvarchar] (max) COLLATE Chinese_PRC_CI_AS NULL,
	[alltext] [nvarchar] (max) COLLATE Chinese_PRC_CI_AS NULL,
	-- [worker_address] [nvarchar] (1000) COLLATE Chinese_PRC_CI_AS NULL,
	[username] [nvarchar] (1000) COLLATE Chinese_PRC_CI_AS NULL,
	[client_hostname] [nvarchar] (1000) COLLATE Chinese_PRC_CI_AS NULL,
	[client_app_name] [nvarchar] (1000) COLLATE Chinese_PRC_CI_AS NULL
	) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
END
GO

-- 创建存储过程
CREATE PROCEDURE [dbo].[event_error_monitor]
AS
    IF NOT EXISTS( SELECT 1 FROM sys.dm_xe_sessions dxs(NOLOCK) WHERE name = 'event_error_monitor') -- 不存在就创建EVENT
        -- 创建扩展事件，并把数据放入内存中
        BEGIN
            CREATE EVENT session event_error_monitor on server
            ADD EVENT sqlserver.error_reported -- error_reported扩展事件
            (
            ACTION -- 返回结果
            (
            sqlserver.session_id, -- 会话id
            sqlserver.plan_handle, -- 计划句柄，可用于检索图形计划
            sqlserver.tsql_stack, -- T-SQ堆栈信息
            package0.callstack, -- 当前调用堆栈
            sqlserver.sql_text, -- 遇到错误的SQL查询
            sqlserver.username, -- 用户名
            sqlserver.client_app_name, -- 客户端应用程序名称
            sqlserver.client_hostname, -- 客户端主机名
            -- sqlos.worker_address, -- 当前任务执行时间
            sqlserver.database_name -- 当前数据库名称
            )
            WHERE severity >= 11 AND Severity <=16 -- 指定用户级错误
            )
            ADD TARGET package0.ring_buffer -- 临时放入内存中
            WITH (max_dispatch_latency=1seconds)

            -- 启动监控事件
            ALTER EVENT SESSION event_error_monitor on server state = START
        END
    ELSE
        -- 存储过程已经存在就把数据插入表中
        BEGIN
            -- 将内存中已经收集到的错误信息转存到临时表中（方便处理）
            SELECT
                DATEADD(hh,
                        DATEDIFF(hh, GETUTCDATE(), CURRENT_TIMESTAMP),
                        n.value('(event/@timestamp)[1]', 'datetime2')) AS [timestamp],
                n.value('(event/action[@name="database_name"]/value)[1]', 'nvarchar(128)') AS [database_name],
                n.value('(event/action[@name="sql_text"]/value)[1]', 'nvarchar(max)') AS [sql_text],
                n.value('(event/data[@name="message"]/value)[1]', 'nvarchar(max)') AS [message],
                n.value('(event/action[@name="username"]/value)[1]', 'nvarchar(max)') AS [username],
                n.value('(event/action[@name="client_hostname"]/value)[1]', 'nvarchar(max)') AS [client_hostname],
                n.value('(event/action[@name="client_app_name"]/value)[1]', 'nvarchar(max)') AS [client_app_name],
                n.value('(event/action[@name="tsql_stack"]/value/frames/frame/@handle)[1]', 'varchar(max)') AS [tsql_stack],
                n.value('(event/action[@name="tsql_stack"]/value/frames/frame/@offsetStart)[1]', 'int') AS [statement_start_offset],
                n.value('(event/action[@name="tsql_stack"]/value/frames/frame/@offsetEnd)[1]', 'int') AS [statement_end_offset]
            into #error_monitor -- 临时表
            FROM
            (    SELECT td.query('.') as n
                FROM
                (
                    SELECT CAST(target_data AS XML) as target_data
                    FROM sys.dm_xe_sessions AS s
                    JOIN sys.dm_xe_session_targets AS t
                        ON t.event_session_address = s.address
                    WHERE s.name = 'event_error_monitor'
                    --AND t.target_name = 'ring_buffer'
                ) AS sub
                CROSS APPLY target_data.nodes('RingBufferTarget/event') AS q(td)
            ) as TAB

            -- 把数据存储到自己新建的表中（有SQL语句的直接插入到表中）
            INSERT INTO log_error_message(start_time,database_name,message,sql_text,alltext,username,client_hostname,client_app_name)
            SELECT TIMESTAMP,database_name,[message],sql_text,'',username,client_hostname,client_app_name
            FROM #error_monitor as a
            WHERE a.sql_text != '' --AND client_app_name !='Microsoft SQL Server Management Studio - 查询'
            AND a.MESSAGE NOT LIKE '找不到会话句柄%' AND a.MESSAGE NOT LIKE '%SqlQueryNotification%' --排除server broker
            AND a.MESSAGE NOT LIKE '远程服务已删除%'

            -- 插入应用执行信息（没有SQL的语句通过句柄查询下SQL）
            INSERT INTO log_error_message(start_time,database_name,message,sql_text,alltext,username,client_hostname,client_app_name)
            SELECT TIMESTAMP,database_name,[message],
            SUBSTRING(qt.text,a.statement_start_offset/2+1,
                        (case when a.statement_end_offset = -1
                        then DATALENGTH(qt.text)
                        else a.statement_end_offset end -a.statement_start_offset)/2 + 1) sql_text,qt.text alltext,
            username,client_hostname,client_app_name
            FROM #error_monitor as a
            CROSS APPLY sys.dm_exec_sql_text(CONVERT(VARBINARY(max),a.tsql_stack,1)) qt -- 通过句柄查询具体的SQL语句
            WHERE a.sql_text IS NULL AND tsql_stack != '' --AND client_app_name = '.Net SqlClient Data Provider'

            DROP TABLE #error_monitor -- 删除临时表

            --重启清空
            ALTER EVENT SESSION event_error_monitor ON SERVER STATE = STOP
            ALTER EVENT SESSION event_error_monitor on server state = START
        END

    -- 美化版预警邮箱
    DECLARE @body_html VARCHAR(max)
    set @body_html = '<table style="width:100%" cellspacing="0"><tr><td colspan="6" align="center" style="font-weight:bold;color:red">数据库错误监控</td></tr>'
    set @body_html = @body_html + '<tr style="text-align: left;"><th>运行时间</th><th>数据库</th><th>发生错误的SQL语句</th><th>消息</th><th>用户名</th><th>应用</th><th>应用程序名</th></tr>'
    -- 格式处理（没内容就空格填充）
    select @body_html = @body_html + '<tr><td>'
        + case (isnull(start_time, '')) when '' then '&nbsp;' else convert(varchar(20), start_time, 120) end + '</td><td>'
        + case (isnull(database_name, '')) when '' then '&nbsp;' else database_name end + '</td><td>'
        + case (isnull(sql_text, '')) when '' then '&nbsp;' else sql_text end + '</td><td>'
        + case (isnull(message, '')) when '' then '&nbsp;' else message end + '</td><td>'
        + case (isnull(username, '')) when '' then '&nbsp;' else username end + '</td><td>'
        + case (isnull(client_hostname, '')) when '' then '&nbsp;' else client_hostname end + '</td><td>'
        + case (isnull(client_app_name, '')) when '' then '&nbsp;' else client_app_name end + '</td></tr>'
    from (
             select start_time, database_name,sql_text, message, username, client_hostname, client_app_name
             from [dbo].[log_error_message]
             where start_time >= dateadd(hh,-2,getdate()) -- 当前时间 - 定时任务的时间间隔（2h）
               and client_app_name != 'Microsoft SQL Server Management Studio - 查询' -- and client_hostname in('')
         ) as temp_message
    set @body_html= @body_html+'</table>'

    -- 发送警告邮件
    exec msdb.dbo.sp_send_dbmail
    @profile_name = 'SQLServer_DotNetCrazy',         --配置名称
    @recipients = 'dotnetcrazy@qq.com',              --收件邮箱
    @body_format = 'HTML',                           --内容格式
    @subject = '数据库监控通知',                       --文章标题
    @body = @body_html --邮件内容
go

---------------------------------------------------------------------------------------------------------------------------------------------------

-- 定时任务只要执行下存储过程就可以实现数据库监控了
select 1/0; -- eg：摸拟一个错误
exec event_error_monitor;

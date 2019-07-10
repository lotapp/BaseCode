--"无法删除数据库，因为该数据库当前正在使用"问题解决

--Start：Kill掉正在占用数据库的进程
use master    
go   

declare @dbname sysname
set @dbname = 'BigValuesTest' --这个是要删除的数据库库名

declare @s nvarchar(1000)
declare tb cursor local
for
    select s = 'kill   ' + cast(spid as varchar)
    from   master.dbo.sysprocesses
    where  dbid = DB_ID(@dbname)

open tb
fetch next from tb into @s
while @@fetch_status = 0
begin
    exec (@s)
    fetch next from tb into @s
end
close tb
deallocate tb 
--End：Kill掉正在占用数据库的进程

--执行你的操作（eg:删除数据库）
exec ('drop   database   [' + @dbname + ']')

--http://www.cnblogs.com/dunitian/p/6047760.html
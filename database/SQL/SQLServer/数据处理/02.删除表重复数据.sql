--模拟数据
select * into TestDB from(
select 'a' A,1 B union all
select 'b',2 union all
select 'b',2 union all
select 'b',2 ) as bbp

--方法一：
select distinct * into #Temp from TestDB
drop table TestDB
select * into TestDB from #Temp
drop table #Temp


--方法二：
delete DB from (select row_number() over(partition by A,B order by A) ID,* from TestDB)DB
where ID>1

--http://www.cnblogs.com/dunitian/p/6041323.html 第七题
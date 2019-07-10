--创建聚集索引
if exists(select * from sysindexes where name='IX_ShopMenuBak_MId')
 drop index ShopMenuBak.IX_ShopMenuBak_MId
create clustered  index  IX_ShopMenuBak_MId
on ShopMenuBak(Mid)
go

--创建一般索引（默认升序）
if exists(select * from sysindexes where name='IX_ShopMenuBak_MName')
 drop index ShopMenuBak.IX_ShopMenuBak_MName
create index  IX_ShopMenuBak_MName
on ShopMenuBak(MName)
go

--扩充：创建一般索引（设置降序）
if exists(select * from sysindexes where name='IX_ShopMenuBak_MName')
 drop index ShopMenuBak.IX_ShopMenuBak_MName
create  index  IX_ShopMenuBak_MName
on ShopMenuBak(MName desc)
go

--恶补知识点：
--聚集索引---意味着排序（物理排序，索引字段一般都是唯一的）
--聚集索引---索引页的顺序就是索引所指向的数据的顺序,当创建主键后无法手动创建其它聚索引。但先创建聚集索引，再创建主键就可以让主键不是聚集索引
--非聚集索引-索引页的顺序与索引所指向的数据的顺序无关（逻辑排序，按照索引页来查找数据）

--索引的作用：
--1.为了提高查询的效率的
--2.每一次增加删除和修改也会修改或者刷新索引页(所有增删改比较耗时)
--3.索引可以理解为引用数据，所以它也需要存储空间
--插入数据

--推荐写法 output
insert into ShopModelBak
output inserted.SId
values(N'222',1,99)

--另一种写法 scope_Identity()（可以得到当前范围内最近插入行生成的标示值）
insert into ShopModelBak values(N'bbb',1,99)
select scope_Identity()

----不推荐：（@@Identity就不一定是当前范围内了） @@identity
insert into ShopModelBak values(N'lll',1,99)
select @@identity

--返回多个值
insert into ShopModelBak
output inserted.SId,inserted.SName,inserted.SOrder,inserted.SDataStatus
values(N'333',1,99)
--非存储过程
select * from(select row_number() over(order by MType) Id,CPName,CName,SName,MType,MName,Mprice from ShopMenu 
inner join ShopModel on ShopMenu.MShopId=ShopModel.SId
inner join View_CityData on ShopMenu.MCityId=CId) as temp
where Id<= 1 * 10 and Id>(1-1)*10

------------------------------------------------------------------------

--存储过程
if exists(select * from sysobjects where name='usp_GetShopMenus_Page')
	drop proc usp_GetShopMenus_Page
go
create proc usp_GetShopMenus_Page
@mIndex int,@mCount int=7
as
begin
	select * from(select row_number() over(order by MType) Id, CPName,CName,SName,MType,MName,Mprice from ShopMenu 
	inner join ShopModel on ShopMenu.MShopId=ShopModel.SId
	inner join View_CityData on ShopMenu.MCityId=CId) as temp
	where Id > (@mIndex-1)*@mCount  and Id<=(@mIndex)*@mCount
	return (select count(1) from ShopMenu)
end
go
declare @total int,@index int=1,@count int=9
exec @total=usp_GetShopMenus_Page @index,@count
select @index Mindex,@count MCount, @total MTotal

------------------------------------------------------------------------

--带查询条件的-非存储过程
select * from
(
	select row_number() over(order by NCreateTime) Id,* from
	(
		select NId,NTitle,NAuthor,NHitCount,NPush,NDataStatus,NCreateTime,NUpdateTime from NoteInfo
		where NTitle like '%1%' and NDataStatus=1		
	) TempA
) as TempInfo 
where TempInfo.Id<= 1 * 10 and TempInfo.Id>(1-1)*10

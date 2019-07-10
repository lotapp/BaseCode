--约束系列
----添加主键
alter table Info
  add constraint PK_Id_Index primary key (Id)
go

------------------------------------------------------------------
--列操作
----添加某一列
alter table Info
  add Id int identity (1,1) primary key
go

----删除某一列
alter table Info
  drop column Id
go

------------------------------------------------------------------

-- 3.1.添加一列 alter table tb_name add 列名 数据类型 修饰符
-- 在email后面添加手机号码列
-- 手机号不会用来做数学运算，varchar可以模糊查询(eg：like ‘138%’)，牵扯到国家代号时，可能出现+、-、()等字符，eg：+86
alter table Info
  add tel varchar(20) not null;

-- 3.1.1.添加含唯一键的列
-- 先添加列
alter table Info
  add uid bigint not null
-- 再添加约束 alter table tb_name add constraint uq_name
alter table Info
  add constraint uq_users_uid unique (uid); -- 自定义名称

-- 3.1.2.定义和约束一步走（系统设置名字）
-- alter table Info
--   add uid bigint not null unique; -- 默认名称

-- 3.2.含唯一键的列
-- 3.2.1.删除约束 alter table tb_name drop constraint uq_name
if exists(select *
          from sysobjects
          where name = 'uq_users_uid')
alter table Info
  drop constraint uq_users_uid;

-- 3.2.2.删除列 alter table tb_name drop column 字段名
alter table Info
  drop column uid;

-- 3.3.修改字段
-- 3.3.1.修改列名：exec sp_rename '表名.旧列名','新列名';
exec sp_rename 'users.ucode', 'usercode';

-- 3.3.2.添加默认值：`alter table tb_name alter 列名 set default df_value`
alter table dotnetcrazy.dbo.users
  add default '7c4a8d09ca3762af61e59520943dc26494f8941b' for password;
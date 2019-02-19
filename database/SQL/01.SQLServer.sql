-- -------------------------------------------------------------------------------
-- ----------------------------1.创建数据库----------------------------------------
use master

--存在就删除
if exists(select *
          from sysdatabases
          where Name = N'dotnetcrazy')
    begin
        drop database dotnetcrazy
    end

--创建数据库（简化版：create database dotnetcrazy）
create database dotnetcrazy
    on primary --数据库文件，主文件组
    (
        name ='dotnetcrazy_Data', --逻辑名
        size =10 mb, --初始大小
        filegrowth =10%, --文件增长
        maxsize =1024 mb, --最大值
        filename =N'D:\Works\SQL\dotnetcrazy_data.mdf'--存放路径（包含文件后缀名）
        )
    log on --日记
    (
        name ='dotnetcrazy_Log',
        size =5 mb,
        filegrowth =5%,
        filename =N'D:\Works\SQL\dotnetcrazy_log.ldf'
        );

-- 切换数据库
use dotnetcrazy;
-- -------------------------------------------------------------------------------
-- -----------------------------2.创建表-------------------------------------------
--存在就删除表
if exists(select *
          from sysobjects
          where name = N'users')
    begin
        drop table users
    end

-- dotnetcrazy.dbo.users
create table users
(
    id         int identity,                                      -- 主键，自增长
    username   nvarchar(20) not null,
    email      varchar(50)  not null,
    password   char(40)     not null,                             -- sha1
    ucode      char(36)     not null default newid(),             -- guid
    createtime datetime     not null default getdate(),
    updatetime datetime     not null default getdate(),
    datastatus tinyint      not null default 0,                   -- 默认值为0
    primary key (id),                                             -- 主键可多列
    unique (email),
    index ix_users_createtime_updatetime (createtime, updatetime) -- 索引
);

select getdate() as datatime, newid() as uuid;

-- # PS：MySQL自增长是`auto_increment`，MSSQL是`identity`
-- # PS：MySQL可以设置无符号`unsigned`，MSSQL不可以直接设置无符号整型，需要通过约束之类的来限制
-- # PS：现在新版本数据库兼容了SQLServer的nvarchar写法（`执行成功后数据类型变成varchar`）

-- -------------------------------------------------------------------------------
-- -----------------------------3.修改表-------------------------------------------

-- 3.1.添加一列 alter table tb_name add 列名 数据类型 修饰符
-- 在email后面添加手机号码列
-- 手机号不会用来做数学运算，varchar可以模糊查询(eg：like ‘138%’)，牵扯到国家代号时，可能出现+、-、()等字符，eg：+86
alter table users
    add tel varchar(20) not null;

-- 3.1.1.添加含唯一键的列
-- 先添加列
alter table users
    add uid bigint not null
-- 再添加约束 alter table tb_name add constraint uq_name
alter table users
    add constraint uq_users_uid unique (uid); -- 自定义名称

-- 3.1.2.定义和约束一步走（系统设置名字）
-- alter table users
--   add uid bigint not null unique; -- 默认名称

-- 3.2.含唯一键的列
-- 3.2.1.删除约束 alter table tb_name drop constraint uq_name
if exists(select *
          from sysobjects
          where name = 'uq_users_uid')
alter table users
    drop constraint uq_users_uid;

-- 3.2.2.删除列 alter table tb_name drop column 字段名
alter table users
    drop column uid;
-- -------------------------------------------------------------------------------
-- 3.3.修改字段
-- 3.3.1.修改列名：exec sp_rename '表名.旧列名','新列名';
exec sp_rename 'users.ucode', 'usercode';

-- 3.3.2.修改字段类型
alter table users
    alter column username varchar(25) not null;

-- 3.3.3.添加默认值：`alter table tb_name alter 列名 set default df_value`
alter table users
    add default '7c4a8d09ca3762af61e59520943dc26494f8941b' for password;

-- -------------------------------------------------------------------------------
-- -----------------------------4.增删改查（CURD）-------------------------------------
-- 4.1.插入 help insert
-- 自增长主键和默认值的字段可以不写
insert into dotnetcrazy.dbo.users(username, password, email, tel, usercode, createtime, updatetime, datastatus)
values ('dnt', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'dnt@qq.com', '18738002038', newid(), getdate(), getdate(),
        1);

-- 批量插入 SQLServer一次批量插入最多1000行左右
insert into dotnetcrazy.dbo.users(username, password, email, tel, usercode, createtime, updatetime, datastatus)
values ('xxx', '7c4a8d09ca3762af61e59520943dc26494f8942b', 'xxx@qq.com', '13738002038', newid(), getdate(), getdate(),
        0),
       ('mmd', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'mmd@qq.com', '13738002038', newid(), getdate(), getdate(),
        1),
       ('小明', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'xiaoming@qq.com', '13718002038', newid(), getdate(),
        getdate(), 1),
       ('小张', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'zhang@qq.com', '13728002038', newid(), getdate(), getdate(),
        1),
       ('小潘', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'pan@qq.com', '13748002038', newid(), getdate(), getdate(),
        1),
       ('小周', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'zhou@qq.com', '13758002038', newid(), getdate(), getdate(),
        1),
       ('小罗', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'luo@qq.com', '13768002038', newid(), getdate(), getdate(),
        1);

-- 4.2.修改 help update
update dotnetcrazy.dbo.users
set datastatus=99,
    updatetime = getdate()
where username = 'mmd'; -- 一定要有where条件！开发中一般都是先写where条件再写update

-- 4.3.删除
-- 删除数据（自增长不重置）help delete;
delete
from dotnetcrazy.dbo.users
where datastatus = 0;

-- 删除全部数据（自增长重置）help truncate;
truncate table dotnetcrazy.dbo.users;

-- ------------------------------------------------------------------------
-- 4.4.查询 help select
-- 编号，文件名，文件MD5，Meta(媒体类型)，当前用户，请求IP，来源地址，请求时间，数据状态
--存在就删除表
if exists(select *
          from sysobjects
          where name = N'file_records')
    begin
        drop table file_records
    end
-- 因为SQLServer的int没有unsigned，所以推荐使用bigint
create table file_records
(
    id         bigint identity primary key,
    file_name  varchar(100) not null,
    md5        char(32)     not null,
    meta_type  tinyint      not null default 1,
    user_id    int          not null,
    ip         bigint       not null, -- 在程序中自行转换
    url        varchar(200) not null default '/',
    createtime datetime     not null default getdate(),
    datastatus tinyint      not null default 0
);

-- 可以插入3次（方便下面演示）
insert into file_records(file_name, md5, meta_type, user_id, ip, url, createtime, datastatus)
values ('2.zip', '3aa2db9c1c058f25ba577518b018ed5b', 2, 1, 736264195, 'http://baidu.com', getdate(), 1),
       ('3.rar', '6f401841afd127018dad402d17542b2c', 3, 3, 736103427, 'http://qq.com', getdate(), 1),
       ('7.jpg', 'fe5df232cafa4c4e0f1a0294418e5660', 4, 5, 978522371, 'http://360.cn', getdate(), 1),
       ('9.png', '7afbb1602613ec52b265d7a54ad27330', 5, 4, 1728288771, 'http://cnblogs.com', getdate(), 1),
       ('1.gif', 'b5e9b4f86ce43ca65bd79c894c4a924c', 6, 3, 1914437635, 'http://qq.com', getdate(), 1),
       ('大马.jsp', 'abbed9dcc76a02f08539b4d852bd26ba', 9, 4, 3702877362, 'http://baidu.com', getdate(),
        99);

-- 查询来源url（去重后）
select distinct url
from file_records;

-- 查询来源url（分组方式）
select url
from file_records
group by url;

-- 分别统计一下url出现的次数（分组+聚合）
-- 分组一般都和聚合函数一起使用
select url, count(*) as count
from file_records
group by url;

-- 分别统计一下url出现的次数，已经删除的文件不算进去
select url, count(*) as count
from file_records
group by url
having count(*) > 3; -- 在group by的结果上筛选，★写成count就不行了★

-- 分别统计一下url出现的次数并查出对应的id
-- SQLServer2017新增string_agg
select ids =(select stuff((select ',' + cast(id as varchar(20))
                           from file_records as f
                           where f.url = file_records.url for xml path ('')), 1, 1, '')),
            url
from file_records
group by url;

-- ------------------------ 课后拓展 -------------------------------------------

-- 类似于concat的效果
select cast(id as varchar(20)) + ','
from file_records for xml path ('');

-- 移除多余的字符
-- STUFF（<character_expression>，<开始>，<长度>，<character_expression>）
-- 将字符串插入到另一个字符串中。它会删除开始位置第一个字符串中的指定长度的字符，然后将第二个字符串插入到开始位置的第一个字符串中
select stuff((select ',' + cast(id as varchar(20))
              from file_records for xml path ('')), 1, 1, '');

-- ------------------------------------------------------------------------
-- 内连接查询 innet join tb_name on 关联条件
select file_records.id,
       users.id as uid,
       users.username,
       users.email,
       file_records.file_name,
       file_records.md5,
       file_records.ip,
       file_records.url
from users
         inner join file_records on file_records.user_id = users.id -- 连接条件
where users.datastatus = 1
  and file_records.datastatus = 1
order by file_records.file_name desc; -- 文件名降序排序

-- 显示前5个数据
select top 5 *
from file_records;

-- 分页查询 第3页，每页5条
select *
from (select row_number() over (order by username desc, file_name desc) as id,
             file_records.id                                            as fid,
             users.id                                                   as uid,
             users.username,
             users.email,
             file_records.file_name,
             file_records.md5,
             file_records.ip,
             file_records.url
      from file_records
               inner join users on file_records.user_id = users.id) as temp
where id > (3 - 1) * 5
  and id <= 3 * 5;
-- ------------------------------------------------------------------------

-- 简单提一下视图：
-- 存在就删除
if exists(select *
          from sysobjects
          where name = N'view_userinfo')
    begin
        drop view view_userinfo
    end
-- 创建视图
create view view_userinfo as
select id, username, password, email, tel, datastatus
from users;

-- 查询视图
select id, username, password, email, tel, datastatus
from view_userinfo;

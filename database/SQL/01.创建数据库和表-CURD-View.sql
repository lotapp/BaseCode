-- -------------------------------------------------------------------------------
-- 显示数据库版本 MariaDB 5.5.60、MySQL 5.7
select version();

-- 当前用户信息
select user();

-- 显示已存在的数据库（权限范围内）
show databases;

-- ----------------------------1.创建数据库----------------------------------------
-- 如果存在就删除数据库 drop database dotnetcrazy
drop database if exists dotnetcrazy;

-- 创建数据库 create database dotnetcrazy (含特殊符号就用`反单引号`括起来)
create database if not exists dotnetcrazy charset utf8;

-- 查看创建数据库的语句
show create database dotnetcrazy;

-- -------------------------------------------------------------------------------
-- 切换到指定数据库
use dotnetcrazy;

-- 查看当前使用的数据库
select database();

-- 查看当前数据库中所有的表
show tables;

-- -----------------------------2.创建表-------------------------------------------
-- 如果存在就删除表 drop table users
drop table if exists dotnetcrazy.users;

-- select now() as datatime, uuid() as uuid;

-- mysql> help create table（低版本的默认值不支持函数）
-- 创建表 create table users(字段名 类型 修饰符,...)
create table if not exists dotnetcrazy.users
(
    id         int unsigned auto_increment,                       -- 主键，自增长【获取ID：last_insert_id()】
    username   varchar(20) not null,
    password   char(40)    not null,                              -- sha1：40
    email      varchar(50) not null,
    ucode      char(36)    not null,-- default uuid(),          -- uuid
    createtime datetime    not null,-- default now(),
    updatetime datetime    not null,-- default now(),
    datastatus tinyint     not null default 0,                    -- 默认值为0
    primary key (id),                                             -- 主键可多列
    unique uq_users_email (email),
    index ix_users_createtime_updatetime (createtime, updatetime) -- 索引，不指定名字默认就是字段名
)
--   表选项
--   engine = 'innodb', -- 引擎
--   character set utf8, -- 字符集
--   collate utf8_general_ci, -- 排序规则
;

-- 显示表结构 desc users
desc dotnetcrazy.users;

-- 显示创建表的语句 show create table users
show create table dotnetcrazy.users;

-- PS：MySQL自增长是`auto_increment`，MSSQL是`identity`
-- PS：MySQL可以设置无符号`unsigned`，MSSQL不可以直接设置无符号整型，需要通过约束之类的来限制
-- PS：现在新版本数据库兼容了SQLServer的nvarchar写法（`执行成功后数据类型变成varchar`）【不推荐使用】

-- -------------------------------------------------------------------------------
-- -----------------------------3.修改表-------------------------------------------
-- 修改表 mysql> help alter table

-- 3.1.添加一列 alter table tb_name add 列名 数据类型 修饰符 [first | after 列名]
alter table dotnetcrazy.users
    add uid bigint not null unique first; -- MSSQL没有[first | after 列名]

-- 在email后面添加手机号码列
-- 手机号不会用来做数学运算，varchar可以模糊查询(eg：like ‘138%’)，牵扯到国家代号时，可能出现+、-、()等字符，eg：+86
alter table dotnetcrazy.users
    add tel varchar(20) not null after email;

-- 3.2.删除一列 alter table tb_name drop 字段名
alter table dotnetcrazy.users
    drop uid;
-- -------------------------------------------------------------------------------

-- 3.3.添加索引 alter table tb_name add index [ix_name] (列名,...)
alter table dotnetcrazy.users
    add index ix_users_ucode (ucode); -- 不指定名字默认就是字段名
-- add index (ucode, tel); -- 不指定索引名字，默认就是第一个字段名

-- 添加唯一键 alter table tb_name add unique [uq_name] (列名,列名2...)
alter table dotnetcrazy.users
    add unique uq_users_tel_ucode (tel, ucode);
-- add unique (tel, ucode);-- 不指定索引名字，默认就是第一个字段名

-- 3.4.删除索引 alter table tb_name drop index ix_name
alter table dotnetcrazy.users
    drop index ix_users_ucode;

-- 删除索引（唯一键) alter table tb_name drop index uq_name
alter table dotnetcrazy.users
    drop index uq_users_tel_ucode;
-- drop index tel; -- 唯一键的索引名就是第一个列名
-- -------------------------------------------------------------------------------

-- 3.5.修改字段
-- 1.修改字段名：`alter table tb_name change 旧列名 新列名 类型 类型修饰符`
-- 此时一定要重新指定该列的类型和修饰符
alter table dotnetcrazy.users
    change ucode usercode char(36); -- default uuid();

-- 2.修改字段类型
alter table dotnetcrazy.users
    modify username varchar(25) not null;

-- 3.添加默认值：`alter table tb_name alter 列名 set default df_value`
alter table dotnetcrazy.users
    alter password set default '7c4a8d09ca3762af61e59520943dc26494f8941b';

-- -------------------------------------------------------------------------------
-- 详情请查看： https://www.cnblogs.com/dotnetcrazy/p/10374091.html
select @@sql_mode; -- 查询SQL_Mode

-- -----------------------------4.增删改查（CURD）-------------------------------------
desc dotnetcrazy.users;

-- 4.1.插入 help insert
-- 自增长主键和默认值的字段可以不写
insert into dotnetcrazy.users(username, password, email, tel, usercode, createtime, updatetime, datastatus)
values ('dnt', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'dnt@qq.com', '18738002038', uuid(), now(), now(), 1);

-- 批量插入
insert into dotnetcrazy.users(username, password, email, tel, usercode, createtime, updatetime, datastatus)
values ('xxx', '7c4a8d09ca3762af61e59520943dc26494f8942b', 'xxx@qq.com', '13738002038', uuid(), now(), now(), 0),
       ('mmd', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'mmd@qq.com', '13738002038', uuid(), now(), now(), 1),
       ('小明', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'xiaoming@qq.com', '13718002038', uuid(), now(), now(), 1),
       ('小张', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'zhang@qq.com', '13728002038', uuid(), now(), now(), 1),
       ('小潘', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'pan@qq.com', '13748002038', uuid(), now(), now(), 1),
       ('小周', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'zhou@qq.com', '13758002038', uuid(), now(), now(), 1),
       ('小罗', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'luo@qq.com', '13768002038', uuid(), now(), now(), 1);

-- 4.2.修改 help update
update dotnetcrazy.users
set datastatus=99,
    updatetime = now()
where username = 'mmd'; -- 一定要有where条件！开发中一般都是先写where条件再写update

-- 4.3.删除
-- 删除数据（自增长不重置）help delete;
delete
from dotnetcrazy.users
where datastatus = 0;

-- 删除全部数据（自增长重置）help truncate;
-- truncate table dotnetcrazy.users;

-- ------------------------------------------------------------------------
-- 4.4.查询 help select
-- 编号，文件名，文件MD5，Meta(媒体类型)，当前用户，请求IP，来源地址，请求时间，数据状态
drop table if exists file_records;
create table if not exists file_records
(
    id         int unsigned auto_increment primary key,
    file_name  varchar(100)     not null,
    md5        char(32)         not null,
    meta_type  tinyint unsigned not null default 1,
    user_id    int unsigned     not null,
    ip         int unsigned     not null,
    url        varchar(200)     not null default '/',
    createtime datetime         not null, -- default now(),
    datastatus tinyint          not null default 0
);

desc dotnetcrazy.file_records;
show create table dotnetcrazy.file_records;

-- 把ip转换成int
select inet_aton('43.226.128.3'); -- inet6_aton()
-- 把int转换成ip
select inet_ntoa('736264195'); -- inet6_ntoa() ipv6

-- truncate table dotnetcrazy.file_records;
-- 可以插入3次（方便下面演示）
insert into file_records(file_name, md5, meta_type, user_id, ip, url, createtime, datastatus)
values ('2.zip', '3aa2db9c1c058f25ba577518b018ed5b', 2, 1, inet_aton('43.226.128.3'), 'http://baidu.com', now(), 1),
       ('3.rar', '6f401841afd127018dad402d17542b2c', 3, 3, inet_aton('43.224.12.3'), 'http://qq.com', now(), 1),
       ('7.jpg', 'fe5df232cafa4c4e0f1a0294418e5660', 4, 5, inet_aton('58.83.17.3'), 'http://360.cn', now(), 1),
       ('9.png', '7afbb1602613ec52b265d7a54ad27330', 5, 4, inet_aton('103.3.152.3'), 'http://cnblogs.com', now(), 1),
       ('1.gif', 'b5e9b4f86ce43ca65bd79c894c4a924c', 6, 3, inet_aton('114.28.0.3'), 'http://qq.com', now(), 1),
       ('大马.jsp', 'abbed9dcc76a02f08539b4d852bd26ba', 9, 4, inet_aton('220.181.108.178'), 'http://baidu.com', now(),
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
having count > 3; -- 在group by的结果上筛选

-- 分别统计一下url出现的次数并查出对应的id
select group_concat(id) as ids, url
from file_records
group by url;

-- ------------------------ 课后拓展 -------------------------------------------
-- 将多个字符串连接成一个字符串
select concat(user_id, ',', file_name, ',', ip, ',', url) as concat_str
from file_records;

-- 将多个字符串连接成一个字符串+可以一次性指定分隔符
select concat_ws(',', user_id, file_name, ip, url) as concat_str
from file_records;

-- 在有group by的查询语句中，select指定的字段要么就包含在group by语句的后面，作为分组的依据，要么就包含在聚合函数中
-- group_concat()：将group by产生的同一个分组中的值连接起来，返回一个字符串结果
select group_concat(file_name) as file_name, url, count(*)
from file_records
group by url;

-- having一般对group by的结果进行筛选，where是对原表进行筛选
select group_concat(file_name) as file_name, group_concat(url) as url, count(*) as count
from file_records
group by url
having count >= 3;

-- 四舍五入到指定位数
select round(3.12345, 4);
-- 存小数数据为了不损伤精读一般都是转成整数，eg：3.1415 ==> 整数：31415，倍数：10000
-- ------------------------------------------------------------------------

-- 内连接查询 innet join tb_name on 关联条件
select file_records.id,
       users.id                   as uid,
       users.username,
       users.email,
       file_records.file_name,
       file_records.md5,
       inet_ntoa(file_records.ip) as ip,
       file_records.url
from users
         inner join file_records on file_records.user_id = users.id -- 连接条件
where users.datastatus = 1
  and file_records.datastatus = 1
order by file_records.file_name desc; -- 文件名降序排序


-- MySQL没有`select top n`语法，可以使用 limit来实现，eg：top 5
select *
from file_records
limit 5; -- limit 0,5

-- 分页查询
-- page:1,count=5 ==> 0,5 ==> (1-1)*5,5
-- page:2,count=5 ==> 5,5 ==> (2-1)*5,5
-- page:3,count=5 ==> 10,5 ==> (3-1)*5,5
-- 推理：limit (page-1)*count,count
select file_records.id,
       users.id                   as uid,
       users.username,
       users.email,
       file_records.file_name,
       file_records.md5,
       inet_ntoa(file_records.ip) as ip,
       file_records.url
from file_records
         inner join users on file_records.user_id = users.id
limit 0,5;

-- limit后面跟表达式就会报错
select file_records.id,
       users.id                   as uid,
       users.username,
       users.email,
       file_records.file_name,
       file_records.md5,
       inet_ntoa(file_records.ip) as ip,
       file_records.url
from file_records
         inner join users on file_records.user_id = users.id
limit 5,5;
-- limit (2-1)*5,5; -- limit错误写法

-- limit要放在最后
select file_records.id,
       users.id                   as uid,
       users.username,
       users.email,
       file_records.file_name,
       file_records.md5,
       inet_ntoa(file_records.ip) as ip,
       file_records.url
from file_records
         inner join users on file_records.user_id = users.id
order by username desc, file_name desc
limit 10,5; -- 先order by排完序，然后再取第三页的5个数据

-- 查找一下从来没上传过文件的用户
-- right join：以右边表（users）为基准连接
select file_records.id            as fid,
       users.id                   as uid,
       users.username,
       users.email,
       file_records.file_name,
       file_records.md5,
       inet_ntoa(file_records.ip) as ip,
       file_records.url
from file_records
         right join users on file_records.user_id = users.id
where users.datastatus = 1
  and file_records.id is null
order by username desc, file_name desc;

-- 自连接案例：
-- 二级联动 p：province，c：city，a：area
-- 前端一般都会显示省级信息，用户选择后可以获得对应的二三级信息
select c.name, a.name
from citys as c
         inner join citys as a on a.pcode = c.code
where c.pcode = '320000'; -- pcode设置为索引

-- 通过省名称查询
select p.name, c.name, a.name
from citys as c
         inner join citys as p on c.pcode = p.code
         inner join citys as a on a.pcode = c.code
where p.name = '江苏省';
-- ------------------------------------------------------------------------

-- 简单提一下视图：
-- 创建视图
create view view_userinfo as
select id, username, password, email, tel, datastatus
from dotnetcrazy.users;

-- 查询视图
select id, username, password, email, tel, datastatus
from dotnetcrazy.view_userinfo;

-- 删除视图
drop view if exists view_userinfo;

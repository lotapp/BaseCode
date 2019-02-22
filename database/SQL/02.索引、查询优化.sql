-- 查看mysql数据文件 -- datadir	/data/mysql/
show variables like '%dataDir%';
-- -------------------------------------------------------------------------------
-- 1.基础相关
-- SQL执行顺序：
-- 1. `from <tb_name>`
-- 2. `on <join_condition>`
-- 3. `<join_type> join <right_table>`
-- 4. `where <where_condition>`
-- 5. `group by <group_by_list>`
-- 6. `having <having_condition>`
-- 7. `select [distinct] <select_list>`
-- 8. `order by <order_by_list>`
-- 9. `limit <limit_number>`
-- -------------------------------------------------------------------------------
-- 1. 查看索引：`show index from tb_name;`
--     - show index from worktemp.userinfo\G;
--     - show index from worktemp.userinfo;
-- 2. 创建索引：
--     - `create [unique] index index_name on tb_name(列名,...)`
--     - `alter table tb_name add [unique] index [index_name] on (列名,...)`
-- 3. 删除索引：
--     - `drop index index_name on tb_name`
--     - `alter table tb_name drop index index_name`

-- 删除索引
drop index ix_users_createtime_updatetime on dotnetcrazy.users;

-- 创建索引
create index ix_users_createtime_updatetime on dotnetcrazy.users (createtime, updatetime);

-- 删除唯一键
drop index uq_users_email on dotnetcrazy.users;

-- 创建唯一键
create unique index uq_users_email on dotnetcrazy.users (email);

-- 1. 唯一索引使用uq_表名_字段名来命名
-- 2. 非唯一索引使用ix_表名_字段名来命名
-- 3. 单张表索引数量建议控制在5个以内
--     - 互联网高并发业务，太多索引会影响写性能
--     - 异常复杂的查询需求，可以选择ES等更为适合的方式存储
--     - 生成执行计划时，如果索引太多，会降低性能，并可能导致MySQL选择不到最优索引
-- 4. 组合索引字段数不建议超过5个
--     - 如果5个字段还不能极大缩小row范围，八成是设计有问题
-- 5. 不建议在频繁更新的字段上建立索引
-- 6. 尽量不要join查询，如果要进行join查询，被join的字段必须类型相同，并建立索引
--     - join字段类型不一致容易导致全表扫描
-- 7. 理解组合索引最左前缀原则，避免重复建设索引
--     - 如果建立了(a,b,c)，相当于建立了(a), (a,b), (a,b,c)

-- -------------------------------------------------------------------------------
-- 2.执行计划
-- 主要是看这几个参数：
-- 1. id：当前查询语句中，每个select语句的编号
--     - 主要是针对子查询、union查询
-- 2. `select_type`：查询类型
--     - 简单查询：simple（一般的查询语句）
--     - 复杂查询：（详解见附录1）
--         - `subquery`：用于where中的子查询（简单子查询）
--         - `derived`：用于from中的子查询
--         - `union`：union语句的第一个之后的select语句
--         - `union result`：匿名临时表
-- 3. `type`：访问类型(MySQL查询表中行的方式)
--     1. all：全表扫描
--     2. index：根据索引的次序进行全表扫描（**覆盖索引效率更高**）
--     3. range：根据索引做指定范围扫描
--     4. ref：返回表中所有匹配某单个值的所有行
--     5. eq_ref：等同于ref，与某个值做比较且仅返回一行
--     6. const：根据具有唯一性索引查找时，且返回单个行（**性能最优**）
--         - eg：主键、唯一键
--     7. **PS：1~6 ==> 数字越大效率越高（性能递增）**，（详解见附录2）
-- 4. `possible_keys`：查询可能会用到的索引
-- 5. `key`：查询中使用了的索引
-- 6. `key_len`：索引使用的字节数（详解见附录3）
--     - 根据这个值，可以判断索引使用情况
--     - eg：使用组合索引时，判断所有索引字段是否都被查询到
-- 7. `ref`：显示key列索引用到了哪些列、常量值
--     - 在索引列上查找数据时，用到了哪些列或者常量
-- 8. `rows`：估算大概需要扫描多少行
-- 9. `Extra`：额外信息（性能递减）
--     1. **using index**：使用了覆盖索引
--     2. `using where`：在存储引擎检索后，再进行一次过滤
--     3. using temporary：对结果排序时会使用临时表
--     4. using filesort：对结果使用一个外部索引排序
--         - 没有有索引顺序，使用了自己的排序算法
--         - 可能出现的情况：（**出现这个情况基本上都是需要优化的**）
--             - where后面的索引列和`order by|group by`后面的索引列不一致(只能用到一个索引)
--             - eg：`explain select * from users where id<10 order by email;`（只用到了id）
create table if not exists `students`
(
    id          int unsigned auto_increment primary key,
    name        varchar(25)      not null default '' comment '姓名',
    age         tinyint unsigned not null default 0 comment '年龄',
    work        varchar(20)      not null default '普通学生' comment '职位',
    create_time datetime         not null comment '入学时间',
    datastatus  tinyint          not null default 0 comment '数据状态'
) charset utf8 comment '学生表';

-- select current_timestamp(), now(), unix_timestamp();
insert into students(name, age, work, create_time, datastatus)
values ('111', 22, 'test', now(), 99),
       ('小张', 23, '英语课代表', now(), 1),
       ('小李', 25, '数学课代表', now(), 1),
       ('小明', 21, '普通学生', now(), 1),
       ('小潘', 27, '物理课代表', now(), 1),
       ('张小华', 22, '生物课代表', now(), 1),
       ('张小周', 22, '体育课代表', now(), 1),
       ('小罗', 22, '美术课代表', now(), 1);

-- 创建一个组合索引
create index ix_students_name_age_work on students (name, age, work);

-- -------------------------------------------------------------------------------
-- `select_type`：查询类型
-- `subquery`：用于where中的子查询（简单子查询）
explain
    select name, age
    from students
    where age > (select avg(age) from students);

-- `union`：union语句的第一个之后的select语句
-- `union result`：匿名临时表
explain
    select name, age, work
    from students
    where name = '小张'
    union
    select name, age, work
    from students
    where name = '小明';

-- `derived`：用于from中的子查询
explain
    select *
    from (select name, age, work
          from students
          where name = '小张'
          union
          select name, age, work
          from students
          where name = '小明') as tmp;

-- -------------------------------------------------------------------------------
-- `type`：访问类型(MySQL查询表中行的方式)**
-- all：全表扫描（效率极低）
explain
    select *
    from students
    where name like '%小%';

-- index：根据索引的次序进行全表扫描（效率低）
explain
    select name, age, work
    from students
    where name like '%小%'; -- 其实就是上面全表扫描的改进版

-- range：根据索引做指定范围扫描
explain
    select name, age, work
    from students
    where id > 5;

-- ref：返回表中所有匹配某单个值的所有行
explain
    select name, age, work
    from students
    where name = '小明';

-- eq_ref：等同于ref，与某个值做比较且仅返回一行
explain
    select *
    from userinfo
             inner join (select id from userinfo limit 10000000,10) as tmp
                        on userinfo.id = tmp.id; -- 1s

-- const：根据具有唯一性索引查找时，且返回单个行（**性能最优**）
explain
    select name, age, work
    from students
    where id = 3; -- 一般都是主键或者唯一键

-- ---------------------------------------------------------------------------------
-- 3.key-len：
-- 1. 字符编码：(PS：不同字符编码占用的存储空间不同)
--     - `latin1`|`ISO8859`占1个字节，`gbk`占2个字节，**`utf8`占3个字节**
-- 2. 是否为空：
--     - not null 不需要额外的字节
--     - null 需要1字节用来标记
--     - PS：索引最好不要为null，这样需要额外的存储空间而且统计也变得更复杂
-- 3. 字符类型（char、varchar）的索引长度计算：
--     - 变长字段（varchar）需要额外的2个字节
--         - 1字节用来保存需要的字符数
--         - 1字节用来记录长度（PS：如果列定义的长度超过255则需要2个字节【总共3字节】）
--     - 定长字段（char）不需要额外的字节
-- 4. 数值类型、日期类型的索引长度计算：
--     - 一般都是其本身长度，如果可空则+1
--         - 标记是否为空需要占1个字节
--     - PS：datetime在5.6中字段长度是5，在5.5中字段长度是8
-- 5. 复合索引有最左前缀的特性。如果复合索引能全部用上，则为复合索引字段的索引长度之和
--     - PS：可以用来判断复合索引是否全部使用到
-- 6. 举个栗子：
--     - eg：`char(20) index 可空`
--         - `key-len=20*3(utf8)+1(可空)=61`
--     - eg：`varchar(20) index 可空`
--         - `key-len=20*3(utf8)+2(可变长度)+1(是否可空的标记)=63`

-- ---------------------------------------------------------------------------------
-- 3.优化原则
-- 1.尽可能多的使用索引列，尽可能使用覆盖索引
-- 如果我查询的时候，索引的三列都用到了，那么速度无疑是最快的
-- Extra：using where
explain
    select id, name, age, work, create_time
    from students
    where name = '小张'
      and age = 23
      and work = '英语课代表';

-- PS：★尽量使用覆盖索引★（近乎万能）
-- 覆盖索引：仅仅查找索引就能找到所需要的数据
-- Extra：using where;using index
explain
    select name, age, work
    from students
    where name = '小张'
      and age = 23
      and work = '英语课代表';
-- PS：一般把经常select出的列设置一个组合索引，一般不超过5个

-- ---------------------------------------------------------------------------------
-- 2.最左前缀原则（组合索引）
-- 查询的时候从最左边的列开始，并且不跳过中间的列，一直到最后
-- 类比火车，火车头自己可以开，车身要是没有了车头就开不了
explain
    select id, name, age, work, create_time
    from students
    where name = '小张'
      and age = 23
      and work = '英语课代表';

-- 跳过了中间的age，这时候只用到了name列的索引（work列没用到）
explain
    select id, name, age, work, create_time
    from students
    where name = '小张'
      and work = '英语课代表';

-- PS：如果跳过了第一列，这时候索引一个也用不到，直接全表扫描了
explain
    select id, name, age, work, create_time
    from students
    where age = 23
      and work = '英语课代表';

-- PS：列不一定需要按照指定顺序来写
explain
    select id, name, age, work, create_time
    from students
    where age = 23
      and work = '英语课代表'
      and name = '小张';

-- ---------------------------------------------------------------------------------
-- 3.范围条件放最后面（范围条件后面的列索引会失效）
-- name、age索引生效时，key_len=78
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小张'
      and age = 23;

-- name、age、work索引生效时，key_len=140
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小张'
      and age = 23
      and work = '英语课代表';

-- 现在key_len=78 ==> work列索引就失效了（PS：age索引列未失效，只是age之后的列失效了）
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小张'
      and age > 22
      and work = '英语课代表';

-- 加快查询速度可以使用覆盖索引
explain
    select name, age, work
    from students
    where name = '小张'
      and age > 22
      and work = '英语课代表';

-- PS：多个主键列也一样
explain
    select id, name, age, work
    from students
    where name = '小张'
      and age > 22
      and work = '英语课代表';

-- PS：调换顺序是没法解决范围后面索引失效的（本来对顺序就不在意）
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小张'
      and work = '英语课代表'
      and age > 22;

-- ---------------------------------------------------------------------------------
-- 4.不在索引列上做其他操作
-- 4.1.`!=`、`is not null`、`is null`、`not in`、`in`、`like`慎用
-- 1.不等于案例
-- 索引失效（key,key_len ==> null）
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name != '小明'; -- <> 等同于 !=

-- 项目里面很多使用都要使用，那怎么办呢？==> 使用覆盖索引
-- key=ix_students_name_age_work，key_len=140
explain
    select name, age, work
    from students
    where name != '小明'; -- <> 等同于 !=

-- 2.is null、is not null案例
-- 索引失效（key,key_len ==> null）
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name is not null;

-- 解决：覆盖索引 key=ix_students_name_age_work，key_len=140
explain
    select name, age, work
    from students
    where name is not null;

-- 3.not in、in案例
-- 索引失效（key,key_len ==> null）
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name in ('小明', '小潘', '小李');

explain
    select id, name, age, work, create_time, datastatus
    from students
    where name not in ('小明', '小潘', '小李');

-- 解决：覆盖索引 key=ix_students_name_age_work，key_len=140
explain
    select name, age, work
    from students
    where name in ('小明', '小潘', '小李');

explain
    select name, age, work
    from students
    where name not in ('小明', '小潘', '小李');

-- 4.like案例：尽量使用`xxx%`的方式来全文搜索，能和覆盖索引联合使用更好
-- 索引不失效 key=ix_students_name_age_work，key_len=77（尽量这么用like）
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name like '张%';

-- 索引失效
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name like '%张';

-- 索引失效
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name like '%张%';

-- 解决：覆盖索引 key=ix_students_name_age_work，key_len=140（尽量避免）
explain
    select name, age, work
    from students
    where name like '%张%';

-- ---------------------------------------------------------------
-- 4.2.计算、函数、类型转换（自动 or 手动）【尽量避免】
-- 这时候索引直接失效了，并全表扫描了
-- 解决虽然可以使用覆盖索引，但是尽量避免下面的情况：
-- 1.计算
explain
    select id, name, age, work, create_time, datastatus
    from students
    where age = (10 + 13);

-- 2.隐式类型转换（111==>'111'）
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name = 111;
-- PS：字符类型不加引号索引就直接失效了
-- 虽然覆盖索引可以解决，但是不要这样做（严格意义上讲，这个算个错误）

-- 3.函数
explain
    select id, name, age, work, create_time, datastatus
    from students
    where right(name, 1) = '明';

-- ---------------------------------------------------------------------------------
-- 5.几种写法上的优化

-- 5.1.or改成union
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小明'
       or name = '小张'
       or name = '小潘';

-- PS：等同上面or的语句
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name in ('小明', '小张', '小潘');

-- 高效
explain
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小明'
    union all
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小张'
    union all
    select id, name, age, work, create_time, datastatus
    from students
    where name = '小潘';

-- union总是产生临时表，优化起来比较棘手
-- > 一般来说union子句尽量查询最少的行，union子句在内存中合并结果集需要去重（浪费资源），所以使用union的时候尽量加上all（在程序级别去重即可）

-- ---------------------------------------------------------------------------------

-- 5.2.count优化
-- 一般都是count(主键|索引)，但现在count(*)基本上都有优化了，根据公司要求使用即可
--     - PS：记得当时踩了次坑，等复现的时候补上案例（记得好像跟null相关）
explain
    select count(id) -- 常用，一般都是count(主键)
    from userinfo;

explain
    select count(*)
    from userinfo;

-- 你`count(非索引)`就有所谓了
explain
    select count(password)
    from userinfo;

-- 我想说的优化是下面这个count优化案例：
-- 需要统计id>10000的数据总量（实际中可能会根据时间来统计）
explain
    select count(*) as count
    from userinfo
    where id > 10000; -- 2s

-- 分解成用总数-小数据统计 ==> 1s
explain
    select (select count(*) from userinfo) - (select count(*) from userinfo where id <= 10000) as count;

-- ---------------------------------------------------------------------------------
-- 5.3.group by和order by的列尽量相同，这样可以避免filesort
explain
    select *
    from students
    group by name
    order by work;

explain
    select *
    from students
    group by name
    order by name;

-- 加where条件也一样
explain
    select *
    from students
    where name like '小%'
    group by age
    order by work;

-- PS：一般group by和order by的列都和where索引列相同（不一致也只会使用一个索引）
explain
    select *
    from students
    where name like '小%'
      and age > 20
    group by name
    order by name;

-- where后面的索引列和`order by|group by`后面的索引列不一致
-- id和email都是索引，但只用了一个索引
explain
    select *
    from users
    where id < 10
    order by email;

-- ---------------------------------------------------------------------------------
-- 5.4.用连接查询来代替子查询
-- 用exists代替in？MySQL查询优化器针对in做了优化（改成了exists，当users表越大查询速度越慢）
explain
    select *
    from students
    where name in (select username from users where id < 7);

-- ==> 等同于：
explain
    select *
    from students
    where exists(select username from users where username = students.name and users.id < 7);

-- 真正改进==>用连接查询代替子查询
explain
    select students.*
    from students
             inner join users on users.username = students.name and users.id < 7;

-- 等效写法：这个tmp是临时表，是没有索引的，如果需要排序可以在（）里面先排完序
explain
    select students.*
    from students
             inner join (select username from users where id < 7) as tmp on students.name = tmp.username;

-- ---------------------------------------------------------------------------------
-- 查看profiling系统变量
show variables like '%profil%';
-- profiling：开启SQL语句剖析功能（开启之后应为ON）

-- 来查看是否已经启用profile
select @@profiling;

-- 启动profile（当前会话启动）
set profiling = 1; -- 0：未启动，1：启动

show profiles; -- 显示查询的列表

show profile for query 5; -- 查看指定编号查询的详细信息

-- 5.5.★limit优化★
-- limit offset,N：mysql并不是跳过offset行，然后取N行，而是取offset+N行，然后放弃前offset行，返回N行（offset越大效率越低）
--     - PS：你去翻贴的时候，页码越大一般越慢
select *
from userinfo
limit 10,10;
select *
from userinfo
limit 1000,10;
select *
from userinfo
limit 100000,10;
select *
from userinfo
limit 1000000,10;
select *
from userinfo
limit 10000000,10;

show profiles; -- 显示查询列表

show profile for query 5; -- 查看指定编号查询的详细信息

-- 解决：
-- 1. 业务上解决，eg：不许翻页超过100（一般都是通过搜索来查找数据）
--     - PS：百度搜索页面也只是最多翻到76
-- 2. 使用where而不使用offset
--     - **id完整的情况**：eg：`limit 5,3 ==> where id > 5 limit 3;`
--     - PS：项目里面一般都是逻辑删除，id基本上算是比较完整的
-- 3. `覆盖索引+延迟关联`：通过使用覆盖索引查询返回需要的主键,再根据主键关联原表获得需要的数据
--     - 使用场景：比如`主键为uuid`或`id不连续`（eg：部分数据物理删除了等等）

-- 全表扫描
explain
    select *
    from userinfo
    limit 10000000,10; -- 3s

-- 先range过滤了一部分
explain
    select *
    from userinfo
    where id > 10000000
    limit 10; -- 20ms

-- 内部查询使用了索引覆盖
explain
    select *
    from userinfo
             inner join (select id from userinfo limit 10000000,10) as tmp
                        on userinfo.id = tmp.id; -- 2s

-- ---------------------------------------------------------------------------------
-- 索引误区
-- **很多人喜欢把where条件的常用列上都加上索引**，但是遗憾的事情是：**`独立的索引只能同时用上一个`**
-- - **PS：在实际应用中往往选择`组合索引`**
-- 别不信，来验证一下就知道了：

-- id和email都是索引，但是只能使用一个索引（独立的索引只能同时用上一个）
-- id的key-len=4（int4个字节）
-- email的key-len=152（50*3(utf8下每个字符占3位)+2(varchar需要额外两个字节存放)==>152）
-- 1.唯一索引和主键：优先使用主键
explain
    select *
    from users
    where id = 4
      and email = 'xiaoming@qq.com';

-- 2.组合索引和主键：优先使用主键
explain
    select *
    from users
    where id = 4
      and createtime = '2019-02-16 17:10:29';

-- 3.唯一索引和组合索引：优先使用唯一索引
explain
    select *
    from users
    where createtime = '2019-02-16 17:10:29'
      and email = 'xiaoming@qq.com';

-- 4.组合索引和一般索引：优先使用组合索引
-- create index ix_users_datastatus on users(datastatus);
-- create index ix_users_username_password on users(username,password);
explain
    select *
    from users
    where datastatus = 1
      and username = '小明';
-- 删除临时添加的索引
-- drop index ix_users_datastatus on users;
-- drop index ix_users_username_password on users;

-- ---------------------------------------------------------------------------------
-- 冗余索引:
-- 举个标签表的例子：
create table tags
(
    id         int unsigned auto_increment primary key,
    aid        int unsigned not null,
    tag        varchar(25)  not null,
    datastatus tinyint      not null default 0
);
insert into tags(aid,tag,datastatus) values (1,'Linux',1),(1,'MySQL',1),(1,'SQL',1),(2,'Linux',1),(2,'Python',1);

select id, aid, tag, datastatus from tags;

-- 实际应用中可能会根据tag查找文章列表，也可能通过文章id查找对应的tag列表
-- > 项目里面一般是这么建立索引（冗余索引）：index(文章id,tag),index(tag,文章id)，这样在上面两种情况下可以直接用到覆盖索引

create index ix_tags_aid_tag on tags(aid,tag);
create index ix_tags_tag_aid on tags(tag,aid);

select tag from tags where aid=1;
select aid from tags where tag='Linux';

-- ---------------------------------------------------------------------------------

-- PS：其实数据库表使用时间长了会出现碎片，可以定期修复一下（不影响数据）
optimize table users;
-- > 修复表的数据以及索引碎片会把数据文件整理一下，这个过程相对耗费时间（数据量大的情况下）一般根据情况选择按周|月|年修复一下

-- PS：可以配合`crontab`（定时任务）使用：
-- - 使用命令：`crontab -e`：`***** 命令 [ > /dev/null 2>&1 ]`
--     - **`5个*的含义`**：`分`、`时`、`日`、`月`、`周`
--     - 从定向知识：
--         - `>> /xx/日志文件`：输出重定向到日记文件（不包含错误信息）
--         - `>> /xx/日志文件 2>&1`：输出信息包括错误信息
--         - `> /dev/null 2>&1`：出错信息重定向到垃圾桶（黑洞）
--     - 举几个栗子：
--         - `21*** xxx` ==> 每天 1:02 执行 xxx命令
--         - `5921*** xxx` ==> 每天 21::59 执行 xxx命令
--         - `*/*1*** xxx` ==> 每1小时 执行一次xxx命令
--             - 定时任务以`*/`开头
-- ----------------------------------------------------------------
-- insert语句优化
-- 1. 提交前关闭自动提交
-- 2. 尽量使用批量insert语句
-- 3. 尽可能使用MyISAM存储引擎（不支持事物，速度当然快）

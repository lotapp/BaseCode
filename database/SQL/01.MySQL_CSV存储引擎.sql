-- 文章参考：https://www.cnblogs.com/dotnetcrazy/p/10481483.html
-- # 协同办公衍生出的需求

-- ## 1.业务需求

-- ### 1.1.流程

-- 先说业务流程：

-- 现在办公基本上都是诸如`TIM`之类的在线office来协同办公，然后所有的在线文档会有一份本地文件用来存储和数据分析

-- ### 1.2.需求

-- 需求是这样的：

-- 希望企业系统和文职人员以及分析部能够共同管理这些Excel表格，但不想耗费资源去开发OA之类的系统，希望开发部想办法

-- 先简单拆分一下：
-- - 文职人员在线编辑
-- - 分析师需要CSV文件来分析数据
-- - 开发人员需要存储到DB中供内网系统使用

-- ### 1.3.思路

-- 再说下思路：

-- 在线文档本地离线存储比较简单，看下更新时间然后覆盖存储即可（数据的产生主要是文职人员）

-- 以前看到Excel表格一般都是使用`NPOI`定时读写文件系统里面的共享Excel文件，然后存到DB中，最后生成CSV文件交给分析部就行了
-- - PS：`麻烦的是增量写入DB`

-- 前段时间给大家讲MySQL的时候（草稿写到存储引擎这块），突然想到了**`CSV存储引擎`**，这不完美符合业务需求吗？

-- 于是就有了这篇文章：

-- ## 2.基础知识

-- ### 2.1.概念

-- **CSV存储引擎**：以文本方式存储在文件中（`innodb`是二进制文件）
--    - frm（表结构）、CSV（表内容）、CSM（表状态、数据量等）
--    - PS：一般都是作为中间表，**不适合大表**

-- ### 2.2.CSV特点

-- 1. 以CSV格式进行数据存储（逗号分隔）
-- 2. 所有列都不能为NULL
-- 3. 不支持索引（不适合大表）
-- 3. 可以对数据文件直接编辑（保存文本文件内容）

-- ## 3.简单解决

-- 存储在线文档的时候保存为CSV文件，建表的时候使用CSV存储引擎，然后定时刷新下表（`flush tables`）就可以数据同步了（或者使用前，让程序自动执行下刷新表操作）

-- 摸拟下场景：

-- 创建数据库
create database if not exists onlinedoc charset utf8;

-- PS：添加权限：`grant all privileges on 数据库.* to 用户名@"%" identified by "密码";`并刷新`flush privileges;`

use onlinedoc;

-- 创建摸拟表
create table if not exists day_total
(
    id           int unsigned not null default 0,
    title        varchar(50)  not null default '',
    shopee_count int unsigned not null default 0,
    whish_count  int unsigned not null default 0,
    ebay_count   int unsigned not null default 0,
    amazon_count int unsigned not null default 0,
    total_count  int unsigned not null default 0,
    actual_count int unsigned not null default 0,
    `date`       date         not null, -- 只需要年月日
    remark       varchar(500) not null default ''
)
    engine = 'csv', -- 引擎
    character set utf8, -- 字符集
    collate utf8_general_ci; -- 排序规则

-- 插入摸拟数据
insert into day_total(id, title, shopee_count, whish_count, ebay_count, amazon_count, total_count, actual_count, `date`,
                      remark)
values (1, '2019-02-03日销售统计', 14310, 7889, 581, 9812, 32592, 32579, '2019-02-03', '有13件未走单'),
       (2, '2019-02-04日销售统计', 1200, 6930, 1304, 612, 10046, 10059, '2019-02-04', '补发昨天13件'),
       (3, '测试', 1, 1, 1, 1, 4, 4, '2018-01-01', '');

-- 一些测试
-- #### 1.基本操作测试
-- 除了索引之类的不支持，其他的基本上都是支持的（包括事物）
select title, total_count, actual_count, `date`, remark
from day_total;

update day_total
set remark='有13件没有发货'
where date = '2019-02-03';

delete from day_total where id=3;

create view view_day_total_mini as
select title, total_count, actual_count, `date`, remark
from day_total;

select * from view_day_total_mini;

begin;
-- drop table day_total_del;
drop view view_day_total_mini;
commit;

-- #### 2.可行性测试

-- 1.分配刷新表的权限
-- ![2.1.权限.png](https://img2018.cnblogs.com/blog/1127869/201903/1127869-20190306125217638-727454098.png)

-- PS：**赋予用户刷新表的权限**：`grant reload on *.* to '用户名'@'%';`并刷新`flush privileges;`

-- 2.先看看csv文件
-- ![2.2.看看csv文件.png](https://img2018.cnblogs.com/blog/1127869/201903/1127869-20190306125246037-1187149156.png)

-- 3.手动添加1条数据（双引号包裹字符串）
-- - `3,"2019-02-05日销售统计",1100,2130,304,1410,4944,4944,"2019-02-04",""`

-- ![2.3.手动添加1条.png](https://img2018.cnblogs.com/blog/1127869/201903/1127869-20190306125318086-1104398046.png)

-- 4.测试一下
-- ![2.4.测试.png](https://img2018.cnblogs.com/blog/1127869/201903/1127869-20190306125347067-1684888338.png)

-- **PS：CSV存储引擎一般都是当中间商**

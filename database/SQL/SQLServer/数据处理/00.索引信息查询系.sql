SELECT  索引名称 = a.name ,
        表名 = c.name ,
        索引字段名 = d.name ,
        索引字段位置 = d.colid
FROM    sysindexes a
        JOIN sysindexkeys b ON a.id = b.id
                               AND a.indid = b.indid
        JOIN sysobjects c ON b.id = c.id
        JOIN syscolumns d ON b.id = d.id
                             AND b.colid = d.colid
WHERE   a.indid NOT IN ( 0, 255 )  
and   c.xtype='U' --查所有用户表  
--and c.name = 'info' --查指定表  
ORDER BY c.name ,
        a.name ,
        d.name
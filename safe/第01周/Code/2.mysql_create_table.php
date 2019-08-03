<?php
    // 建立连接
    $conn=new mysqli("192.168.0.9", "bryan", "WWW.baidu.com1", "safe_db");
    if ($conn->connect_errno) {
        die("连接失败：" . $conn->connect_error);
    }
    // SQL
    $sql="create table if not exists safe_db.users(
    id         int unsigned auto_increment,
    username   varchar(20) not null,
    password   char(40)    not null,
    email      varchar(50) not null,
    ucode      char(36)    not null,
    createtime datetime    not null,
    updatetime datetime    not null,
    datastatus tinyint     not null default 0,
    primary key (id),
    unique uq_users_email (email),
    index ix_users_createtime_updatetime (createtime, updatetime)
    )";
    // 执行SQL
    if ($conn->query($sql)==true) {
        echo "User表创建成功!";
    } else {
        echo "User表创建失败!" . $conn->error;
    }
    // 关闭连接
    $conn->close()
?>
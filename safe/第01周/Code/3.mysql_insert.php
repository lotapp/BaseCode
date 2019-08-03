<?php
    // 建立连接
    $conn=new mysqli("192.168.0.9", "bryan", "WWW.baidu.com1", "safe_db");
    if ($conn->connect_errno) {
        die("连接失败：" . $conn->connect_error);
    }

    // 插入语句
    $sql="insert into safe_db.users
    values(0, 'test1', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'test1@qq.com', uuid(), now(), now(), 1),
    (0, '小张1', '7c4a8d09ca3762af61e59520943dc26494f8941b', 'zhang1@qq.com', uuid(), now(), now(), 1);";

    // 防止SQL中文乱码
    $conn->query("set names utf8;");

    // 执行SQL
    if ($conn->query($sql)==true) {
        echo "插入成功!";
    } else {
        echo "Error：" . $sql . "<br/>" . $conn->error;
    }
    // 关闭连接
    $conn->close();

?>

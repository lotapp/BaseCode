<?php
    $conn=new mysqli("192.168.0.9", "bryan", "WWW.baidu.com1", "safe_db");
    if ($conn->connect_error) {
        die("连接失败：" . $conn->connect_error);
    }
    # 删除表数据 // PS：只保留表结构：truncate table users
    $sql="truncate table users"; // 删除表：drop table users
    if ($conn->query($sql)==true) {
        echo "删除成功!";
    } else {
        echo "删除失败：" . $sql . "<br/>" . $conn->error;
    }
    $conn->close();
?>

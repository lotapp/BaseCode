<?php
    // 建立连接
    $conn = new mysqli("192.168.0.9", "bryan", "WWW.baidu.com1", "safe_db");
    if ($conn->connect_errno) {
        die("连接失败：" . $conn->connect_errno);
    } else {
        echo "连接成功!";
    }
    // 关闭连接
    $conn->close();
?>
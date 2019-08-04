<?php
    $conn=new mysqli("192.168.0.9", "bryan", "WWW.baidu.com1", "safe_db");
    if ($conn->connect_error) {
        die("连接失败：" . $conn->connect_error);
    }

    // 防止SQL中文乱码
    $conn->query("set names utf8;");
    
    // 防止SQLi的写法（预处理语句）
    $statement  = $conn->prepare("update users set username=? , email=? , updatetime=? where id=?");
    // 指定参数类型（i：int，d：double，s：string，b：blob）
    $name="小张";$email="zhang@qq.com";$updatetime=date('Y-m-d H:i:s');$id=2;
    $statement ->bind_param("sssi", $name, $email, $updatetime, $id);
    // 执行sql
    $statement ->execute();
    
    echo "更新成功";

    $statement->close();
    $conn->close();
?>
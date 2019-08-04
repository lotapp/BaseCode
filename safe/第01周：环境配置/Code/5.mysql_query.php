<?php
    $conn=new mysqli("192.168.0.9", "bryan", "WWW.baidu.com1", "safe_db");
    if ($conn->connect_error) {
        die("连接失败：" . $conn->connect_error);
    }

    // 防止中文乱码
    $conn->query("set names utf8;");
    
    // 防止SQLi的写法（预处理语句）
    $sth = $conn->prepare("select id,username,email,updatetime from safe_db.users where datastatus=? and id=?;");
    // 指定参数类型（i：int，d：double，s：string，b：blob）
    $id=2;$datastatus=1;
    $sth->bind_param("ii", $datastatus, $id);
    // 执行SQL
    $sth->execute();

    // 接受返回结果
    $result = $sth->get_result();
    while ($row = $result->fetch_assoc()) {
        echo $row["id"] . "," . $row["username"] . "," . $row["email"]. "," . $row["updatetime"];
    }
    // 释放结果集
    $sth->free_result();
    $sth->close();
    $conn->close();
?>
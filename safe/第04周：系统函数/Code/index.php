<?php
    // 自己构造的一个sqli页面
    $pms=$_GET["id"];
    if(empty($pms)){
        $pms=1;
    }
    echo "id=" . $pms . "<br/>";

    $conn=new mysqli("localhost", "用户名", "密码", "数据库");
    if ($conn->connect_error) {
        die("连接失败：" . $conn->connect_error);
    }

    // 防止中文乱码
    $conn->query("set names utf8;");
    $sql = "select username,password from workdb.users where id=" . $pms;
    echo "SQL：" . $sql . "<br/>";

    $result = $conn->query($sql);
    if($result->num_rows > 0){
        while($row = $result->fetch_assoc()){
            echo "username：" . $row["username"] . "，name：" . $row["password"] . "<br/>";
        }
    } else {
        echo "no results";
    }
    $conn->close();
?>
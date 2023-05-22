<?php
header("Content-type: text/html; charset=utf8");
 
$host = '156.247.29.237'; //数据库ip
 
$user = 'a202303290840018'; //用户名
 
$password = 'VUzwprew76'; //密码
 
$dbName = 'a202303290840018'; //要连接的数据库名
 
$con = new mysqli($host, $user, $password, $dbName); //数据库连接
 
if ($con->connect_error) {
    echo "系统异常，连接数据库失败:", $con->connect_error;
} 
?>
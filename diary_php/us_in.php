<?php
include 'connect.php';//调用connect.php文件
$TD=$_GET['today'];
$TM=$_GET['tomorrow'];
if ($con->connect_error) {
	die("连接失败：".$con->connect_error);
}
else 
{

 	$sql = "INSERT INTO diary(today,tomorrow) VALUES ('".$TD."','".$TM."');";
 	$res=$con->query($sql);
 	if($res){
    $arr['status'] = 1;
    $arr['info'] = 'success';
	}else{
    $arr['status'] = 0;
    $arr['info'] = 'error';
	}
	echo json_encode($arr);
	die;
}
 
?>
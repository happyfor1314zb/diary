<?php
include 'connect.php'; 
$sql1="SELECT `today` FROM `diary_today` WHERE DATEDIFF(`day`,NOW())=0 order by `id` desc";
$sql2="SELECT `tomorrow` FROM `diary_tomorrow` WHERE DATEDIFF(`day`,NOW())=0 order by `id` desc";
$reslut1=$con->query($sql1);
$reslut2=$con->query($sql2);
// $reslut=[$reslut1,$reslut2];
if ($reslut2) 
{
    $attr = $reslut->fetch_all();
    //$attr = $reslut->fetch_row();
    //var_dump($attr);
    echo json_encode($attr);

    } else {
        echo '查询出错！';
    }
?>
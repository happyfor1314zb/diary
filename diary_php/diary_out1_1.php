<?php
include 'connect.php'; 
$sql="SELECT `tomorrow` FROM `diary_tomorrow` WHERE DATEDIFF(`day`,NOW())=-1 order by `id` desc";
$reslut=$con->query($sql);

if ($reslut) 
{
    $attr = $reslut->fetch_all();
    //$attr = $reslut->fetch_row();
    //var_dump($attr);
    echo json_encode($attr);

    } else {
        echo '查询出错！';
    }
?>
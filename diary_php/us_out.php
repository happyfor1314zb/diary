<?php
include 'connect.php'; 
$sql="SELECT * FROM `diary` order by `id` desc";
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
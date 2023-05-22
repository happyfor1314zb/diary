# 日报

#### 介绍
配合微信小程序，云服务器的mysql，及天气api的json数据，利用指定的docx模板，自动生成日报，并在钉钉汇报群内及时发布

#### 软件架构
软件架构说明


#### 安装教程

1.  在原“日报”项目文件中的‘main.pyw“代码前增两行代码，设置一个环境变量
```python
import os
# 设置一个环境变量
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python310\tcl\tcl8.6'
```
2.  在开始搜索框中输入“任务计划程序“点击进入。
<br>![](readme_img\readme1.png)
3.  依次点开Microsoft文件夹，再点右边的创建任务。
<br>![](readme_img\readme2.png)
4. 在任务的名称中注明‘张斌日报‘方便日后管理。
<br>![](readme_img\readme3.png)
5. 按下面截图设置，每天晚上19点执行一次。
<br>![](readme_img\readme4.png)
6.  第一个操作，保持默认为‘启动程序‘。剩下的三行依次填上，Python W执行程序文件的路径， PYW文件路径，文件起始的文件夹位置具体如下。

"C:\Program Files\Python310\pythonw.exe"

E:\pyGit\05日报\main.pyw

E:\pyGit\05日报 

**重要说明：若用main.py文件执行，就会自动弹出一个执行窗，可以监控程序执行状态。要更改为：**

"C:\Program Files\Python310\python.exe"

E:\pyGit\05日报\main.py

E:\pyGit\05日报
<br>![](readme_img\readme5.png)
7.   全部设置好后，点右侧的运行按钮测试运行结果。
<br>![](readme_img\readme6.png)
8. 为了测试不打扰，将发送程序注解了。经测试，能够正常生成当日的日报，证明设置成功。
<br>![](readme_img\readme7.png)

#### 使用说明

1.  部署一个 HTTPS mysql服务器,建立diary_today和diary_tomorrow两张数据表，结构如下图，根据当天的日期，取对应日期存入的数据
<br>![](readme_img\readme11.png)
<br>
````mysql 
CREATE TABLE `a202303290840018`.`diary_today`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `day` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `today` VARCHAR(300) NOT NULL,
    PRIMARY KEY(`id`)
) ENGINE = MyISAM;
````

<br>![](readme_img\readme12.png)
````mysql 
CREATE TABLE `a202303290840018`.`diary_tomorrow`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `day` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `tomorrow` VARCHAR(200) NOT NULL,
    PRIMARY KEY(`id`)
) ENGINE = MyISAM;
````

2.  装操作数据库的PHP代码，上传到服务器目录
<br>![](readme_img\readme21.png)<br>
下方代码为数据写入功能
````php
<?php
include 'connect.php';//调用connect.php文件
$user=$_GET['na'];
$content=$_GET['txt'];
if ($con->connect_error) {
	die("连接失败：".$con->connect_error);
}
else 
{

 	$sql = "INSERT INTO us(name,content) VALUES ('".$user."','".$content."');";
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
````
下方代码为数据读取功能
```php
<?php
include 'connect.php'; 
$sql="SELECT `today` FROM `diary_today` WHERE DATEDIFF(`day`,NOW())=0 order by `id` desc";
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
```
3.  创建一个微信公众号账号 建一个界面用于 输入和展示数据内容.
<br>![](readme_img\readme31.png)

#### 参与贡献

1.  new bing
2. csdn 技术社区



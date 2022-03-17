### MYSQL的安装和启动

- 先在官网下载dmg文件，记住安装到最后时的密码；
- 在系统偏好设置启动mysql
- 打开终端，为Path路径附加MySQL的bin目录: PATH="$PATH":/usr/local/mysql/bin
- 然后通过以下命令登陆MySQL（密码就是前面自动生成的临时密码）mysql -u root -p
- 修改密码，新密码为123456 set PASSWORD =PASSWORD('123456'); 再次执行show databases;就正常了。

[参考网址](http://www.myexception.cn/mysql/2043991.html)

### [删除在mac上的mysql](http://blog.csdn.net/maxsky/article/details/40347505)

```
sudo rm -rf /usr/local/mysql  
sudo rm -rf /usr/local/mysql*  
sudo rm -rf /Library/StartupItems/MySQLCOM  
sudo rm -rf /Library/PreferencePanes/My*  
sudo nano /etc/hostconfig     (复制前面部分回车，然后删掉这一行: MYSQLCOM=-YES-，control+O回车保存，control+X退出编辑界面)  
sudo rm -rf ~/Library/PreferencePanes/My*  
sudo rm -rf /Library/Receipts/mysql*  
sudo rm -rf /Library/Receipts/MySQL*  
sudo rm -rf /var/db/receipts/com.mysql.*
```

[MYSQL MAC客户端工具](https://sequelpro.com/download#auto-start)

修改数据库用户名和密码 <http://blog.csdn.net/individualing/article/details/7887025>

### 导入数据

- 输入：mysql>use 目标数据库名,如图黄色区域。
- 如我输入的命令行:mysql>use ygeshop;
- <http://jingyan.baidu.com/article/4e5b3e19505e9091901e24ba.html>
- 导入文件：mysql>source 导入的文件名;
- 如我输入的命令行：mysql>source ygeshop.sql;

### 表关联（内关联）

- create table `test_test2` as select `test`.`id`, `test`.`name`,`test`.`sex`, `test2`.`add` from `test` inner join `test2` on `test`.`name` = `test2`.`name`;
- select * from `click_16_08_27` inner join `16_08_27` on `click_16_08_27`.`push_time` = `16_08_27`.`request_time` and `click_16_08_27`.`push_time_us` = `16_08_27`.`request_time_us` ;


### 移除包的时候还把相关的文件删除，然后重新装的时候才不会出问题
python-mysql
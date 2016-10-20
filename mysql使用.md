MYSQL的安装和启动

- 先在官网下载dmg文件，记住安装到最后时的密码；
- 在系统偏好设置启动mysql
- 打开终端，为Path路径附加MySQL的bin目录: PATH="$PATH":/usr/local/mysql/bin
- 然后通过以下命令登陆MySQL（密码就是前面自动生成的临时密码）mysql -u root -p
- 修改密码，新密码为123456
set PASSWORD =PASSWORD('123456');
再次执行show databases;就正常了。

[参考网址](http://www.myexception.cn/mysql/2043991.html)

[删除在mac上的mysql](http://blog.csdn.net/maxsky/article/details/40347505)

	sudo rm -rf /usr/local/mysql  
	sudo rm -rf /usr/local/mysql*  
	sudo rm -rf /Library/StartupItems/MySQLCOM  
	sudo rm -rf /Library/PreferencePanes/My*  
	sudo nano /etc/hostconfig     (复制前面部分回车，然后删掉这一行: MYSQLCOM=-YES-，control+O回车保存，control+X退出编辑界面)  
	sudo rm -rf ~/Library/PreferencePanes/My*  
	sudo rm -rf /Library/Receipts/mysql*  
	sudo rm -rf /Library/Receipts/MySQL*  
	sudo rm -rf /var/db/receipts/com.mysql.*


[MYSQL MAC客户端工具](https://sequelpro.com/download#auto-start)
# Mysql

* 更新软件包列表：`sudo apt update`
* 安装MySQL软件包：`sudo apt install mysql-server`
* 启动MySQL服务：`sudo systemctl start mysql`
* 进行安全初始化：`sudo mysql_secure_installation`
* 设置或更改密码（默认安装是没有设置密码的，需要我们自己设置密码。）
	```shell
	 mysql> use mysql;
	 mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
	 mysql> flush privileges;
	 mysql> quit;
	```

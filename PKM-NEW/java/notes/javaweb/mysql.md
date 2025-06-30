# MYSQL

## 连接操作

* -u 用户名
* -p 密码
* -h 主机名，默认是localhost
* -P 端口号，默认是3306
* -D 数据库名
* -e 执行sql语句

案例
```bash
mysql -u root -p -h localhost -P 3306 -D test -e "select * from user;"
```

## 数据库操作（DDL）

```sql
-- 查询
show databases;
-- 创建
create database test;
-- 删除
drop database test;
-- 使用
use test;
-- 查看当前数据库
select database();
```

推荐使用可以支持emoj表情的编码：utf8mb4（MySQL 8.0+ 就是默认了）

```sql
create database test character set utf8mb4 collate utf8mb4_general_ci;
```
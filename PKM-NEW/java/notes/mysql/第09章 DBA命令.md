# 新建用户
创建一个用户名为java1，密码设置为123的本地用户：
```sql
create user 'java1'@'localhost' identified by '123';
```
创建一个用户名为java2，密码设置为123的外网用户：
```sql
create user 'java2'@'%' identified by '123';
```
采用以上方式新建的用户没有任何权限：系统表也只能看到以下两个
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679813363625-10cc7c30-76b3-4a1a-a83f-a1727489a420.png#averageHue=%23141211&clientId=u8834b383-d147-4&from=paste&height=197&id=u9bbde222&originHeight=197&originWidth=318&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6925&status=done&style=shadow&taskId=ub1483b88-60e6-4eac-a9d2-c1eb024463f&title=&width=318)
使用root用户查看系统中当前用户有哪些？
```sql
select user,host from mysql.user;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=L1FfU&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 给用户授权
授权语法：grant [权限1，权限2...] on 库名.表名 to '用户名'@'主机名/IP地址';
给本地用户授权：grant [权限1，权限2...] on 库名.表名 to '用户名'@'localhost';
给外网用户授权：grant [权限1，权限2...] on 库名.表名 to '用户名'@'%';
所有权限：all privileges
细粒度权限：select、insert、delete、update、alter、create、drop、index(索引)、usage(登录权限)......
库名可以使用 * ，它代表所有数据库
表名可以采用 * ，它代表所有表
也可以提供具体的数据库和表，例如：powernode.emp （powernode数据库的emp表）

```sql
# 将所有库所有表的查询权限赋予本地用户java1
grant select,insert,delete,update,create on *.* to 'java1'@'localhost';

# 将powernode库中所有表的所有权限赋予本地用户java1
grant all privileges on powernode.* to 'java1'@'localhost';
```
授权后必须刷新权限，才能生效：flush privileges
查看某个用户拥有哪些权限？
show grants for 'java1'@'localhost'
show grants for 'java2'@'%'

with grant option：

```sql
# with grant option的作用是：java2用户也可以给其他用户授权了。
grant select,insert,delete,update on *.* to 'java2'@'%' with grant option;
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=SE1yi&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 撤销用户权限
revoke 权限 on 数据库名.表名 from '用户'@'IP地址';
```sql
# 撤销本地用户java1的insert、update、delete权限
revoke insert, update, delete on powernode.* from 'java1'@'localhost'

# 撤销外网用户java2的insert权限
revoke insert on powernode.* from 'java2'@'%'
```
撤销权限后也需要刷新权限：flush privileges

注意：撤销权限时 “数据库名.表名” 不能随便写，要求和授权语句时的 “数据库名.表名” 一致。

# 修改用户的密码
具有管理用户权限的用户才能修改密码，例如root账户可以修改其他账户的密码：
```sql
# 本地用户修改密码
alter user 'java1'@'localhost' identified by '456';

# 外网用户修改密码
alter user 'java2'@'%' identified by '456';
```
修改密码后，也需要刷新权限才能生效：flush privileges
以上是MySQL8版本以后修改用户密码的方式。
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=zlA3C&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 修改用户名
```sql
rename user '原始用户名'@'localhost' to '新用户名'@'localhost';
rename user '原始用户名'@'localhost' to '新用户名'@'%';

rename user 'java1'@'localhost' to 'java11'@'localhost';
rename user 'java11'@'localhost' to 'java123'@'%';
```
flush privileges;
# 删除用户
```sql
drop user 'java123'@'localhost';
drop user 'java2'@'%';
```
flush privileges;
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=OUoZv&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
# 数据备份

- 导出数据（请在登录mysql数据库之前进行）
```sql
# 导出powernode这个数据库中所有的表
mysqldump powernode > e:/powernode.sql -uroot -p1234 --default-character-set=utf8

# 导出powernode中emp表的数据
mysqldump powernode emp > e:/powernode.sql -uroot -p1234 --default-character-set=utf8
```

- 导入数据第一种方式：（请在登录mysql之前进行）

```sql
# 现在登录mysql状态下新建一个数据库
create database powernode;
# 在登录mysql之前执行以下命令
mysql powernode < e:/powernode.sql -uroot -p1234 --default-character-set=utf8
```

- 导入数据第二种方式：（请在登录mysql之后操作）

```sql
create  database powernode;
use powernode;
source d:/powernode.sql
```
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg?x-oss-process=image%2Fresize%2Cw_1177%2Climit_0%2Finterlace%2C1%2Finterlace%2C1#averageHue=%23f9f8f8&from=url&id=MMQTP&originHeight=66&originWidth=1177&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

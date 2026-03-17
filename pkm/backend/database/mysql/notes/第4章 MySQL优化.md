# MySQL优化手段

MySQL数据库的优化手段通常包括但不限于：
- SQL查询优化：这是最低成本的优化手段，通过优化查询语句、适当添加索引等方式进行。并且效果显著。
- 库表结构优化：通过规范化设计、优化索引和数据类型等方式进行库表结构优化，需要对数据库结构进行调整和改进
- 系统配置优化：根据硬件和操作系统的特点，调整最大连接数、内存管理、IO调度等参数
- 硬件优化：升级硬盘、增加内存容量、升级处理器等硬件方面的投入，需要购买和替换硬件设备，成本较高

我们主要掌握：SQL查询优化

---
## SQL性能分析工具

### 查看数据库整体情况
通过以下命令可以查看当前数据库在SQL语句执行方面的整体情况：
```sql
show global status like 'Com_select';
show global status like 'Com_insert';
show global status like 'Com_delete';
show global status like 'Com_update';

show global status like 'Com_______';
```
这些结果反映了从 MySQL 服务器启动到当前时刻，所有的 SELECT 查询总数。对于 MySQL 性能优化来说，通过查看 `Com_select` 的值可以了解 SELECT 查询在整个 MySQL 服务期间所占比例的情况：

- 如果 `Com_select` 次数过高，可能说明查询表中的每条记录都会返回过多的字段。
- 如果 `Com_select` 次数很少，同时insert或delete或update的次数很高，可能说明服务器运行的应用程序过于依赖写入操作和少量读取操作。

总之，通过查看 `Com_select` 的值，可以了解 MySQL 服务器的长期执行情况，并在优化查询性能时，帮助我们了解 MySQL 的性能瓶颈。

### 慢查询日志
慢查询日志文件可以将查询较慢的DQL语句记录下来，便于我们定位需要调优的select语句。
通过以下命令查看慢查询日志功能是否开启：
```sql
show variables like 'slow_query_log';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709606608296-a4ccd38c-c353-4a5e-bd8c-9d51d15374ff.png#averageHue=%23161412&clientId=u1bbf35a1-ca62-4&from=paste&height=112&id=u210c5b81&originHeight=112&originWidth=315&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4586&status=done&style=none&taskId=u261aee54-a8a7-468c-ad22-c9059861cb2&title=&width=315)
慢查询日志功能默认是关闭的。请修改my.ini文件来开启慢查询日志功能，在my.ini的[mysqld]后面添加如下配置：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709606812974-8aff10a9-5595-41aa-a64b-ea1d1b666999.png#averageHue=%23fdfaf8&clientId=u1bbf35a1-ca62-4&from=paste&height=285&id=ueaebdf7e&originHeight=285&originWidth=350&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10518&status=done&style=none&taskId=uceb1546e-7784-4eea-8d71-9443c9b3149&title=&width=350)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709606969144-3bf8c279-f05b-4788-98b5-0c891bb40585.png#averageHue=%23f3f1ef&clientId=u1bbf35a1-ca62-4&from=paste&height=127&id=ua72cf8e3&originHeight=127&originWidth=316&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6526&status=done&style=none&taskId=u3d056f4c-25b1-4e32-9a5d-644198b3a6b&title=&width=316)
注意：slow_query_log=1表示开启慢查询日志功能，long_query_time=3表示：只要SELECT语句的执行耗时超过3秒则将其记录到慢查询日志中。
重启mysql服务。再次查看是否开启慢查询日志功能：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709606848489-73c9ee06-7264-4e69-9f82-557973eec793.png#averageHue=%23141210&clientId=u1bbf35a1-ca62-4&from=paste&height=211&id=ub5e18942&originHeight=211&originWidth=480&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21908&status=done&style=none&taskId=udef397a2-544d-4195-bc54-4c868c41303&title=&width=480)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709606863859-18c78fe1-1e63-4f41-b4c1-cab73d311927.png#averageHue=%2313110f&clientId=u1bbf35a1-ca62-4&from=paste&height=183&id=u51e64fd1&originHeight=183&originWidth=549&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11421&status=done&style=none&taskId=u6fd5f422-e867-4432-beaf-60017743f43&title=&width=549)

尝试执行一条时长超过3秒的select语句：
```sql
select empno,ename,sleep(4) from emp where ename='smith';
```

慢查询日志文件默认存储在：C:\dev\mysql-8.0.36-winx64\data 目录下，默认的名字是：计算机名-slow.log
通过该文件可以清晰的看到哪些DQL语句属于慢查询：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709607677892-55420a92-0c66-4dff-a34e-85ba3ef1fa77.png#averageHue=%23f6f2f0&clientId=u1bbf35a1-ca62-4&from=paste&height=360&id=u5357d1d9&originHeight=360&originWidth=1264&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40700&status=done&style=shadow&taskId=u96de1bce-7f1e-4608-8eec-88635aa660f&title=&width=1264)

### show profiles
通过show profiles可以查看一个SQL语句在执行过程中具体的耗时情况。帮助我们更好的定位问题所在。

查看当前数据库是否支持 profile操作：
```sql
select @@have_profiling;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709608207454-21a4e8a0-aaed-4c7e-a145-8e006efc79b5.png#averageHue=%23121110&clientId=u1bbf35a1-ca62-4&from=paste&height=138&id=uc91f2727&originHeight=138&originWidth=413&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7034&status=done&style=shadow&taskId=uecb73d27-9d3d-4149-897b-58179fb9dbf&title=&width=413)

查看 profiling 开关是否打开：
```sql
select @@profiling;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709608223016-c81a692f-11f4-4cf9-89ab-73d7ccb17327.png#averageHue=%23121110&clientId=u1bbf35a1-ca62-4&from=paste&height=138&id=ud07b7db5&originHeight=138&originWidth=365&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5765&status=done&style=shadow&taskId=u7841096e-d19e-400d-acc1-2ea0eb71b11&title=&width=365)

将 profiling 开关打开：
```sql
set profiling = 1;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709608246449-a1a5b6a5-64ae-453c-8e75-c14734c08a2e.png#averageHue=%23100f0e&clientId=u1bbf35a1-ca62-4&from=paste&height=250&id=u948237d1&originHeight=250&originWidth=576&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15181&status=done&style=shadow&taskId=ue2e11072-5cad-41f6-87f8-6b4ebb4fb3f&title=&width=576)

可以执行多条DQL语句，然后使用 show profiles; 来查看当前数据库中执行过的每个SELECT语句的耗时情况。
```sql
select empno,ename from emp;
select empno,ename from emp where empno=7369;
select count(*) from emp;
show profiles;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709608477900-aef25ddf-a9ea-4caa-982c-633a75adc684.png#averageHue=%23141211&clientId=u1bbf35a1-ca62-4&from=paste&height=185&id=ue1ad13db&originHeight=185&originWidth=870&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17479&status=done&style=shadow&taskId=u5b746d60-cce8-4d00-86fd-a87e1e326b3&title=&width=870)

查看某个SQL语句语句在执行过程中，每个阶段的耗时情况：
```sql
show profile for query 4;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709608620665-462b1fae-d1bb-49cb-9fc0-a4ee4e74e8a9.png#averageHue=%23141210&clientId=u1bbf35a1-ca62-4&from=paste&height=490&id=ue2e1a07e&originHeight=490&originWidth=546&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38244&status=done&style=shadow&taskId=u679c4a6c-fe2d-415a-8c1d-61331ac89de&title=&width=546)

想查看执行过程中cpu的情况，可以执行以下命令：
```sql
show profile cpu for query 4;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709608704507-1e11a01d-cf8d-4208-9d1e-1a55287e8c0d.png#averageHue=%23161311&clientId=u1bbf35a1-ca62-4&from=paste&height=490&id=u28beb940&originHeight=490&originWidth=831&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44398&status=done&style=shadow&taskId=u99024dea-0f7d-4b4f-8d21-1e097d5070e&title=&width=831)


### explain
explain命令可以查看一个DQL语句的执行计划，根据执行计划可以做出相应的优化措施。提高执行效率。
```sql
explain select * from emp where empno=7369;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709802585549-f377b6db-7fff-4b76-8c8f-8770df3f6b7f.png#averageHue=%23f2f1f0&clientId=u35b840e1-8af8-4&from=paste&height=76&id=u83c0f5ad&originHeight=76&originWidth=1414&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5085&status=done&style=shadow&taskId=ueb9576b2-b431-461d-9fe8-1ccd9ecfe0e&title=&width=1414)

#### id
id反映出一条select语句执行顺序，id越大优先级越高。id相同则按照自上而下的顺序执行。
```sql
explain select e.ename,d.dname from emp e join dept d on e.deptno=d.deptno join salgrade s on e.sal between s.losal and s.hisal;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709802962333-8700f0d2-9db0-4ccb-b35a-20dcb0189ca4.png#averageHue=%23f2f1f0&clientId=u35b840e1-8af8-4&from=paste&height=102&id=ubd183a12&originHeight=102&originWidth=1419&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10534&status=done&style=shadow&taskId=u5c7862c4-b39c-4a1c-8fd3-4a0b01c87c7&title=&width=1419)
由于id相同，反映出三张表在执行顺序上属于平等关系，执行时采用，先d，再e，最后s。
```sql
explain select e.ename,d.dname from emp e join dept d on e.deptno=d.deptno where e.sal=(select sal from emp where ename='ford');
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709803180821-4cb09e82-1c77-4ecd-b943-e087f9c736a0.png#averageHue=%23f3f3f2&clientId=u35b840e1-8af8-4&from=paste&height=111&id=u33484cc8&originHeight=111&originWidth=1425&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10128&status=done&style=shadow&taskId=u9a25fc3d-c6b9-4a11-af93-f842d73f328&title=&width=1425)
反映出，先执行子查询，然后让e和d做表连接。


#### select_type
反映了mysql查询语句的类型。常用值包括：

- SIMPLE：表示查询中不包含子查询或UNION操作。这种查询通常包括一个表或是最多一个联接（JOIN）
- PRIMARY：表示当前查询是一个主查询。（主要的查询）
- UNION：表示查询中包含UNION操作
- SUBQUERY：子查询
- DERIVED：派生表（表示查询语句出现在from后面）

#### table
反映了这个查询操作的是哪个表。

#### type
反映了查询表中数据时的访问类型，常见的值：

1. NULL：效率最高，一般不可能优化到这个级别，只有查询时没有查询表的时候，访问类型是NULL。例如：select 1;
2. system：通常访问系统表的时候，访问类型是system。一般也很难优化到这个程序。
3. const：根据主键或者唯一性索引查询，索引值是常量值时。explain select * from emp where empno=7369;
4. eq_ref：根据主键或者唯一性索引查询。索引值不是常量值。
5. ref：使用了非唯一的索引进行查询。
6. range：使用了索引，扫描了索引树的一部分。
7. index：表示用了索引，但是也需要遍历整个索引树。
8. all：全表扫描

效率最高的是NULL，效率最低的是all，从上到下，从高到低。


#### possible_keys
这个查询可能会用到的索引

#### key
实际用到的索引

#### key_len
反映索引中在查询中使用的列所占的总字节数。

#### rows
查询扫描的预估计行数。

#### Extra
给出了与查询相关的额外信息和说明。这些额外信息可以帮助我们更好地理解查询执行的过程。

---
# 索引优化
## 加索引 vs 不加索引
将这个sql脚本初始化到数据库中（初始化100W条记录）：t_vip.sql
根据id查询（id是主键，有索引）：
```sql
select * from t_vip where id = 900000;
```

根据name查询（name上没有索引）：
```sql
select * from t_vip where name='4c6494cb';
```

给name字段添加索引：
```sql
create index idx_t_user_name on t_vip(name);
```

再次根据name查询（此时name上已经有索引了） ：
```sql
select * from t_vip where name='4c6494cb';
```


## 最左前缀原则
假设有这样一张表：
```sql
create table t_customer(
    id int primary key auto_increment,
    name varchar(255),
    age int,
    gender char(1),
    email varchar(255)
);
```
添加了这些数据：
```sql
insert into t_customer values(null, 'zhangsan', 20, 'M', 'zhangsan@123.com');
insert into t_customer values(null, 'lisi', 22, 'M', 'lisi@123.com');
insert into t_customer values(null, 'wangwu', 18, 'F', 'wangwu@123.com');
insert into t_customer values(null, 'zhaoliu', 22, 'F', 'zhaoliu@123.com');
insert into t_customer values(null, 'jack', 30, 'M', 'jack@123.com');
```
添加了这样的复合索引：
```sql
create index idx_name_age_gender on t_customer(name,age,gender);
```
**最左前缀原则：当查询语句条件中包含了这个复合索引最左边的列 name 时，此时索引才会起作用。**

验证1：
```sql
explain select * from t_customer where name='zhangsan' and age=20 and gender='M';
```
验证结果：完全使用了索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709620707530-1bf42ae8-0a5a-48d4-a175-f63cd590cc27.png#averageHue=%23f0efee&clientId=u75f16c53-61e9-4&from=paste&height=77&id=u9b1a3cd4&originHeight=77&originWidth=1233&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6530&status=done&style=shadow&taskId=ue11ca645-e658-44d2-a33c-ad9d556733a&title=&width=1233)

验证2：
```sql
explain select * from t_customer where name='zhangsan' and age=20;
```
验证结果：使用了部分索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709620741009-6e68b6e8-72f9-4dac-b81c-4a7a83e2fc3d.png#averageHue=%23efeded&clientId=u75f16c53-61e9-4&from=paste&height=69&id=ue40d9726&originHeight=69&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6262&status=done&style=shadow&taskId=ue029fc49-fb04-463d-b957-6fbe89123ca&title=&width=1226)

验证3：
```sql
explain select * from t_customer where name='zhangsan';
```
验证结果：使用了部分索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709620763950-41d223ab-585f-413d-a57b-4974c6f0beab.png#averageHue=%23efeeed&clientId=u75f16c53-61e9-4&from=paste&height=72&id=u8bce969b&originHeight=72&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6335&status=done&style=shadow&taskId=ua9f2ed2a-6f4e-4363-8a9c-e49cffdb37c&title=&width=1226)

验证4：
```sql
explain select * from t_customer where age=20 and gender='M' and name='zhangsan';
```
验证结果：完全使用了索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709620790877-981fb10c-d890-45ba-a216-7657788fb107.png#averageHue=%23f3f2f1&clientId=u75f16c53-61e9-4&from=paste&height=98&id=u8406d237&originHeight=98&originWidth=1231&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7142&status=done&style=shadow&taskId=ud8c1fc7d-77b0-4764-9e68-b2bedac00c9&title=&width=1231)

验证5：
```sql
explain select * from t_customer where gender='M' and age=20;
```
验证结果：没有使用任何索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709620812205-51aeb294-baeb-4170-9aec-9227568689e8.png#averageHue=%23f1f1f0&clientId=u75f16c53-61e9-4&from=paste&height=76&id=uaede0bcd&originHeight=76&originWidth=1224&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5254&status=done&style=shadow&taskId=ucfc9e344-95a0-4783-a44e-436766ba3e8&title=&width=1224)

验证6：
```sql
explain select * from t_customer where name='zhangsan' and gender='M';
```
验证结果：使用了部分索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709620943989-005425b6-42c5-4ed5-93ec-f60966f7a62a.png#averageHue=%23f2f0f0&clientId=u75f16c53-61e9-4&from=paste&height=87&id=u06dd06a9&originHeight=87&originWidth=1225&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6567&status=done&style=shadow&taskId=uf1143a9e-dd31-4173-ac3e-17d0dac7968&title=&width=1225)

验证7：
```sql
explain select * from t_customer where name='zhangsan' and gender='M' and age=20;
```
验证结果：完全使用了索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709621197079-aea69012-aa33-43fd-ac04-4e836a41ac49.png#averageHue=%23f2f0f0&clientId=u75f16c53-61e9-4&from=paste&height=86&id=u5af42892&originHeight=86&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6520&status=done&style=shadow&taskId=u89b6599c-fef6-481c-b822-662c6eac2ee&title=&width=1226)

**范围查询时，在“范围条件”右侧的列索引会失效：**
验证：
```sql
explain select * from t_customer where name='zhangsan' and age>20 and gender='M';
```
验证结果：name和age列索引生效。gender列索引无效。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709621337919-fa59c6b8-6bdd-47f8-bb5d-1c944ca8d1f3.png#averageHue=%23f1efee&clientId=u75f16c53-61e9-4&from=paste&height=77&id=ufc1c332e&originHeight=77&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6427&status=done&style=shadow&taskId=u34989e10-0f7b-471c-aafd-1b2ed3e647f&title=&width=1226)
怎么解决？建议范围查找时带上“=”
```sql
explain select * from t_customer where name='zhangsan' and age>=20 and gender='M';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709621423612-619d1ea5-3b98-4947-ab73-6f0ac42cfddf.png#averageHue=%23f1f0ef&clientId=u75f16c53-61e9-4&from=paste&height=82&id=u25f8a2d7&originHeight=82&originWidth=1229&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6657&status=done&style=shadow&taskId=u17028540-44fd-440f-9cd8-594c7a1d182&title=&width=1229)


## 索引失效情况
有这样一张表：
```sql
create table t_emp(
  id int primary key auto_increment,
  name varchar(255),
  sal int,
  age char(2)
);
```
有这样一些数据：
```sql
insert into t_emp values(null, '张三', 5000,'20');
insert into t_emp values(null, '张飞', 4000,'30');
insert into t_emp values(null, '李飞', 6000,'40');
```
有这样一些索引：
```sql
create index idx_t_emp_name on t_emp(name);
create index idx_t_emp_sal on t_emp(sal);
create index idx_t_emp_age on t_emp(age);
```


### 索引列参加了运算，索引失效
```sql
explain select * from t_emp where sal > 5000;
```
验证结果：使用了索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709622626287-156e8f2e-9233-40ee-9740-fc13bac956b2.png#averageHue=%23f1f0f0&clientId=u75f16c53-61e9-4&from=paste&height=82&id=ue86c4189&originHeight=82&originWidth=1230&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5886&status=done&style=shadow&taskId=uda74fd1b-4c94-4936-8813-79cba63b06c&title=&width=1230)
```sql
explain select * from t_emp where sal*10 > 50000;
```
验证结果：索引失效
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709622656653-0408c8c3-8c58-4856-a7f2-407a33255882.png#averageHue=%23f0efee&clientId=u75f16c53-61e9-4&from=paste&height=68&id=ua9cb8fa0&originHeight=68&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5004&status=done&style=shadow&taskId=u76feb04f-430d-4b0d-abca-bde56a34eaa&title=&width=1226)

### 索引列进行模糊查询时以 % 开始的，索引失效
```sql
explain select * from t_emp where name like '张%';
```
验证结果：索引有效
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709622777843-e993f862-6523-48db-b5ec-fd6b8d6b81a8.png#averageHue=%23f2f0f0&clientId=u75f16c53-61e9-4&from=paste&height=82&id=uac080f8b&originHeight=82&originWidth=1227&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6041&status=done&style=shadow&taskId=uc660d0c7-51e9-43a4-bcbc-df0a5f55ed1&title=&width=1227)
```sql
explain select * from t_emp where name like '%飞';
```
验证结果：索引失效
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709622812719-bffd2a58-de91-413c-bbe9-afef66216412.png#averageHue=%23f2f1f1&clientId=u75f16c53-61e9-4&from=paste&height=83&id=u3307c19b&originHeight=83&originWidth=1232&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5167&status=done&style=shadow&taskId=u9dc0622b-972e-49d5-a0a1-85e40e0240e&title=&width=1232)
### 索引列是字符串类型，但查询时省略了单引号，索引失效
```sql
explain select * from t_emp where age='20';
```
验证结果：索引有效
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709623022492-47eb2402-b727-4c24-adc7-3985c2fbca3d.png#averageHue=%23f1f0f0&clientId=u75f16c53-61e9-4&from=paste&height=80&id=u2d1c59de&originHeight=80&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5271&status=done&style=shadow&taskId=u575e101b-560c-4351-aafd-cec3189afa9&title=&width=1226)

```sql
explain select * from t_emp where age=20;
```
验证结果：索引失效
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709623062895-ec669b01-a288-4403-b3a0-d6c0a6b50b77.png#averageHue=%23f2f2f1&clientId=u75f16c53-61e9-4&from=paste&height=82&id=uf90aa3b5&originHeight=82&originWidth=1231&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5368&status=done&style=shadow&taskId=u0e061030-0742-44e8-ac24-08c8ed27f98&title=&width=1231)


### 查询条件中有or，只要有未添加索引的字段，索引失效
```sql
explain select * from t_emp where name='张三' or sal=5000;
```
验证结果：使用了索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709623659977-13993818-9310-4e1c-a472-f0e56902ccc6.png#averageHue=%23f4f3f2&clientId=u75f16c53-61e9-4&from=paste&height=99&id=u27003f00&originHeight=99&originWidth=1362&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7084&status=done&style=shadow&taskId=ue6a2c5be-88a8-4a37-abfe-f8b11181877&title=&width=1362)

将t_emp表sal字段上的索引删除：
```sql
alter table t_emp drop index idx_t_emp_sal;
```
再次验证：
```sql
explain select * from t_emp where name='张三' or sal=5000;
```
验证结果：索引失效
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709623713074-9e8ee071-84ce-44e9-89e4-d3a3f9534ddd.png#averageHue=%23f1f0ef&clientId=u75f16c53-61e9-4&from=paste&height=72&id=u7e588147&originHeight=72&originWidth=1345&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5460&status=done&style=shadow&taskId=u81c8b944-dc24-4197-9d97-d02f5be4450&title=&width=1345)


### 当查询的符合条件的记录在表中占比较大，索引失效
复制一张新表：emp2
```sql
create table emp2 as select * from emp;
```
给sal添加索引：
```sql
alter table emp2 add index idx_emp2_sal(sal);
```

验证1：
```sql
explain select * from emp2 where sal > 800;
```
不走索引：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709624416152-f79a2fd0-f440-4848-9ebf-af30955177fa.png#averageHue=%23f1f0ef&clientId=u75f16c53-61e9-4&from=paste&height=71&id=ubaa14cc4&originHeight=71&originWidth=1352&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5596&status=done&style=shadow&taskId=u6c5eb6e8-7879-411d-ad7c-01118b70c77&title=&width=1352)

验证2：
```sql
explain select * from emp2 where sal > 1000;
```
不走索引：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709624416152-f79a2fd0-f440-4848-9ebf-af30955177fa.png#averageHue=%23f1f0ef&clientId=u75f16c53-61e9-4&from=paste&height=71&id=hAdjc&originHeight=71&originWidth=1352&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5596&status=done&style=shadow&taskId=u6c5eb6e8-7879-411d-ad7c-01118b70c77&title=&width=1352)

验证3：
```sql
explain select * from emp2 where sal > 2000;
```
走索引：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709624457745-c7680a75-84cb-4569-9b4e-07cdfdd08135.png#averageHue=%23f1f0ef&clientId=u75f16c53-61e9-4&from=paste&height=73&id=ubf126d85&originHeight=73&originWidth=1348&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5397&status=done&style=shadow&taskId=u8706c3c4-8968-4685-8b58-199b5c47842&title=&width=1348)


### 关于is null和is not null的索引失效问题
给emp2的comm字段添加一个索引：
```sql
create index idx_emp2_comm on emp2(comm);
```
将emp2表的comm字段值全部更新为NULL：
```sql
update emp2 set comm=null;
```

验证此时条件使用is null是否走索引：
```sql
explain select * from emp2 where comm is null;
```
验证结果：不走索引。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709694195151-1ca17464-4c88-45fa-b219-cb08f0b5091c.png#averageHue=%23f0efef&clientId=u832e6504-1b74-4&from=paste&height=68&id=u37bd1e0d&originHeight=68&originWidth=1351&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5412&status=done&style=shadow&taskId=u3c332f0e-d44b-47ce-8ae1-93ec5c5fd10&title=&width=1351)
验证此时条件使用is not null是否走索引：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709694228684-a0adc3b3-2e1f-42a9-bc04-e9b3794f4c07.png#averageHue=%23eeedec&clientId=u832e6504-1b74-4&from=paste&height=61&id=u46c4c324&originHeight=61&originWidth=1348&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5257&status=done&style=shadow&taskId=ub8dbdb4b-ae22-42b7-9365-d62ded3075f&title=&width=1348)

将emp2表的comm字段全部更新为非NULL：
```sql
update emp2 set comm=100;
```

验证此时条件使用is null是否走索引：
```sql
explain select * from emp2 where comm is null;
```
验证结果：走索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709694340514-f50fe8fb-362e-4ab4-b34d-0e2f914bafe2.png#averageHue=%23efeeed&clientId=u832e6504-1b74-4&from=paste&height=64&id=u5926030e&originHeight=64&originWidth=1354&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5293&status=done&style=shadow&taskId=ua3e13478-ec0b-4df6-bb04-0e53d9b65be&title=&width=1354)
验证此时条件使用is not null是否走索引：
```sql
explain select * from emp2 where comm is not null;
```
验证结果：不走索引
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709694398287-3000e893-0a5a-4284-a110-968a9f651b6e.png#averageHue=%23efeeee&clientId=u832e6504-1b74-4&from=paste&height=68&id=u4e6beae8&originHeight=68&originWidth=1354&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5632&status=done&style=shadow&taskId=u944ca771-d4e6-433a-abf2-7ea376745fd&title=&width=1354)

结论：走索引还是不走索引，根数据分布有很大关系，如果符合条件的记录占比较大，会考虑使用全表扫描，而放弃走索引。


## 指定索引
当一个字段上既有单列索引，又有复合索引时，我们可以通过以下的SQL提示来要求该SQL语句执行时采用哪个索引：

- use index(索引名称)：建议使用该索引，只是建议，底层mysql会根据实际效率来考虑是否使用你推荐的索引。
- ignore index(索引名称)：忽略该索引
- force index(索引名称)：强行使用该索引

查看 t_customer 表上的索引：
```sql
show index from t_customer;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709695662786-e69e7393-fb4e-4ca9-a167-b81c6d1dcef4.png#averageHue=%23f9f8f6&clientId=u832e6504-1b74-4&from=paste&height=141&id=u8027b76a&originHeight=141&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11140&status=done&style=shadow&taskId=ufccb1506-f046-49af-86f8-ce60b1efc15&title=&width=950)
可以看到name age gender三列添加了一个复合索引。
现在给name字段添加一个单列索引：
```sql
create index idx_name on t_customer(name);
```
看看以下的语句默认使用了哪个索引：
```sql
explain select * from t_customer where name='zhangsan';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709695789495-7937dbd6-1c3b-4881-aeac-e868dd7e818d.png#averageHue=%23f5f4f3&clientId=u832e6504-1b74-4&from=paste&height=108&id=u0fe537ca&originHeight=108&originWidth=1350&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7064&status=done&style=shadow&taskId=u794e7ad2-d26f-4479-be56-b81c7464a7b&title=&width=1350)
通过测试得知，默认使用了联合索引。

如何建议使用单列索引idx_name：
```sql
explain select * from t_customer use index(idx_name) where name='zhangsan';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709695922746-7c298082-197e-49a9-be41-68a80eb1d8cd.png#averageHue=%23eeedec&clientId=u832e6504-1b74-4&from=paste&height=61&id=uacfb4dc3&originHeight=61&originWidth=1347&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5173&status=done&style=shadow&taskId=uc2f18419-fc69-4dab-9b1e-6fb98a1a3a9&title=&width=1347)

如何忽略使用符合索引 idx_name_age_gender：
```sql
explain select * from t_customer ignore index(idx_name_age_gender) where name='zhangsan';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709695945125-1fdb373d-e99d-40ff-ba0c-116f323de32a.png#averageHue=%23f1f0f0&clientId=u832e6504-1b74-4&from=paste&height=77&id=u2059b06f&originHeight=77&originWidth=1346&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5375&status=done&style=shadow&taskId=u66156ea8-68db-4846-82dd-0108c69e814&title=&width=1346)

如何强行使用单列索引idx_name：
```sql
explain select * from t_customer force index(idx_name) where name='zhangsan';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709695965581-f97fc288-0420-4fd5-9fc6-b5a6d398389b.png#averageHue=%23f2f1f0&clientId=u832e6504-1b74-4&from=paste&height=79&id=u62a0d9e3&originHeight=79&originWidth=1338&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5357&status=done&style=shadow&taskId=ud0ebd6c4-faf9-4cd0-8008-99a6a1fccad&title=&width=1338)


## 覆盖索引
覆盖索引我们在讲解索引的时候已经提到过了，覆盖索引强调的是：在select后面写字段的时候，这些字段尽可能是索引所覆盖的字段，这样可以避免回表查询。尽可能避免使用 select *，因为select * 很容易导致回表查询。（本质就是：能在索引上检索的，就不要再次回表查询了。）

例如：有一张表 emp3，其中 ename,job添加了联合索引：idx_emp3_ename_job，以下这个select语句就不会回表：
```sql
drop table if exists emp3;
create table emp3 as select * from emp;
alter table emp3 add constraint emp3_pk primary key(empno);
create index idx_emp3_ename_job on emp3(ename,job);
explain select empno,ename,job from emp3 where ename='KING';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709869967499-4087b2ec-38ec-423c-bc35-b6beea430958.png#averageHue=%23caa768&clientId=ucd943da5-f2f2-4&from=paste&height=83&id=u594bc3ee&originHeight=83&originWidth=1452&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6563&status=done&style=shadow&taskId=ue01a5a68-4bec-43a6-bf60-76b7c1ca78e&title=&width=1452)
如果查询语句要查找的列没有在索引中，则会回表查询，例如：
```sql
explain select empno,ename,job,sal from emp3 where ename='KING';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709870027544-6ff21f88-252e-4ea0-863c-7cbc60244423.png#averageHue=%23f3f1f0&clientId=ucd943da5-f2f2-4&from=paste&height=85&id=u1a058cfb&originHeight=85&originWidth=1495&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7712&status=done&style=shadow&taskId=u1216ccd4-32e7-4a53-8027-83ae45ea842&title=&width=1495)
面试题：t_user表字段如下：id,name,password,realname,birth,email。表中数据量500万条，请针对以下SQL语句给出优化方案：
```sql
select id,name,realname from t_user where name='鲁智深';
```
如果只给name添加索引，底层会进行大量的回表查询，效率较低，建议给name和realname两个字段添加联合索引，这样大大减少回表操作，提高查询效率。


## 前缀索引
如果一个字段类型是varchar或text字段，字段中存储的是文本或者大文本，直接对这种长文本创建索引，会让索引体积很大，怎么优化呢？可以将字符串的前几个字符截取下来当做索引来创建。这种索引被称为前缀索引，例如：
```sql
drop table if exists emp4;
create table emp4 as select * from emp;
create index idx_emp4_ename_2 on emp4(ename(2));
```
以上SQL表示将emp4表中ename字段的前2个字符创建到索引当中。

使用前缀索引时，需要通过以下公式来确定使用前几个字符作为索引：
```sql
select count(distinct substring(ename,1,前几个字符)) / count(*) from emp4;
```
以上查询结果越接近1，表示索引的效果越好。（原理：做索引值的话，索引值越具有唯一性效率越高）

假设我们使用前1个字符作为索引值：
```sql
select count(distinct substring(ename,1,1)) / count(*) from emp4;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709710923936-8ad47445-f0fc-4dd0-848d-d2035635bf42.png#averageHue=%23d3d1d0&clientId=u832e6504-1b74-4&from=paste&height=55&id=u30d177c0&originHeight=55&originWidth=176&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1645&status=done&style=shadow&taskId=uff63c5ed-375f-4cc0-a85b-01ea782449e&title=&width=176)

假设我们使用前2个字符作为索引值：
```sql
select count(distinct substring(ename,1,2)) / count(*) from emp4;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709710960232-d16e0bfd-3d49-45f5-b4cd-5bc2543ec6bf.png#averageHue=%23d0cecd&clientId=u832e6504-1b74-4&from=paste&height=50&id=ucad3b1a8&originHeight=50&originWidth=182&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1351&status=done&style=shadow&taskId=ueb32d080-9fcb-4f3f-8ad9-0b5d6e4f99d&title=&width=182)
可见使用前2个字符作为索引值，能够让索引值更具有唯一性，效率越好，因此我们选择前2个字符作为前缀索引。
```sql
create index idx_emp4_ename_2 on emp4(ename(2));
```
执行以下的查询语句则会走这个前缀索引：
```sql
explain select * from emp4 where ename='KING';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709711252551-389620f6-0b3e-402f-8279-14714e0b6934.png#averageHue=%23f3f2f2&clientId=u832e6504-1b74-4&from=paste&height=85&id=u516d6059&originHeight=85&originWidth=1449&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5750&status=done&style=shadow&taskId=u29314072-63e8-412a-9e2f-5c304631fcd&title=&width=1449)


## 单列索引和复合索引怎么选择
当查询语句的条件中有多个条件，建议将这几个列创建为复合索引，因为创建单列索引很容易回表查询。
例如分别给emp5表ename，job添加两个单列索引：

```sql
create table emp5 as select * from emp;
alter table emp5 add constraint emp5_pk primary key(empno);

create index idx_emp5_ename on emp5(ename);
create index idx_emp5_job on emp5(job);
```
执行以下查询语句：
```sql
explain select empno,ename,job from emp5 where ename='SMITH' and job='CLERK';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709712992383-465eef54-a764-4b4a-bb7b-d44b6eaf0755.png#averageHue=%23f6f3f3&clientId=u832e6504-1b74-4&from=paste&height=127&id=ub3a37eef&originHeight=127&originWidth=1489&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12323&status=done&style=shadow&taskId=ua0e9fb61-562f-4549-810e-40827bb1858&title=&width=1489)

ename和job都出现在查询条件中，可以给emp6表的ename和job创建一个复合索引：
```sql
create table emp6 as select * from emp;
alter table emp6 add constraint emp6_pk primary key(empno);

create index idx_emp6_ename_job on emp6(ename,job);
explain select empno,ename,job from emp6 where ename='SMITH' and job='CLERK';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709713204610-5a0d695a-170d-447f-9ba0-a5b68719d539.png#averageHue=%23f3f2f2&clientId=u832e6504-1b74-4&from=paste&height=89&id=u38af9318&originHeight=89&originWidth=1473&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5990&status=done&style=shadow&taskId=uec0c7d7e-a85c-4e36-84f6-08136e4672d&title=&width=1473)
对于以上查询语句，使用复合索引避免了回表，因此这种情况下还是建议使用复合索引。

注意：创建索引时应考虑最左前缀原则，主字段并且具有很强唯一性的字段建议排在第一位，例如：
```sql
create index idx_emp_ename_job on emp(ename,job);
```
和以下方式对比：
```sql
create index idx_emp_job_ename on emp(job,ename);
```
由于ename是主字段，并且ename具有很好的唯一性，建议将ename列放在最左边。因此这两种创建复合索引的方式，建议采用第一种。

复合索引底层原理：
![无标题.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709715492890-3ee1db80-14c3-48c9-8e2c-dec200f039d9.png#averageHue=%23bcbbba&clientId=u832e6504-1b74-4&from=paste&height=446&id=u426aad54&originHeight=446&originWidth=1502&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51157&status=done&style=shadow&taskId=u646afbee-d394-4950-9ba3-c06f03041e0&title=&width=1502)


## 索引创建原则

1. 表数据量庞大，通常超过百万条数据。
2. 经常出现在where，order by，group by后面的字段建议添加索引。
3. 创建索引的字段尽量具有很强的唯一性。
4. 如果字段存储文本，内容较大，一定要创建前缀索引。
5. 尽量使用复合索引，使用单列索引容易回表查询。
6. 如果一个字段中的数据不会为NULL，建议建表时添加not null约束，这样优化器就知道使用哪个索引列更加有效。
7. 不要创建太多索引，当对数据进行增删改的时候，索引需要重新重新排序。
8. 如果很少的查询，经常的增删改不建议加索引。 

---
# SQL优化
## order by的优化
准备数据：
```sql
drop table if exists workers;

create table workers(
  id int primary key auto_increment,
  name varchar(255),
  age int,
  sal int
);

insert into workers values(null, '孙悟空', 500, 50000);
insert into workers values(null, '猪八戒', 300, 40000);
insert into workers values(null, '沙和尚', 600, 40000);
insert into workers values(null, '白骨精', 600, 10000);
```

explain查看一个带有order by的语句时，Extra列会显示：using index 或者 using filesort，区别是什么？

- using index:  表示使用索引，因为索引是提前排好序的。效率很高。
- using filesort：表示使用文件排序，这就表示没有走索引，对表中数据进行排序，排序时将硬盘的数据读取到内存当中，在内存当中排好序。这个效率是低的，应避免。

此时name没有添加索引，如果根据name进行排序的话：
```sql
explain select id,name from workers order by name;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709781082541-862ac81e-9a79-4e31-9514-35e97a39279b.png#averageHue=%23f2f1f1&clientId=u35b840e1-8af8-4&from=paste&height=81&id=ufe7325b8&originHeight=81&originWidth=1483&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6475&status=done&style=shadow&taskId=udb902c9b-42b3-4d03-9fec-0e3293b182a&title=&width=1483)
显然这种方式效率较低。
给name添加索引：
```sql
create index idx_workers_name on workers(name);
```
再根据name排序：
```sql
explain select id,name from workers order by name;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709781158431-68a613c1-33d6-46d0-a14b-e0cb855b8681.png#averageHue=%23f3f2f2&clientId=u35b840e1-8af8-4&from=paste&height=85&id=u1d6061b5&originHeight=85&originWidth=1483&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6486&status=done&style=shadow&taskId=u0cf01012-9c92-472c-ac19-31e967efdcd&title=&width=1483)
这样效率则提升了。

如果要通过age和sal两个字段进行排序，最好给age和sal两个字段添加复合索引，不添加复合索引时：
按照age升序排，如果age相同则按照sal升序
```sql
explain select id,age,sal from workers order by age,sal;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709781464653-7d4b762b-70da-409d-a8cc-1026f425ad48.png#averageHue=%23f3f2f1&clientId=u35b840e1-8af8-4&from=paste&height=84&id=ueb311e95&originHeight=84&originWidth=1488&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6279&status=done&style=shadow&taskId=u5de7a94b-04b7-41db-a2b8-250f3b9eecc&title=&width=1488)
这样效率是低的。
给age和sal添加复合索引：
```sql
create index idx_workers_age_sal on workers(age, sal);
```
再按照age升序排，如果age相同则按照sal升序：
```sql
explain select id,age,sal from workers order by age,sal;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709781624043-82823844-ebeb-41cc-8fcb-27a8967e9eea.png#averageHue=%23f4f3f2&clientId=u35b840e1-8af8-4&from=paste&height=91&id=u8383b4b8&originHeight=91&originWidth=1479&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5966&status=done&style=shadow&taskId=ucf411262-97b5-451c-9436-fffb9572004&title=&width=1479)
这样效率提升了。

在B+树上叶子结点上的所有数据默认是按照升序排列的，如果按照age降序，如果age相同则按照sal降序，会走索引吗？
```sql
explain select id,age,sal from workers order by age desc,sal desc;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709781795115-c94583df-3766-4d80-a4f7-8af913d4b0a9.png#averageHue=%23cda567&clientId=u35b840e1-8af8-4&from=paste&height=94&id=u9974ad4c&originHeight=94&originWidth=1425&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7558&status=done&style=shadow&taskId=u6f9dd59d-cca6-40ca-9e74-bb7ead187cb&title=&width=1425)
可以看到备注信息是：反向索引扫描，使用了索引。
这样效率也是很高的，因为B+树叶子结点之间采用的是双向指针。可以从左向右（升序），也可以从右向左（降序）。

如果一个升序，一个降序会怎样呢？
```sql
explain select id,age,sal from workers order by age asc, sal desc;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709782038074-ee34a154-581b-4dd2-9168-5e9cbf762b05.png#averageHue=%23f2f1f0&clientId=u35b840e1-8af8-4&from=paste&height=86&id=u80038654&originHeight=86&originWidth=1329&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6775&status=done&style=shadow&taskId=ub7395e16-2a46-42e5-8ef4-57f82dac0cd&title=&width=1329)
可见age使用了索引，但是sal没有使用索引。怎么办呢？可以针对这种排序情况创建对应的索引来解决：
```sql
create index idx_workers_ageasc_saldesc on workers(age asc, sal desc);
```
创建的索引如下：A表示升序，D表示降序。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709782274642-1cb28544-576c-4c7f-9c0c-cbaaacc9ae6e.png#averageHue=%23f9f7f6&clientId=u35b840e1-8af8-4&from=paste&height=326&id=ue295817c&originHeight=326&originWidth=1504&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27858&status=done&style=shadow&taskId=uf94fe3cb-751c-47e2-b82a-87f5ceb807a&title=&width=1504)
再次执行：

```sql
explain select id,age,sal from workers order by age asc, sal desc;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709782153009-a74b6d7f-b41e-4654-b068-ad5749dbb098.png#averageHue=%23f2f1f1&clientId=u35b840e1-8af8-4&from=paste&height=87&id=u37610f47&originHeight=87&originWidth=1256&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6076&status=done&style=shadow&taskId=u637d549c-e66e-4ea6-99c1-16443b9b7a6&title=&width=1256)

我们再来看看，对于排序来说是否支持最左前缀法则：
```sql
explain select id,age,sal from workers order by sal;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709782435845-ace755ba-8ab0-4330-93ed-3bf5e82a4ed2.png#averageHue=%23f3f2f1&clientId=u35b840e1-8af8-4&from=paste&height=85&id=u453e6be7&originHeight=85&originWidth=1303&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6165&status=done&style=shadow&taskId=u4788f1ec-9cc1-47a3-9a5d-22d93fedbfb&title=&width=1303)
通过测试得知，order by也遵循最左前缀法则。

我们再来看一下未使用覆盖索引会怎样？
```sql
explain select * from workers order by age,sal;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709782521969-56b24557-9c9f-4077-a82c-c929e92a0129.png#averageHue=%23f4f3f3&clientId=u35b840e1-8af8-4&from=paste&height=95&id=u17bd9104&originHeight=95&originWidth=1265&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6021&status=done&style=shadow&taskId=u4f6e9fdb-a00c-4333-8c5e-d97acfe370f&title=&width=1265)
通过测试得知，排序也要尽量使用覆盖索引。

order by 优化原则总结：

1. 排序也要遵循最左前缀法则。
2. 使用覆盖索引。
3. 针对不同的排序规则，创建不同索引。（如果所有字段都是升序，或者所有字段都是降序，则不需要创建新的索引）
4. 如果无法避免filesort，要注意排序缓存的大小，默认缓存大小256KB，可以修改系统变量 sort_buffer_size ：
```sql
show variables like 'sort_buffer_size';
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709782782925-0ec340e2-d15c-4296-86ac-250568c46dc0.png#averageHue=%23dfdedc&clientId=u35b840e1-8af8-4&from=paste&height=60&id=u3e96e4a4&originHeight=60&originWidth=223&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2489&status=done&style=shadow&taskId=uec6668b2-9aa8-4155-a6ec-9659492ecf8&title=&width=223)


## group by优化
创建empx表：
```sql
create table empx as select * from emp;
```
job字段上没有索引，根据job进行分组，查看每个工作岗位有多少人：
```sql
select job,count(*) from empx group by job;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709783194871-ebac7b79-ccdc-455c-8166-2fd36e833d71.png#averageHue=%23efedec&clientId=u35b840e1-8af8-4&from=paste&height=148&id=u8fe3bc16&originHeight=148&originWidth=201&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4412&status=done&style=shadow&taskId=u0ffbae4e-d414-4573-83d7-508901a8853&title=&width=201)
看看是否走索引了：
```sql
explain select job,count(*) from empx group by job;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709783226523-4ad14ecb-039e-4538-8b7c-574b71294dfb.png#averageHue=%23f3f2f1&clientId=u35b840e1-8af8-4&from=paste&height=89&id=u4ee51c14&originHeight=89&originWidth=1248&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5983&status=done&style=shadow&taskId=uf09e69c3-4d14-4012-89fa-5610caa5f15&title=&width=1248)
使用了临时表，效率较低。

给job添加索引：
```sql
create index idx_empx_job on empx(job);
```
再次执行：
```sql
explain select job,count(*) from empx group by job;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709783325987-ccb3c7a5-232d-4d7b-aea2-5065f2c6ce43.png#averageHue=%23f4f2f2&clientId=u35b840e1-8af8-4&from=paste&height=96&id=u18ff7284&originHeight=96&originWidth=1258&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5984&status=done&style=shadow&taskId=u7c785f8b-ab5d-4671-91cf-7bd81a5a98e&title=&width=1258)
效率提升了。

我们再来看看group by是否需要遵守最左前缀法则：给deptno和sal添加复合索引
```sql
create index idx_empx_deptno_sal on empx(deptno, sal);
```
根据部门编号分组，查看每个部门人数：
```sql
explain select deptno,count(*) from empx group by deptno;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709783498550-a5bd4f3e-3167-474e-81d3-54ca8b7ab90e.png#averageHue=%23f2f1f0&clientId=u35b840e1-8af8-4&from=paste&height=85&id=u3d6add83&originHeight=85&originWidth=1279&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5921&status=done&style=shadow&taskId=u29487fbc-dee7-4e98-b993-b15a24a38aa&title=&width=1279)
效率很高，因为deptno是复合索引中最左边的字段。
根据sal分组，查看每个工资有多少人：
```sql
explain select sal, count(*) from empx group by sal;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709783567910-aaa709cf-edd2-4827-bfe5-59bd4d939e20.png#averageHue=%23f2f1f0&clientId=u35b840e1-8af8-4&from=paste&height=86&id=uf812a6fe&originHeight=86&originWidth=1336&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6456&status=done&style=shadow&taskId=u2f89bd10-af35-474f-9310-d9112de2966&title=&width=1336)
使用了临时表，效率较低。
通过测试得知，group by也同样遵循最左前缀法则。

我们再来测试一下，如果将部门编号deptno（复合索引的最左列）添加到where条件中，效率会不会提升：
```sql
explain select sal, count(*) from empx where deptno=10 group by sal;
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709783791088-acd69751-3ef3-4bb4-a86c-80734281920f.png#averageHue=%23f2f1f0&clientId=u35b840e1-8af8-4&from=paste&height=82&id=u9ea99fa9&originHeight=82&originWidth=1270&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6278&status=done&style=shadow&taskId=uac239529-cb8b-4c88-a8a8-bbc3b004efa&title=&width=1270)
效率有提升的，这说明了，group by确实也遵循最左前缀法则。（where中使用了最左列）


## limit优化
数据量特别庞大时，取数据时，越往后效率越低，怎么提升？mysql官方给出的解决方案是：使用覆盖索引+子查询的形式来提升效率。

![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709792419459-85a3ad86-c141-426c-b9de-6dc7469d60ee.png#averageHue=%23151211&clientId=u35b840e1-8af8-4&from=paste&height=634&id=u51e2988a&originHeight=634&originWidth=921&originalType=binary&ratio=1&rotation=0&showTitle=false&size=61566&status=done&style=shadow&taskId=uc68032bd-7849-4c40-bdb3-c234b55b01b&title=&width=921)

怎么解决？使用覆盖索引，加子查询
使用覆盖索引：速度有所提升
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709792480566-96befb8b-95c5-498a-b6ca-fa813ed527c2.png#averageHue=%23100e0e&clientId=u35b840e1-8af8-4&from=paste&height=219&id=ub9c7ece1&originHeight=219&originWidth=723&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10161&status=done&style=shadow&taskId=ue75ff2e1-1f52-455e-ad48-7db2b74f010&title=&width=723)
使用子查询形式取其他列的数据：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709792539686-fc91c8b7-31c3-4d86-acd5-13355ec2af34.png#averageHue=%23121110&clientId=u35b840e1-8af8-4&from=paste&height=202&id=uc374a206&originHeight=202&originWidth=1269&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21977&status=done&style=shadow&taskId=u9ba6a9b3-13b3-44c2-9d69-a2c2292684b&title=&width=1269)
通过测试，这种方式整体效率有所提升。


## 主键优化
主键设计原则：

1. 主键值不要太长，二级索引叶子结点上存储的是主键值，主键值太长，容易导致索引占用空间较大。
2. 尽量使用auto_increment生成主键。尽量不要使用uuid做主键，因为uuid不是顺序插入。
3. 最好不要使用业务主键，因为业务的变化会导致主键值的频繁修改，主键值不建议修改，因为主键值修改，聚集索引一定会重新排序。
5. 在插入数据时，主键值最好是顺序插入，不要乱序插入，因为乱序插入可能会导致B+树叶子结点频繁的进行页分裂与页合并操作，效率较低。
   1. 主键值对应聚集索引，插入主键值如果是乱序的，B+树叶子结点需要不断的重新排序，重排过程中还会频繁涉及到**页分裂和页合并**的操作，效率较低。
   2. B+树上的每个节点都存储在页（page）中。一个页面中存储一个节点。
   3. MySQL的InnoDB存储引擎一个页可以存储16KB的数据。
   4. 如果主键值不是顺序插入的话，会导致频繁的页分裂和页合并。在一个B+树中，页分裂和页合并是树的自动调整机制的一部分。当一个页已经满了，再插入一个新的关键字时就会触发页分裂操作，将页中的关键字分配到两个新的页中，同时调整树的结构。相反，当一个页中的关键字数量下降到一个阈值以下时，就会触发页合并操作，将两个相邻的页合并成一个新的页。如果主键值是随机的、不是顺序插入的，那么页的利用率会降低，页分裂和页合并的次数就会增加。由于页的分裂和合并是比较耗时的操作，频繁的分裂和合并会降低数据库系统的性能。因此，为了优化B+树的性能，可以将主键值设计成顺序插入的，这样可以减少页的分裂和合并的次数，提高B+树的性能。在实际应用中，如果对主键值的顺序性能要求不是特别高，也可以采用一些技术手段来减少页分裂和合并，例如B+树分裂时采用“延迟分裂”技术，或者通过调整页的大小和节点的大小等方式来优化B+树的性能。

![1.jpg](https://cdn.nlark.com/yuque/0/2024/jpeg/21376908/1709779279973-956a0695-45ff-472d-bc49-20db1031cc9e.jpeg#averageHue=%23ece6c8&clientId=u35b840e1-8af8-4&from=paste&height=442&id=u860d200d&originHeight=2000&originWidth=3020&originalType=binary&ratio=1&rotation=0&showTitle=false&size=344186&status=done&style=shadow&taskId=ue57bddc9-90d5-4461-8e1d-a0334ed7b70&title=&width=667)


## insert优化
insert优化原则：

- 批量插入：数据量较大时，不要一条一条插入，可以批量插入，当然，建议一次插入数据不超过1000条
```sql
insert into t_user(id,name,age) values (1,'jack',20),(2,'lucy',30),(3,'timi',22);
```

- mysql默认是自动提交事务，只要执行一条DML语句就自动提交一次，因此，当插入大量数据时，建议手动开启事务和手动提交事务。不建议使用数据库事务自动提交机制。
- 主键值建议采用顺序插入，顺序插入比乱序插入效率高。
- 超大数据量插入可以考虑使用mysql提供的load指令，load指令可以将csv文件中的数据批量导入到数据库表当中，并且效率很高，过程如下：
   - 第一步：登录mysql时指定参数
```sql
mysql --local-infile -uroot -p1234
```

   - 第二步：开启local_infile功能
```sql
set global local_infile = 1;
```

   - 第三步：执行load指令
```sql
use powernode;

create table t_temp(
  id int primary key,
  name varchar(255),
  password varchar(255),
  birth char(10),
  email varchar(255)
);

load data local infile 'E:\\powernode\\05-MySQL高级\\resources\\t_temp-100W.csv' into table t_temp fields terminated by ',' lines terminated by '\n';
```

文件中的数据如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709775730313-08bbfff2-f309-48c1-8a0b-8f35199ea26b.png#averageHue=%23e4e0db&clientId=u487a63fb-d269-4&from=paste&height=124&id=u682f5f56&originHeight=124&originWidth=721&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15197&status=done&style=shadow&taskId=ube19aa54-7d7f-4be2-993b-142cfdc94b5&title=&width=721)

导入表中之后，数据如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709775744254-1cec3fef-c141-47d2-9b63-fecfda8dc360.png#averageHue=%23171513&clientId=u487a63fb-d269-4&from=paste&height=211&id=ud57abe6c&originHeight=211&originWidth=824&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26037&status=done&style=shadow&taskId=u800e80b7-21a0-4ae8-89a4-a843171b036&title=&width=824)



## count(*)优化
分组函数count的使用方式：

- count(主键)
   - 原理：将每个主键值取出，累加
- count(常量值)
   - 原理：获取到每个常量值，累加
- count(字段)
   - 原理：取出字段的每个值，判断是否为NULL，不为NULL则累加。
- count(*)
   - 原理：不用取值，底层mysql做了优化，直接统计总行数，效率最高。

结论：如果你要统计一张表中数据的总行数，建议使用 count(*)

注意：

- 对于InnoDB存储引擎来说，count计数的实现原理就是将表中每一条记录取出，然后累加。如果你想真正提高效率，可以自己使用额外的其他程序来实现，例如每向表中插入一条记录时，在redis数据库中维护一个总行数，这样获取总行数的时候，直接从redis中获取即可，这样效率是最高的。
- 对于MyISAM存储引擎来说，当一个select语句没有where条件时，获取总行数效率是极高的，不需要统计，因为MyISAM存储引擎维护了一个单独的总行数。


## update优化
当存储引擎是InnoDB时，表的行级锁是针对索引添加的锁，如果索引失效了，或者不是索引列时，会提升为表级锁。
什么是行级锁？A事务和B事务，开启A事务后，通过A事务修改表中某条记录，修改后，在A事务未提交的前提下，B事务去修改同一条记录时，无法继续，直到A事务提交，B事务才可以继续。

有一张表：t_fruit
```sql
create table t_fruit(
  id int primary key auto_increment,
  name varchar(255)
);

insert into t_fruit values(null, '苹果');
insert into t_fruit values(null, '香蕉');
insert into t_fruit values(null, '橘子');
```

开启A事务和B事务，演示行级锁：
事务A没有结束之前，事务B卡住：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709801809111-e793cdbb-8831-4a09-8ed2-c59a06c059b7.png#averageHue=%23343332&clientId=u35b840e1-8af8-4&from=paste&height=262&id=u334dda64&originHeight=262&originWidth=1317&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37438&status=done&style=shadow&taskId=u61a2bedb-5248-4796-9afe-78c03eabfa2&title=&width=1317)
事务A结束之后，事务B继续执行：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709801868506-53ecc7e3-4b12-4f17-9842-e4e073e48dc8.png#averageHue=%232c2b2a&clientId=u35b840e1-8af8-4&from=paste&height=333&id=u6e51fb46&originHeight=333&originWidth=1283&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50480&status=done&style=shadow&taskId=uc9936036-1805-447c-85cd-e6ae35f8ff9&title=&width=1283)
当然，如果更新的不是同一行数据，事务A和事务B可以并发：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709802096461-f9ab6622-48f9-4e19-8773-f31ef8728303.png#averageHue=%232a2928&clientId=u35b840e1-8af8-4&from=paste&height=328&id=u0ba90557&originHeight=328&originWidth=1279&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49283&status=done&style=shadow&taskId=u7c4d7d00-1f15-4fca-866e-c68b3b49999&title=&width=1279)

行级锁是对索引列加锁，以上更新语句的where条件是id，id是主键，当然有索引，所以使用了行级锁，如果索引失效，或者字段上没有索引，则会升级为表级锁：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/21376908/1709802244610-ba45b78f-f8b7-445a-af7d-f5d8ad44441f.png#averageHue=%232f2e2d&clientId=u35b840e1-8af8-4&from=paste&height=285&id=u0540d10d&originHeight=285&originWidth=1388&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35657&status=done&style=shadow&taskId=u0eb965eb-c2c4-43f1-9bd1-602b94111e5&title=&width=1388)

因此，为了更新的效率，建议update语句中where条件中的字段是添加索引的。

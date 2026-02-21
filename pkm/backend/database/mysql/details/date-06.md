
### date_format日期格式化函数

将日期转换成具有某种格式的日期字符串，通常用在查询操作当中。（date类型转换成char类型）

语法格式：`date_format(日期, '日期格式')`

该函数有两个参数：

- 第一个参数：日期。这个参数就是即将要被格式化的日期。类型是date类型。
- 第二个参数：指定要格式化的格式字符串。
	- %Y：四位年份
	- %y：两位年份
	- %m：月份（1..12）
	- %d：日（1..30）
	- %H：小时（0..23）
	- %i：分（0..59）
	- %s：秒（0..59）

例如：获取当前系统时间，让其以这个格式展示：2000-10-11 20:15:30
```sql
mysql> select date_format(now(), '%Y-%m-%d %H:%i:%s');
+-----------------------------------------+
| date_format(now(), '%Y-%m-%d %H:%i:%s') |
+-----------------------------------------+
| 2026-02-21 16:04:03                     |
+-----------------------------------------+
1 row in set (0.000 sec)
```

注意：在mysql当中，默认的日期格式就是：`%Y-%m-%d %H:%i:%s`。

### str_to_date函数

该函数的作用是将char类型的日期字符串转换成日期类型date，通常使用在插入和修改操作当中。（char类型转换成date类型）

假设有一个学生表t_student，学生有一个生日的字段，类型是date类型：

```sql
drop table if exists t_student;
create table t_student(
name varchar(255),
birth date
);
desc t_student;
```

我们要给这个表插入一条数据：姓名zhangsan，生日85年10月1日，执行以下insert语句：

```sql
mysql> insert into t_student(name,birth) values('zhangsan','10/01/1985');
ERROR 1292 (22007): Incorrect date value: '10/01/1985' for column 'birth' at row 1
```

错误原因：日期值不正确。意思是：birth字段需要一个日期，你给的这个字符串'10/01/1985'我识别不了。这种情况下，我们就可以使用str_to_date函数进行类型转换

```sql
mysql> insert into t_student(name,birth)
    -> values('zhangsan',str_to_date('10/01/1985','%m/%d/%Y'));
Query OK, 1 row affected (0.003 sec)
```

```sql
mysql> select * from t_student;
+----------+------------+
| name     | birth      |
+----------+------------+
| zhangsan | 1985-10-01 |
+----------+------------+
1 row in set (0.001 sec)
```

当然，如果你提供的日期字符串格式能够被mysql解析，str_to_date函数是可以省略的，底层会自动调用该函数进行类型转换：

```sql
mysql> insert into t_student(name,birth) values('zhangsan1','1985-10-01');
Query OK, 1 row affected (0.002 sec)

mysql> insert into t_student(name,birth) values('zhangsan2','85-10-01');
Query OK, 1 row affected (0.002 sec)

mysql> insert into t_student(name,birth) values('zhangsan3','85/10/01');
Query OK, 1 row affected, 1 warning (0.001 sec)

mysql> insert into t_student(nam,birth) values('zhangsan4','1985/10/01');
Query OK, 1 row affected, 1 warning (0.002 sec)
```

如果日期格式符合以上的几种格式，mysql都会自动进行类型转换的。

  
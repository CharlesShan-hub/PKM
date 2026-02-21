
### 模糊查询like

模糊查询又被称为模糊匹配，在实际开发中使用较多，比如：查询公司中所有姓张的，查询岗位中带有经理两个字的职位等等，这些都需要使用模糊查询。

模糊查询的语法格式如下：

```sql

select .. from .. where 字段 like '通配符表达式';

```

在模糊查询中，通配符主要包括两个：一个是`%`，一个是下划线`_`。其中`%`代表任意多个字符。下划线`_`代表任意一个字符。

案例1：查询员工名字以'S'开始的员工姓名

```sql
mysql> select ename from emp where ename like 'S%';
+-------+
| ename |
+-------+
| SMITH |
| SCOTT |
+-------+
2 rows in set (0.002 sec)
```

案例2：查询员工名字以'T'结尾的员工姓名

```sql
mysql> select ename from emp where ename like '%t';
+-------+
| ename |
+-------+
| SCOTT |
+-------+
1 row in set (0.001 sec)
```

案例3：查询员工名字中含有'O'的员工姓名

```sql
mysql> select ename from emp where ename like '%O%';
+-------+
| ename |
+-------+
| JONES |
| SCOTT |
| FORD  |
+-------+
3 rows in set (0.001 sec)
```

案例4：查询员工名字中第二个字母是'A'的员工姓名

```sql
mysql> select ename from emp where ename like '_A%';
+--------+
| ename  |
+--------+
| WARD   |
| MARTIN |
| JAMES  |
+--------+
3 rows in set (0.001 sec)
```

案例5：查询学员名字中含有下划线的。

执行以下SQL语句，先准备测试数据：

```sql
drop table if exists student;
create table student(
id int,
name varchar(255)
);
insert into student(id,name) values(1, 'susan');
insert into student(id,name) values(2, 'lucy');
insert into student(id,name) values(3, 'jack_son');
select * from student;
```

```bash
+------+----------+
| id   | name     |
+------+----------+
|    1 | susan    |
|    2 | lucy     |
|    3 | jack_son |
+------+----------+
3 rows in set (0.001 sec)
```

查询学员名字中含有下划线的，执行以下SQL试试：

```sql
mysql> select name from student where name like '%_%';
+----------+
| name     |
+----------+
| susan    |
| lucy     |
| jack_son |
+----------+
3 rows in set (0.001 sec)
```

显然这个查询结果不是我们想要的，以上SQL之所以将所有数据全部显示了，因为下划线代表任意单个字符，如果你想让这个下划线变成一个普通的下划线字符，就要使用转义字符了，在mysql当中转义字符是“\”，这个和java语言中的转义字符是一样的：

```sql
mysql> select name from student where name like '%\_%';
+----------+
| name     |
+----------+
| jack_son |
+----------+
1 row in set (0.001 sec)
```


  
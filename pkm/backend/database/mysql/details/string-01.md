### 转大写upper和ucase

```sql
-- 查询所有员工名字，以大写形式展现
select upper(ename) as ename from emp;
```

```bash
+--------+
| ename  |
+--------+
| SMITH  |
| ALLEN  |
| WARD   |
| JONES  |
| MARTIN |
| BLAKE  |
| CLARK  |
| SCOTT  |
| KING   |
| TURNER |
| ADAMS  |
| JAMES  |
| FORD   |
| MILLER |
+--------+
14 rows in set (0.004 sec)
```

还有一个和upper函数功能相同的函数ucase，也可以转大写，了解一下即可：

```sql
-- 查询所有员工姓名，以大写形式展现
select ucase(ename) as ename from emp;
```

```shell
+--------+
| ename  |
+--------+
| SMITH  |
| ALLEN  |
| WARD   |
| JONES  |
| MARTIN |
| BLAKE  |
| CLARK  |
| SCOTT  |
| KING   |
| TURNER |
| ADAMS  |
| JAMES  |
| FORD   |
| MILLER |
+--------+
14 rows in set (0.001 sec)
```

```sql
-- 查询员工smith的岗位、薪资（假如你不知道数据库表中的人名是大写、小写还是大小写混合）
select ename, job, sal from emp where upper(ename) = 'SMITH';
```

```shell
+-------+-------+--------+
| ename | job   | sal    |
+-------+-------+--------+
| SMITH | CLERK | 800.00 |
+-------+-------+--------+
1 row in set (0.001 sec)
```


### 转小写lower和lcase

**很简单，不再赘述，直接上代码：**

```sql
-- # 查询员工姓名，以小写形式展现
select lower(ename) as ename from emp;
select lcase(ename) as ename from emp;
```

```shell
+--------+
| ename  |
+--------+
| smith  |
| allen  |
| ward   |
| jones  |
| martin |
| blake  |
| clark  |
| scott  |
| king   |
| turner |
| adams  |
| james  |
| ford   |
| miller |
+--------+
14 rows in set (0.001 sec)
```

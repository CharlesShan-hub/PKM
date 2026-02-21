
### in、not in

#### in

* 语法：`in`后面有一个小括号，小括号当中有多个值，值和值之间采用逗号隔开
* `in`和`=`+`or`查询效果是相同的（但是效率不同）
	* `job in('MANAGER','SALESMAN','CLERK')`等同于 `job = 'MANAGER' or job = 'SALESMAN' or job = 'CLERK'`
	* `sal in(1600, 3000, 5000)` 等同于 `sal = 1600 or sal = 3000 or sal = 5000`
* `sal in(1500, 5000)`，需要注意的是：这个并不是说薪资在1500到5000之间，in不代表区间，表示sal是1500的和sal是5000的

案例1：找出工作岗位是MANAGER和SALESMAN的员工姓名、薪资、工作岗位

第一种：使用or

```sql
mysql> select ename,sal,job from emp
    -> where
    -> job = 'MANAGER' or job = 'SALESMAN';
+--------+---------+----------+
| ename  | sal     | job      |
+--------+---------+----------+
| ALLEN  | 1600.00 | SALESMAN |
| WARD   | 1250.00 | SALESMAN |
| JONES  | 2975.00 | MANAGER  |
| MARTIN | 1250.00 | SALESMAN |
| BLAKE  | 2850.00 | MANAGER  |
| CLARK  | 2450.00 | MANAGER  |
| TURNER | 1500.00 | SALESMAN |
+--------+---------+----------+
7 rows in set (0.001 sec)
```

第二种：使用in

```sql
mysql> select ename,sal,job from emp where job in ('MANAGER','SALESMAN');
+--------+---------+----------+
| ename  | sal     | job      |
+--------+---------+----------+
| ALLEN  | 1600.00 | SALESMAN |
| WARD   | 1250.00 | SALESMAN |
| JONES  | 2975.00 | MANAGER  |
| MARTIN | 1250.00 | SALESMAN |
| BLAKE  | 2850.00 | MANAGER  |
| CLARK  | 2450.00 | MANAGER  |
| TURNER | 1500.00 | SALESMAN |
+--------+---------+----------+
7 rows in set (0.000 sec)
```

#### not in

* 同理，`not in`等价于`<>`和`and`组合
	* `job not in('MANAGER','SALESMAN')` 等同于 `job <> 'MANAGER' and job <> 'SALESMAN'`
	* `sal not in(1600, 5000)` 等同于 `sal <> 1600 and sal <> 5000`

案例：找出工作岗位不是MANAGER和SALESMAN的员工姓名、工作岗位

第一种：使用and

```sql
mysql> select ename,job from emp where
    -> job <> 'MANAGER' and job <> 'SALESMAN';
+--------+-----------+
| ename  | job       |
+--------+-----------+
| SMITH  | CLERK     |
| SCOTT  | ANALYST   |
| KING   | PRESIDENT |
| ADAMS  | CLERK     |
| JAMES  | CLERK     |
| FORD   | ANALYST   |
| MILLER | CLERK     |
+--------+-----------+
7 rows in set (0.001 sec)
```

第二种：使用not in

```sql
mysql> select ename,job from emp where
    -> job not in('MANAGER', 'SALESMAN');
+--------+-----------+
| ename  | job       |
+--------+-----------+
| SMITH  | CLERK     |
| SCOTT  | ANALYST   |
| KING   | PRESIDENT |
| ADAMS  | CLERK     |
| JAMES  | CLERK     |
| FORD   | ANALYST   |
| MILLER | CLERK     |
+--------+-----------+
7 rows in set (0.001 sec)
```

#### in、not in 与 NULL

先来看一下emp表中的数据

```sql
mysql> select ename, comm from emp;
+--------+---------+
| ename  | comm    |
+--------+---------+
| SMITH  |    NULL |
| ALLEN  |  300.00 |
| WARD   |  500.00 |
| JONES  |    NULL |
| MARTIN | 1400.00 |
| BLAKE  |    NULL |
| CLARK  |    NULL |
| SCOTT  |    NULL |
| KING   |    NULL |
| TURNER |    0.00 |
| ADAMS  |    NULL |
| JAMES  |    NULL |
| FORD   |    NULL |
| MILLER |    NULL |
+--------+---------+
14 rows in set (0.001 sec)
```

通过表中数据观察到，有4个员工的津贴不为NULL，剩下10个员工的津贴都是NULL。写这样一条SQL语句：

```sql
mysql> select ename,comm from emp where comm in(NULL, 300);
+-------+--------+
| ename | comm   |
+-------+--------+
| ALLEN | 300.00 |
+-------+--------+
1 row in set (0.001 sec)
```

为什么以上执行结果只有一条记录呢？分析一下：首先你要知道in的执行原理实际上是采用=和or的方式，也就是说，以上SQL语句实际上是：

```sql
select * from emp where comm = NULL or comm = 300;
```

其中NULL不能用等号=进行判断，所以comm = NULL结果是false，然而中间使用的是or，所以comm = NULL被忽略了。所以查询结果就以上一条数据。

通过以上的测试得知：**in是自动忽略NULL的**。

再写这样一条SQL语句：

```sql
mysql> select * from emp where comm not in(NULL, 300);
Empty set (0.001 sec)
```

以上的执行结果奇怪了，为什么没有查到任何数据呢？我们分析一下：首先你要知道not in的执行原理实际上是采用<>和and的方式，也就是说，以上SQL语句实际上是：

```sql
select * from emp where comm <> NULL and comm <> 300;
```

其中NULL的判断不能使用<>，所以comm <> NULL结果是false，由于后面是and，and表示并且，comm <> NULL已经是false了，所以and右边的就没必要运算了，comm <> NULL and comm <> 300的整体运算结果就是false。所以查询不到任何数据。

通过以上测试得知，**not in是不会自动忽略NULL的**，所以在使用not in的时候一定要提前过滤掉NULL。

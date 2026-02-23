# 子查询

> 本章案例的数据初始化：[powerpoint-init-data](../details/powerpoint-init-data.md)

---
## 什么是子查询

1. select语句中嵌套select语句就叫做子查询。
2. select语句可以嵌套在哪里？where后面、from后面、select后面都是可以的。
	```sql
	select ..(select)..
	from ..(select)..
	where ..(select)..
	```

---
## where后面使用子查询

案例：找出高于平均薪资的员工姓名和薪资。

错误的示范：

```sql
select ename,sal from emp where sal > avg(sal);
```

错误原因：where后面不能直接使用分组函数。

可以使用子查询：

```sql
select ename,sal from emp where sal > (select avg(sal) from emp);
```

---
## from后面使用子查询

小窍门：**from后面的子查询可以看做一张临时表**。

案例：找出每个部门的平均工资的等级。

第一步：先找出每个部门平均工资。

```sql
select deptno, avg(sal) avgsal from emp group by deptno;
```

```shell
+--------+-------------+
| deptno | avgsal      |
+--------+-------------+
|     20 | 2175.000000 |
|     30 | 1566.666667 |
|     10 | 2916.666667 |
+--------+-------------+
3 rows in set (0.003 sec)
```

第二步：将以上查询结果当做临时表t，t表和salgrade表进行连接查询。条件：`t.avgsal between s.losal and s.hisal`

```sql
select t.*,s.grade from (select deptno, avg(sal) avgsal from emp group by deptno) t join salgrade s on t.avgsal between s.losal and s.hisal;
```

```shell
+--------+-------------+-------+
| deptno | avgsal      | grade |
+--------+-------------+-------+
|     20 | 2175.000000 |     4 |
|     30 | 1566.666667 |     3 |
|     10 | 2916.666667 |     4 |
+--------+-------------+-------+
3 rows in set (0.002 sec)
```

---
## select后面使用子查询

```sql
select e.ename,(select d.dname from dept d where e.deptno = d.deptno) as dname from emp e;
```

```sql
+--------+------------+
| ename  | dname      |
+--------+------------+
| SMITH  | RESEARCH   |
| ALLEN  | SALES      |
| WARD   | SALES      |
| JONES  | RESEARCH   |
| MARTIN | SALES      |
| BLAKE  | SALES      |
| CLARK  | ACCOUNTING |
| SCOTT  | RESEARCH   |
| KING   | ACCOUNTING |
| TURNER | SALES      |
| ADAMS  | RESEARCH   |
| JAMES  | SALES      |
| FORD   | RESEARCH   |
| MILLER | ACCOUNTING |
+--------+------------+
14 rows in set (0.002 sec)
```

---
## exists、not exists  

在 MySQL 数据库中，EXISTS（存在）用于检查子查询的查询结果行数是否大于0。如果子查询的查询结果行数大于0，则 EXISTS 条件为真。（即存在查询结果则是true。）

主要应用场景：
- EXISTS 可以与 SELECT、UPDATE、DELETE 一起使用，用于检查另一个查询是否返回任何行；
- EXISTS 可以用于验证条件子句中的表达式是否存在；
- EXISTS 常用于子查询条件过滤，例如查询有订单的用户等。

```sql
drop table if exists t_customer;
drop table if exists t_order;

create table t_customer(
	customer_id int,
	customer_name varchar(32)
);

create table t_order(
	order_id int,
	order_price decimal(5,1),
	customer_id int
);

insert into t_customer(customer_id,customer_name) values(1,'zhangsan');
insert into t_customer(customer_id,customer_name) values(2,'lisi');
insert into t_customer(customer_id,customer_name) values(3,'wangwu');
  
insert into t_order(order_id, order_price, customer_id) values(10, 1000.0, 1);
insert into t_order(order_id, order_price, customer_id) values(20, 2000.0, 1);
insert into t_order(order_id, order_price, customer_id) values(30, 3000.0, 2);
insert into t_order(order_id, order_price, customer_id) values(40, 4000.0, 2);

commit;
select * from t_customer;
select * from t_order;
```

现在我们来看一个简单的案例，假设我们要查询先前有过订单的顾客，而订单信息保存在 t_order 表中，顾客信息保存在 t_customer 表中。我们可以使用以下 sql 语句：

```sql
select * from t_customer c where exists(select * from t_order o where o.customer_id=c.customer_id);
```

```sql
mysql> select * from t_customer c where exists(select * from t_order o where o.customer_id=c.customer_id);
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
|           1 | zhangsan      |
|           2 | lisi          |
+-------------+---------------+
2 rows in set (0.003 sec)
  
mysql> select * from t_customer;
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
|           1 | zhangsan      |
|           2 | lisi          |
|           3 | wangwu        |
+-------------+---------------+
3 rows in set (0.000 sec)

mysql> select * from t_order;
  
+----------+-------------+-------------+
| order_id | order_price | customer_id |
+----------+-------------+-------------+
|       10 |      1000.0 |           1 |
|       20 |      2000.0 |           1 |
|       30 |      3000.0 |           2 |
|       40 |      4000.0 |           2 |
+----------+-------------+-------------+
4 rows in set (0.000 sec)
```

在这个查询语句中，子查询用于检查是否有订单与每个客户相关联。如果子查询返回至少一行，则表示该顾客已经下过订单，并返回此客户的所有信息，否则该顾客将不被包含在结果中。

以下是这个查询语句的执行过程：

1. 首先查询表 t_customer 中的所有顾客信息（以下简称为顾客表）；
2. 对于顾客表中的每一行，都执行一次子查询，子查询查询该顾客有没有订单，如果有，则在结果集中保留该顾客信息；如果没有，则将该顾客排除；
3. 最终返回有订单顾客的所有信息。

除了 EXISTS，也可以使用 NOT EXISTS 条件从 SELECT、UPDATE、DELETE 语句中获取子查询的返回结果。NOT EXISTS 用于检查一个子查询是否返回任何行，如果没有行返回，那么 NOT EXISTS 将返回 true。

例如，我们想要查找所有没有下过订单的顾客，可以使用以下 sql 语句：

```sql
select * from t_customer c where not exists(select * from t_order o where o.customer_id=c.customer_id);
```

在这个查询语句中，如果没有任何与顾客相关联的订单，则 NOT EXISTS 子查询将返回一个空结果集，这时候 WHERE 条件为 true，并将返回所有顾客信息。如果顾客有订单，则 NOT EXISTS 子查询的结果集将不为空，WHERE 条件为 false，则不会返回该顾客的信息。

总之，无论是 EXISTS 还是 NOT EXISTS，都是非常有用的 SQL 工具。可以通过它们来结合子查询来动态过滤查询结果，使 SQL 查询变得更加灵活和高效。

---
## in和exists区别

IN 和 EXISTS 都是用于关系型数据库查询的操作符。不同之处在于（面试题）：

1. **IN 操作符**是根据指定列表中的**值**来判断是否满足条件，而 **EXISTS 操作符**则是根据子查询的结果**是否有返回记录集**来判断。
2. **EXISTS 操作符通常比 IN 操作符更快**，尤其是在子查询返回记录数很大的情况下。**因为 EXISTS 只需要判断是否存在符合条件的记录，而 IN 操作符需要比对整个列表**，因此执行效率相对较低。
3. IN 操作符可同时匹配**多个值**，而 EXISTS **只能匹配一组条件**。

下面是一个简单的示例，用于演示 IN 和 EXISTS 之间的区别。假设我们有两个表 orders 和 products，orders 表中记录了订单信息，products 表中记录了商品信息。现在我们想查询所有“手机”和“平板电脑”这两种商品中，至少有一笔订单销售了 $1000 以上的商品：

使用 IN 操作符：

```sql
SELECT *
FROM products
WHERE product_name IN ('手机', '平板电脑')
AND product_id IN (
SELECT product_id
FROM orders
WHERE order_amount > 1000
);
```

使用 EXISTS 操作符：

```sql
SELECT *
FROM products
WHERE product_name IN ('手机', '平板电脑')
AND EXISTS (
SELECT *
FROM orders
WHERE orders.product_id = products.product_id
AND order_amount > 1000
);
```

总之，IN 和 EXISTS 都是用于条件过滤的操作符，但其实现方式和性能特点都不同，需要根据具体情况进行选择和使用。

---
## union&union all

不管是union还是union all都可以将两个查询结果集进行合并。

**union**会对合并之后的查询结果集进行**去重操作**。

union all是直接将查询结果集合并，不进行去重操作。（union all和union都可以完成的话，**优先选择union all**，union all因为不需要去重，所以效率高一些。）

```sql
-- 只查询'salesman','clerk'的员工
mysql> select e.ename, e.sal from emp e where e.job in ('salesman','clerk');
+--------+---------+
| ename  | sal     |
+--------+---------+
| SMITH  |  800.00 |
| ALLEN  | 1600.00 |
| WARD   | 1250.00 |
| MARTIN | 1250.00 |
| TURNER | 1500.00 |
| ADAMS  | 1100.00 |
| JAMES  |  950.00 |
| MILLER | 1300.00 |
+--------+---------+
8 rows in set (0.001 sec)

-- 只查询'manager','clerk'的员工
mysql> select e.ename, e.sal from emp e where e.job in ('manager','clerk');
+--------+---------+
| ename  | sal     |
+--------+---------+
| SMITH  |  800.00 |
| JONES  | 2975.00 |
| BLAKE  | 2850.00 |
| CLARK  | 2450.00 |
| ADAMS  | 1100.00 |
| JAMES  |  950.00 |
| MILLER | 1300.00 |
+--------+---------+
7 rows in set (0.000 sec)

-- 使用union对两个结果合并（会自动去重）
mysql> select e.ename, e.sal from emp e where e.job in ('salesman','clerk')
    -> union
    -> select e.ename, e.sal from emp e where e.job in ('manager','clerk');
+--------+---------+
| ename  | sal     |
+--------+---------+
| SMITH  |  800.00 |
| ALLEN  | 1600.00 |
| WARD   | 1250.00 |
| MARTIN | 1250.00 |
| TURNER | 1500.00 |
| ADAMS  | 1100.00 |
| JAMES  |  950.00 |
| MILLER | 1300.00 |
| JONES  | 2975.00 |
| BLAKE  | 2850.00 |
| CLARK  | 2450.00 |
+--------+---------+
11 rows in set (0.004 sec)

-- 使用union all对两个结果合并（不会去重）
mysql> select e.ename, e.sal from emp e where e.job in ('salesman','clerk')
    -> union all
    -> select e.ename, e.sal from emp e where e.job in ('manager','clerk');
+--------+---------+
| ename  | sal     |
+--------+---------+
| SMITH  |  800.00 |
| ALLEN  | 1600.00 |
| WARD   | 1250.00 |
| MARTIN | 1250.00 |
| TURNER | 1500.00 |
| ADAMS  | 1100.00 |
| JAMES  |  950.00 |
| MILLER | 1300.00 |
| SMITH  |  800.00 |
| JONES  | 2975.00 |
| BLAKE  | 2850.00 |
| CLARK  | 2450.00 |
| ADAMS  | 1100.00 |
| JAMES  |  950.00 |
| MILLER | 1300.00 |
+--------+---------+
15 rows in set (0.001 sec)
```

以上案例采用or也可以完成，那or和union all有什么区别？：**考虑走索引优化之类的选择union all，其它选择or**。

两个结果集合并时，列数量要相同：
```sql
mysql> select e.ename from emp e
    -> union
    -> select e.ename, e.sal from emp e;
ERROR 1222 (2100): The used SELECT statements have a different number of columns
```

---
## limit

1. limit作用：查询第几条到第几条的记录。通常是因为表中数据量太大，需要分页显示。
2. limit语法格式：`limit 开始下标, 长度`
3. 案例：查询员工表前5条记录
	```sql
	select ename,sal from emp limit 0, 5;
	```
	如果下标是从0开始，可以简写为：
	```sql
	select ename,sal from emp limit 5;
	```

4. 查询工资排名在前5名的员工（limit是在order by执行之后才会执行的
	```sql
	select ename,sal from emp order by sal desc limit 5;
	```

5. 通用的分页sql

假设每页显示3条记录：pageSize = 3
第1页：limit 0, 3
第2页：limit 3, 3
第3页：limit 6, 3
第pageNo页：`limit (pageNo - 1)*pageSize, pageSize`
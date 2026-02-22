# 连接查询

---
## 简介
### 什么是连接查询

1. 从一张表中查询数据称为单表查询。
2. 从两张或更多张表中联合查询数据称为多表查询，又叫做连接查询。
3. 什么时候需要使用连接查询？比如这样的需求：员工表中有员工姓名，部门表中有部门名字，要求查询每个员工所在的部门名字，这个时候就需要连接查询。

### 连接查询的分类

1. 根据语法出现的年代进行分类：
	1. SQL92（这种语法很少用，可以不用学。）
	2. SQL99（我们主要学习这种语法。）
2. 根据连接方式的不同进行分类：
	1. 内连接
		1. 等值连接
		2. 非等值连接
		3. 自连接
	2. 外连接
		1. 左外连接（左连接）
		2. 右外连接（右连接）
	3. 全连接
  
### 笛卡尔积现象

  
1. 🌟什么是笛卡尔积现象：当两张表进行连接查询时，如果没有任何条件进行过滤，**最终的查询结果条数是两张表条数的乘积**。[cartesian-product-example](../details/cartesian-product-example.md)
2. 为了避免笛卡尔积现象的发生，需要添加条件进行筛选过滤。
3. 需要注意：添加条件之后，虽然避免了笛卡尔积现象，但是匹配的次数没有减少。
4. 为了SQL语句的可读性，为了执行效率，建议给表起别名。
### 内连接

  

#### 什么叫内连接

![内连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398804476-afbffad7-7d5a-4318-9e86-a3f8092dfcc8.png#averageHue=%23f7f5f5&clientId=u1be67ea7-0240-4&from=paste&height=233&id=u4f6abf7d&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29826&status=done&style=shadow&taskId=u51112874-93e5-4ef2-8366-f78cc265d04&title=&width=300)

满足条件的记录才会出现在结果集中。

#### 内连接之等值连接

连接时，条件为等量关系。

案例：查询每个员工所在的部门名称，要求显示员工名、部门名。

```sql

select

e.ename,d.dname

from

emp e

inner join

dept d

on

e.deptno = d.deptno;

```

注意：inner可以省略。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401675659-04e46e96-9f00-4210-8beb-e8148807ae10.png#averageHue=%231a1613&clientId=u1be67ea7-0240-4&from=paste&height=380&id=u91e060d7&originHeight=380&originWidth=258&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15942&status=done&style=shadow&taskId=u2319a8db-57a3-4bcb-a42b-b58c46e0381&title=&width=258)

  

#### 内连接之非等值连接

连接时，条件是非等量关系。

案例：查询每个员工的工资等级，要求显示员工名、工资、工资等级。

```sql

select

e.ename,e.sal,s.grade

from

emp e

join

salgrade s

on

e.sal between s.losal and s.hisal;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401628377-11f115a0-b961-4e10-b411-97ea04a89035.png#averageHue=%23191613&clientId=u1be67ea7-0240-4&from=paste&height=380&id=u9ef14890&originHeight=380&originWidth=279&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17957&status=done&style=shadow&taskId=u97872f0c-74c1-40ef-b3bb-607697cbe62&title=&width=279)

  

#### 内连接之自连接

连接时，一张表看做两张表，自己和自己进行连接。

案例：找出每个员工的直属领导，要求显示员工名、领导名。

```sql

select

e.ename 员工名, l.ename 领导名

from

emp e

join

emp l

on

e.mgr = l.empno;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677402107820-a3fc38cc-4e13-4a39-8bb4-f1d9de713cd9.png#averageHue=%23161311&clientId=u1be67ea7-0240-4&from=paste&height=363&id=ub784a9c1&originHeight=363&originWidth=256&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15854&status=done&style=shadow&taskId=u67543946-a969-42f9-a55b-91571731d16&title=&width=256)

思路：

将emp表当做员工表 e

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401951879-b0967e07-82f4-41e3-861e-d61e7d679e71.png#averageHue=%23141210&clientId=u1be67ea7-0240-4&from=paste&height=409&id=u4a5d8630&originHeight=409&originWidth=409&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28580&status=done&style=shadow&taskId=ua9050736-6b86-415c-9f4d-e4e8d72c0b5&title=&width=409)

将emp表当做领导表 l

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401973338-4bc03ba9-815d-4fca-90fb-de34e5848da3.png#averageHue=%2312100f&clientId=u1be67ea7-0240-4&from=paste&height=409&id=uffcf8f58&originHeight=409&originWidth=374&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19851&status=done&style=shadow&taskId=uad8210e5-8156-449c-bc2f-25f2614109b&title=&width=374)

可以发现连接条件是：e.mgr = l.empno（员工的领导编号=领导的员工编号）

注意：KING这个员工没有查询出来。如果想将KING也查询出来，需要使用外连接。

  

### 外连接

  

#### 什么叫外连接

内连接是满足条件的记录查询出来。也就是两张表的交集。

外连接是除了满足条件的记录查询出来，再将其中一张表的记录全部查询出来，**另一张表如果没有与之匹配的记录，自动模拟出NULL与其匹配**。

左外连接：

![左连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398828684-41b0bde2-1689-47a4-ae7b-3c5c4fb82ce6.png#averageHue=%23f5e6e4&clientId=u1be67ea7-0240-4&from=paste&height=233&id=ue0f4c04f&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42064&status=done&style=shadow&taskId=u3697d149-d9f5-4090-8773-ffb0962ff90&title=&width=300)

右外连接：

![右连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398837026-688ff40f-d74b-4da6-a2e4-9573f5ba1580.png#averageHue=%23f4e6e3&clientId=u1be67ea7-0240-4&from=paste&height=233&id=ua18b1d44&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43272&status=done&style=shadow&taskId=u4bb1c6ab-4c51-4fe0-938b-a7950969180&title=&width=300)

  

#### 外连接之左外连接（左连接）

案例：查询所有部门信息，并且找出每个部门下的员工。

```sql

select

d.*,e.ename

from

dept d

left outer join

emp e

on

d.deptno = e.deptno;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677402955987-bdcd956a-8dd4-481b-97de-c785b200e902.png#averageHue=%23171411&clientId=u1be67ea7-0240-4&from=paste&height=408&id=ud8f95a62&originHeight=408&originWidth=470&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36154&status=done&style=shadow&taskId=u3263d663-860e-41a9-b973-50a3be9baa0&title=&width=470)

注意：outer可以省略。

任何一个左连接都可以写作右连接。

  

#### 外连接之右外连接（右连接）

还是上面的案例，可以写作右连接。

```sql

select

d.*,e.ename

from

emp e

right outer join

dept d

on

d.deptno = e.deptno;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677403445932-325502d5-b568-46a5-8f7a-d91030f3cac3.png#averageHue=%23191411&clientId=u1be67ea7-0240-4&from=paste&height=412&id=ue32d3266&originHeight=412&originWidth=454&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36142&status=done&style=shadow&taskId=u28ef1b62-f835-472a-b916-1ee2eb5299b&title=&width=454)

案例：找出所有员工的上级领导，要求显示员工名和领导名。

```sql

select

e.ename 员工名,l.ename 领导名

from

emp e

left join

emp l

on

e.mgr = l.empno;

```

```sql

select

e.ename 员工名,l.ename 领导名

from

emp l

right join

emp e

on

e.mgr = l.empno;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677403569294-c9688076-61e2-4e33-bb40-06d4307c6b43.png#averageHue=%23171210&clientId=u1be67ea7-0240-4&from=paste&height=386&id=ud80e0755&originHeight=386&originWidth=273&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16908&status=done&style=shadow&taskId=uded0f105-8d51-486b-97fb-acb24822774&title=&width=273)

  

  

### 全连接

什么是全连接？

MySQL不支持full join。oracle数据库支持。

![全连接.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398846702-4a3f3e0f-16bb-4e00-8015-490dc44d114b.png#averageHue=%23f2d7d2&clientId=u1be67ea7-0240-4&from=paste&height=233&id=u050103a2&originHeight=233&originWidth=300&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51399&status=done&style=shadow&taskId=ued746d97-47c2-46a3-83cd-097182ea146&title=&width=300)

两张表数据全部查询出来，没有匹配的记录，各自为对方模拟出NULL进行匹配。

客户表：t_customer

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677405118434-d9979d32-5647-4b0a-8d65-1ff6b61c6d44.png#averageHue=%23131210&clientId=u1be67ea7-0240-4&from=paste&height=137&id=u66bb1e76&originHeight=137&originWidth=235&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4218&status=done&style=shadow&taskId=u7d338668-6c7a-488f-851d-635afa97d29&title=&width=235)

订单表：t_order

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677405287024-4df811ac-9216-47c3-98b2-20f5d7ce2886.png#averageHue=%23151311&clientId=u1be67ea7-0240-4&from=paste&height=136&id=u8ef1b39a&originHeight=136&originWidth=261&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4032&status=done&style=shadow&taskId=u69ae2de5-204a-4a0b-8d2f-67ccbc73ad2&title=&width=261)

案例：查询所有的客户和订单。

```sql

select

c.*,o.*

from

t_customer c

full join

t_order o

on

c.cid = o.cid;

```

  

### 多张表连接

三张表甚至更多张表如何进行表连接

案例：找出每个员工的部门，并且要求显示每个员工的薪资等级。

```sql

select

e.ename,d.dname,s.grade

from

emp e

join

dept d

on

e.deptno = d.deptno

join

salgrade s

on

e.sal between s.losal and s.hisal;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677404511432-b8fe8eb2-c828-4913-8d7c-a7b47a0ee270.png#averageHue=%23171411&clientId=u1be67ea7-0240-4&from=paste&height=381&id=u6047af30&originHeight=381&originWidth=324&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18547&status=done&style=shadow&taskId=uc90c12f6-bdbb-4221-abe5-dcc4e221c96&title=&width=324)

  

---

## 子查询

  

### 什么是子查询

  

1. select语句中嵌套select语句就叫做子查询。

2. select语句可以嵌套在哪里？where后面、from后面、select后面都是可以的。

  

```sql

select ..(select)..

from ..(select)..

where ..(select)..

```

  

### where后面使用子查询

  

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

  

### from后面使用子查询

  

小窍门：**from后面的子查询可以看做一张临时表**。

案例：找出每个部门的平均工资的等级。

第一步：先找出每个部门平均工资。

```sql

select deptno, avg(sal) avgsal from emp group by deptno;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677477788393-e2525a0a-2092-4a5e-80e7-7f8df04f6a6c.png#averageHue=%23151311&clientId=ud7d035d7-9c64-4&from=paste&height=163&id=u397cf064&originHeight=163&originWidth=303&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5620&status=done&style=shadow&taskId=uc8a5cf34-abe3-446f-9948-e3cedf385f9&title=&width=303)

第二步：将以上查询结果当做临时表t，t表和salgrade表进行连接查询。条件：`t.avgsal between s.losal and s.hisal`

```sql

select t.*,s.grade from (select deptno, avg(sal) avgsal from emp group by deptno) t join salgrade s on t.avgsal between s.losal and s.hisal;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677477892811-ef9b366b-82be-4407-86f1-8dfa81492d8c.png#averageHue=%23151311&clientId=ud7d035d7-9c64-4&from=paste&height=162&id=u5d9f4ab4&originHeight=162&originWidth=397&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7422&status=done&style=shadow&taskId=uc90565b7-edc2-43bf-ba54-1e7db925c63&title=&width=397)

  

### select后面使用子查询

  

```sql

select e.ename,(select d.dname from dept d where e.deptno = d.deptno) as dname from emp e;

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678063689524-a204a93a-6454-4ff7-a1c6-ac5229edae91.png#averageHue=%231a1714&clientId=ud9fded62-54bb-4&from=paste&height=428&id=u2b69cf05&originHeight=428&originWidth=276&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16342&status=done&style=shadow&taskId=ua4f4e977-d3e6-4e90-8781-42050638d4a&title=&width=276)

  

### exists、not exists

  

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

  

### in和exists区别

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

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078225300-461e069f-0c80-4745-88a7-2969acccd076.png#averageHue=%23141210&clientId=ue32f086e-fc2b-4&from=paste&height=488&id=u46d82364&originHeight=488&originWidth=404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31584&status=done&style=shadow&taskId=u459bc800-2e1c-4247-866e-b06b0313a0c&title=&width=404)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078278429-e97f96a1-7429-4b68-8df9-3bda3a890797.png#averageHue=%23151210&clientId=ue32f086e-fc2b-4&from=paste&height=884&id=u2ef6109a&originHeight=884&originWidth=408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60134&status=done&style=shadow&taskId=u8c39e0b0-c274-46f0-8866-347160e1418&title=&width=408)

  

案例：查询工作岗位是MANAGER和SALESMAN的员工。

```sql

select ename,sal from emp where job='MANAGER'

union all

select ename,sal from emp where job='SALESMAN';

```

以上案例采用or也可以完成，那or和union all有什么区别？**考虑走索引优化之类的选择union all，其它选择or**。

两个结果集合并时，列数量要相同：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078078467-89b7ba88-52ae-4e70-b5cc-b4fe4a3daf76.png#averageHue=%2312110f&clientId=ue32f086e-fc2b-4&from=paste&height=101&id=u85e05b84&originHeight=101&originWidth=999&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11813&status=done&style=shadow&taskId=u29bd097d-8994-4842-be9e-3bcb8865687&title=&width=999)

  

---

## limit

  

1. limit作用：查询第几条到第几条的记录。通常是因为表中数据量太大，需要分页显示。

2. limit语法格式：

3. limit 开始下标, 长度

4. 案例：查询员工表前5条记录

```sql

select ename,sal from emp limit 0, 5;

```

如果下标是从0开始，可以简写为：

```sql

select ename,sal from emp limit 5;

```

  

4. 查询工资排名在前5名的员工（limit是在order by执行之后才会执行的）

```sql

select ename,sal from emp order by sal desc limit 5;

```

  

5. 通用的分页sql

  

假设每页显示3条记录：pageSize = 3

第1页：limit 0, 3

第2页：limit 3, 3

第3页：limit 6, 3

第pageNo页：`limit (pageNo - 1)*pageSize, pageSize`

  

---

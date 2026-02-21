# DQL
> 数据查询语言（Data **Query** Language, DQL）是SQL语言中，负责进行数据查询而不会对数据本身进行修改的语句。查询是SQL语言的核心，用于表达SQL查询的`select`查询命令是功能最强也是最为复杂的SQL语句，它的作用就是从数据库中检索数据，并将查询结果返回给用户。 select语句由：select子句(查询内容)、from子句(查询对象)、where子句(查询条件)、order by子句(排序方式)、group by子句(分组方式)等组成。
> 本章案例的数据初始化：[powerpoint-init-data](../details/powerpoint-init-data.md)

---
## `SELECT`, `FROM`, `AS`

### 查一个字段

查询一个字段说的是：一个表有多列，查询其中的一列。
```sql
select 字段名 from 表名;
```

- `select`和`from`是关键字，不能随便写
- **一条SQL语句必须以“;”结尾**
- **对于SQL语句来说，大小写都可以**
- 字段名和表名属于标识符，按照表的实际情况填写，不知道字段名的，可以使用desc命令查看表结构
* 案例：查询公司中所有员工编号/员工姓名 [select-01](../details/select-01.md)

### 查多个字段

查询多个字段时，在字段名和字段名之间添加“,”即可。
```sql
select 字段名1,字段名2,字段名3 from 表名;
```

* 字段的前后顺序无所谓（只是显示结果列的时候顺序变了）
* 案例：[select-02](../details/select-02.md)

### 查所有字段

查询所有字段的可以将每个字段都列出来查询，也可以采用`*`来代表所有字段
```sql
select * from 表名;
```

* 采用`*`进行查询存在的缺点：
	- `select * from dept;` 在执行的时候会被解析为 `select DEPTNO, DNAME, LOC from dept;` 再执行，所以这种效率方面弱一些。
	- 采用`*`的可读性较差，通过`*`很难看出都有哪些具体的字段。
- 什么时候使用`*`：这个SQL语句不在项目编码中使用，更常用语平时自己想快速查看表中所有数据。
- 案例：查询部门表所有信息 [select-03](../details/select-03.md)

### 查询时字段可参与数学运算

在进行查询操作的时候，字段是可以参与数学运算的，例如**加减乘除**等。
```sql
-- 比如年薪 = 月薪 * 12
select ename, sal * 12 from emp;
```
* 完整案例：查询每个员工的年薪（月薪 * 12），月薪加1000之后的月薪，月薪加1000之后的年薪。[select-04](../details/select-04.md)

### 查询时字段可起别名

结果列名`sal * 12`可读性较差，是否可以给查询结果的列名进行重命名呢？
```sql
-- 使用as关键字
select ename, sal * 12 as yearsal from emp;
-- 省略as关键字
select ename, sal * 12 yearsal from emp;
-- 空格需要用引号包围
select ename, sal * 12 "year sal" from emp;
select ename, sal * 12 'year sal' from emp;
-- 中文
select ename, sal * 12 年薪 from emp;
```
* 在mysql中，字符串既可以使用双引号也可以使用单引号，但还是建议使用单引号，因为单引号属于标准SQL。
* 别名是中文是可以的，但是对于低版本的mysql来说会报错，需要添加双引号或单引号。(8.0是可以支持的)

---

## `WHERE` 

### 条件查询语法格式

```sql
select 
  ...
from
  ...
where
  过滤条件;
```
过滤条件放在where子句当中，以上语句的执行顺序是：
* 第一步：先执行from
* 第二步：再通过where条件过滤
* 第三步：最后执行select，查询并将结果展示到控制台

### 符号

| **条件**                | **说明**          | 案例                                   |
| --------------------- | --------------- | ------------------------------------ |
| =                     | 等于              | [select-05](../details/select-05.md) |
| <> 或 !=               | 不等于             | [select-06](../details/select-06.md) |
| >, >=, <, <=          | 大于、大于等于、小于、小于等于 | [select-07](../details/select-07.md) |
| between...and...      | 等同于 >= and <=   | [select-08](../details/select-08.md) |
| is null / is not null | 为空 / 不为空        | [select-09](../details/select-09.md) |
| <=>                   | 安全等于（可读性差）      | 很少使用了                                |
| and 或 &&              | 并且              | [select-10](../details/select-10.md) |
| or 或 \|\|             | 或者              | [select-11](../details/select-11.md) |
| in / not in           | 在 / 不在指定的值当中    | [select-12](../details/select-12.md) |
| exists / not exists   | 存在 / 不存在        | [select-13](../details/select-13.md) |
| like                  | 模糊查询            | [select-14](../details/select-14.md) |
* mysql和orcal区别
	* MySQL判断字符串相等不区分大小写
	* Oracle判断字符串相等区分大小写
* and和or的优先级问题
	* **and优先级较高，会先执行**，如果希望or先执行，可以添加小括号。
	* 可以通过添加小括号的方式来解决。对于优先级问题没必要记忆。
* 在MySQL当中，如何统计一个SQL语句的执行时长？[sql-time](../details/sql-time.md)
* in和or的效率比拼：`or`的效率为O(n)，而`in`的效率为O(log n), 当n越大的时候效率相差越明显（也就是说数据量越大的时候，in的效率越高）。[select-in-or](../details/select-in-or.md)
* in不要使用null
	* **in自动忽略NULL**
	* **not in是不会自动忽略NULL**

---
## `ORDER BY`

### 单一字段

排序操作很常用，比如查询学员成绩，按照成绩降序排列。排序的SQL语法：
```sql
select .. from .. order by 字段 asc/desc
```
* 升序(默认)，用asc：[order-by-01](../details/order-by-01.md)
* 降序，用desc：[order-by-02](../details/order-by-02.md)

### 多个字段

多个要排序的内容依次写好就可以了：
```sql
select ... from ... order by A asc/desc, B asc/desc;
```
* [order-by-03](../details/order-by-03.md)

### where和order by的位置

where先执行，order by语句是最后执行的：
```sql
select ... from ... where ... order by ...;
```
* [order-by-04](../details/order-by-04.md)

---
## `DISTINCT`

```sql
select distinct 字段[,其他字段] from ...;
```
* 普通案例：[distinct-01](../details/distinct-01.md)（注意：这个去重只是将显示的结果去重，原表数据不会被更改。）
* `distinct`必须是第一个字段！：[distinct-02](../details/distinct-02.md)
* `distinct`出现后，后面多个字段一定是**联合去重**的：[distinct-03](../details/distinct-03.md)

---
## `GROUP UP`




### 统计函数

```sql
-- COUNT (及格的同学)
SELECT COUNT(*) FROM student
	WHERE chinese >= 60 AND english >= 60 AND math >= 60;

-- COUNT (所有的分数取值，主要是为了演示COUNT的用法, 会排除为NULL，但不会去重)
SELECT COUNT(`english`) FROM student;
SELECT COUNT(DISTINCT english) FROM student; -- 这样就去重了
-- SUM（英语总分）
SELECT SUM(english) FROM student;
-- AVG（英语平均分）
SELECT AVG(english) FROM student;
-- MAX（英语最高分）
SELECT MAX(english) FROM student;
-- MIN（英语最低分）
SELECT MIN(english) FROM student;
```

### 分组查询：GROUP BY 与 HAVING

```sql
-- 创建部门表 (dept) 并插入数据
CREATE TABLE dept (
    deptnum MEDIUMINT UNSIGNED NOT NULL DEFAULT 0,  /* 部门编号 */
    dname VARCHAR(20) NOT NULL DEFAULT "",          /* 部门名称 */
    loc VARCHAR(13) NOT NULL DEFAULT ""             /* 部门位置 */
);

INSERT INTO dept VALUES
(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH', 'DALLAS'),
(30, 'SALES', 'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON');

-- 创建雇员表 (emp) 并插入数据
CREATE TABLE emp (
    empno MEDIUMINT UNSIGNED NOT NULL DEFAULT 0,    /* 雇员编号 */
    ename VARCHAR(20) NOT NULL DEFAULT "",          /* 雇员姓名 */
    job VARCHAR(9) NOT NULL DEFAULT "",             /* 工作职位 */
    mgr MEDIUMINT UNSIGNED,                        /* 上级编号 */
    hiredate DATE NOT NULL,                         /* 入职时间 */
    sal DECIMAL(7,2) NOT NULL,                      /* 薪水 */
    comm DECIMAL(7,2),                              /* 红利 */
    deptnum MEDIUMINT UNSIGNED NOT NULL DEFAULT 0   /* 部门编号 */
);

INSERT INTO emp VALUES
(7369, 'SMITH', 'CLERK', 7902, '1990-12-17', 800.00, NULL, 20),
(7499, 'ALLEN', 'SALESMAN', 7698, '1991-2-20', 1600.00, 300.00, 30),
(7521, 'WARD', 'SALESMAN', 7698, '1991-2-22', 1250.00, 500.00, 30),
(7566, 'JONES', 'MANAGER', 7839, '1991-2-22', 2975.00, NULL, 20),
(7698, 'BLAKE', 'MANAGER', 7839, '1991-5-1', 2850.00, NULL, 30),
(7768, 'CLARK', 'MANAGER', 7839, '1991-6-9', 2450.00, NULL, 10),
(7788, 'SCOTT', 'ANALYST', 7566, '1997-4-19', 3000.00, NULL, 20),
(7839, 'KING', 'PRESIDENT', NULL, '1991-11-17', 5000.00, NULL, 10),
(7844, 'TURNER', 'SALESMAN', 7698, '1991-9-8', 1500.00, NULL, 30),
(7900, 'JAMES', 'CLERK', 7698, '1991-12-3', 950.00, NULL, 30),
(7902, 'FORD', 'ANALYST', 7566, '1991-12-3', 3000.00, NULL, 20),
(7934, 'MILLER', 'CLERK', 7782, '1992-1-23', 1300.00, NULL, 10);

-- 工资级别表 (salgrade)
CREATE TABLE salgrade (
    grade MEDIUMINT UNSIGNED NOT NULL DEFAULT 0,  /* 工资级别 */
    losal DECIMAL(17,2) NOT NULL,                /* 该级别的最低工资 */
    hisal DECIMAL(17,2) NOT NULL                  /* 该级别的最高工资 */
);
INSERT INTO salgrade VALUES (1, 700, 1200);
INSERT INTO salgrade VALUES (2, 1201, 1400);
INSERT INTO salgrade VALUES (3, 1401, 2000);
INSERT INTO salgrade VALUES (4, 2001, 3000);
INSERT INTO salgrade VALUES (5, 3001, 9999);
```

```sql
-- 查询每个部门的平均工资和最高工资，并按照部门编号升序排序
SELECT AVG(sal), MAX(sal), deptnum FROM emp
	GROUP BY deptnum
	ORDER BY deptnum;

-- 查询每个部门的平均工资和最高工资，并按照部门编号升序排序，并且只保留平均工资大于2000的部门
SELECT AVG(sal), MAX(sal), deptnum FROM emp
	GROUP BY deptnum
	HAVING AVG(sal) > 2000
	ORDER BY deptnum;   

-- 更好的办法：HAVING可以使用别名，提高效率
SELECT AVG(sal) as avg_sal, MAX(sal), deptnum FROM emp
	GROUP BY deptnum
	HAVING avg_sal > 2000
	ORDER BY deptnum;
```

### 字符串函数

| 函数                | 语法                                      | 功能描述                         |
| ----------------- | --------------------------------------- | ---------------------------- |
| ​**​CHARSET​**​   | `CHARSET(str)`                          | 返回字符串的字符集                    |
| ​**​CONCAT​**​    | `CONCAT(string2[,…])`                   | 连接多个字符串                      |
| ​**​INSTR​**​     | `INSTR(string, substring)`              | 返回子串在字符串中出现的位置(从1开始)，未找到则返回0 |
| ​**​UCASE​**​     | `UCASE(string2)`                        | 将字符串转换为大写                    |
| ​**​LCASE​**​     | `LCASE(string2)`                        | 将字符串转换为小写                    |
| ​**​LEFT​**​      | `LEFT(string2, length)`                 | 从字符串左侧截取指定长度的字符              |
| ​**​LENGTH​**​    | `LENGTH(string)`                        | 返回字符串的字节长度                   |
| ​**​REPLACE​**​   | `REPLACE(str, search_str, replace_str)` | 在字符串中用新字符串替换所有匹配的子串          |
| ​**​STRCMP​**​    | `STRCMP(string1, string2)`              | 逐字符比较两个字符串的大小(返回-1,0,1)      |
| ​**​SUBSTRING​**​ | `SUBSTRING(str, position[, length])`    | 从指定位置开始截取指定长度的字符(位置从1开始)     |
| ​**​LTRIM​**​     | `LTRIM(string2)`                        | 去除字符串前端的空格                   |
| ​**​RTRIM​**​     | `RTRIM(string2)`                        | 去除字符串后端的空格                   |
| ​**​TRIM​**​      | `TRIM(string2)`                         | 去除字符串两端空格                    |

```sql
SELECT CHARSET('数据库') AS charset_result;
-- 结果(取决于数据库设置): utf8mb4 或 utf8


```

# 老韩结束

---

## 分组查询

### group by

按照某个字段分组，或者按照某些字段联合分组。注意：group by的执行是在where之后执行。

语法：

group by 字段

group by 字段1,字段2,字段3....

**找出每个岗位的平均薪资**

```sql

select job, avg(sal) from emp group by job;

```

**找出每个部门最高工资**

```sql

select deptno,max(sal) from emp group by deptno;

```

**找出每个部门不同岗位的平均薪资**

```sql

select deptno,job,avg(sal) from emp group by deptno,job;

```

**当select语句中有group by的话，select后面只能跟分组函数或参加分组的字段**

```sql

select ename,deptno,avg(sal) from emp group by deptno; // 这个SQL执行后会报错。

```

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1676866192155-44d23157-87d0-4a58-a9d5-2641619d74fe.png#averageHue=%23171412&clientId=u417b9e29-4007-4&from=paste&height=140&id=uae74e6b8&originHeight=140&originWidth=1141&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25591&status=done&style=shadow&taskId=u4097c74b-3d21-485a-a74f-1390352d2e3&title=&width=1141)

### having

having写在group by的后面，当你对分组之后的数据不满意，可以继续通过having对分组之后的数据进行过滤。

where的过滤是在分组前进行过滤。

使用原则：尽量在where中过滤，实在不行，再使用having。越早过滤效率越高。

  

**找出除20部分之外，其它部门的平均薪资。**

```sql

select deptno,avg(sal) from emp where deptno<>20 group by deptno; // 建议

select deptno,avg(sal) from emp group by deptno having deptno <> 20; // 不建议

```

  

  

**查询每个部门平均薪资，找出平均薪资高于2000的。**

```sql

select deptno,avg(sal) from emp group by deptno having avg(sal) > 2000;

```

### 组内排序

案例：找出每个工作岗位的工资排名在前两名的。

substring_index函数的使用：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678080182698-009c47d2-eb75-4f67-afaa-874c7904ed45.png#averageHue=%2312100f&clientId=ue32f086e-fc2b-4&from=paste&height=379&id=rhnfq&originHeight=379&originWidth=755&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27939&status=done&style=shadow&taskId=u49228cac-a6a0-4d31-8dbc-abc432cd804&title=&width=755)

group_concat函数的使用：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678082111760-02413f4e-a8b0-4837-8cb0-3b201151293f.png#averageHue=%23100f0e&clientId=ue32f086e-fc2b-4&from=paste&height=272&id=bhhYI&originHeight=272&originWidth=904&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20533&status=done&style=shadow&taskId=uac8b6d07-c85c-47d4-9724-b29c1e8f927&title=&width=904)

学习了这两个函数之后，自己可以尝试写出来吗？

  

---

## 总结单表的DQL语句

select ...5

from ...1

where ...2

group by ...3

having ...4

order by ...6

重点掌握一个完整的DQL语句执行顺序。

  

---

## 连接查询

### 什么是连接查询

  

1. 从一张表中查询数据称为单表查询。

2. 从两张或更多张表中联合查询数据称为多表查询，又叫做连接查询。

3. 什么时候需要使用连接查询？比如这样的需求：员工表中有员工姓名，部门表中有部门名字，要求查询每个员工所在的部门名字，这个时候就需要连接查询。

  

### 连接查询的分类

  

1. 根据语法出现的年代进行分类：

2. SQL92（这种语法很少用，可以不用学。）

3. SQL99（我们主要学习这种语法。）

4. 根据连接方式的不同进行分类：

5. 内连接

6. 等值连接

7. 非等值连接

8. 自连接

9. 外连接

10. 左外连接（左连接）

11. 右外连接（右连接）

12. 全连接

  

### 笛卡尔积现象

  

1. 🌟什么是笛卡尔积现象：当两张表进行连接查询时，如果没有任何条件进行过滤，**最终的查询结果条数是两张表条数的乘积**。

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

## 35个DQL练手题

### 第1题

  

1. 取得每个部门最高薪水的人员名称

  

第一步：取得每个部门最高薪水

```sql

select deptno,max(sal) as maxsal from emp group by deptno;

```

  

第二步：将上面第一步的查询结果当做一张临时表t，进行表连接，条件是：t.deptno=e.deptno and t.maxsal=e.sal

  

```sql

select e.ename,t.* from emp e join (select deptno,max(sal) as maxsal from emp group by deptno) t on e.deptno = t.deptno and e.sal = t.maxsal;

```

  

### 第2题

  

2. 哪些人的薪水在部门的平均薪水之上

第一步：取得每个部门的平均薪水

```sql

select deptno,avg(sal) as avgsal from emp group by deptno;

```

  

第二步：将上面的查询结果当做临时表t，让t和emp e表进行表连接，条件是：`t.deptno=e.deptno and e.sal>t.avgsal`

  

```sql

select e.ename,e.sal,t.* from emp e join (select deptno,avg(sal) as avgsal from emp group by deptno) t on t.deptno=e.deptno and e.sal>t.avgsal;

```

  

### 第3题

  

3. 取得每个部门平均薪水的等级

第一步：取得每个部门的平均薪水

```sql

select deptno,avg(sal) as avgsal from emp group by deptno;

```

  

第二步：将上面的查询结果当做临时表t，然后t和salgrade s表进行连接，条件是：t.avgsal between s.losal and s.hisal

  

```sql

select t.*,s.grade from (select deptno,avg(sal) as avgsal from emp group by deptno) t join salgrade s on t.avgsal between s.losal and s.hisal;

```

  

### 第4题

  

4. 取得部门中（所有人的）平均的薪水等级

第一步：找出每个人的薪水等级

```sql

select e.ename,e.sal,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;

```

  

第二步：在上面的查询结果当中继续按照部门编号进行分组，求平均值。（不需要将上面的查询结果当做临时表，继续基于它进行分组即可。）

  

```sql

select

e.deptno,avg(s.grade)

from

emp e

join

salgrade s

on

e.sal between s.losal and s.hisal

group by

e.deptno;

```

### 第5题

  

5. 不准用组函数（Max），取得最高薪水（给出两种解决方案）

第一种方案：按照薪资降序排列，取第一个。

```sql

select sal from emp order by sal desc limit 1;

```

  

第二种方案：采用表的自连接方式。

  

```sql

select ename,sal from emp where sal not in(select distinct a.sal from emp a join emp b on a.sal < b.sal);

```

  

### 第6题

  

6. 取得平均薪水最高的部门的部门编号（至少给出两种解决方案）

第一种方案：降序排列取第一个

```sql

select deptno,avg(sal) as avgsal from emp group by deptno order by avgsal desc limit 1;

```

  

第二种方案：max函数

  

```sql

select deptno,avg(sal) as avgsal from emp group by deptno having avg(sal)=(select max(t.avgsal) from (select avg(sal) as avgsal from emp group by deptno) t);

```

### 第7题

  

7. 取得平均薪水最高的部门的部门名称

比上面的题目多一个表连接，和dept表连接，按照部门名称进行分组。

```sql

select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno=d.deptno group by d.dname order by avgsal desc limit 1;

```

### 第8题

  

8. 求平均薪水的等级最低的部门的部门名称

第一步：求每个部门的平均薪水

```sql

select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname;

```

  

第二步：求每个部门的平均薪水等级（将以上的执行结果当做临时表t，t和salgrade s表进行连接，条件：t.avgsal between .s.losal and s.hisal）

  

```sql

select t.*,s.grade from (select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname) t join salgrade s on t.avgsal between s.losal and s.hisal;

```

  

第三步：找到最低的部门名称（以上结果继续按照grade进行升序，然后limit 1）

  

```sql

select t.*,s.grade from (select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname) t join salgrade s on t.avgsal between s.losal and s.hisal order by s.grade asc limit 1;

```

  

### 第9题

  

9. 取得比普通员工(员工代码没有在mgr字段上出现的)的最高薪水还要高的领导人姓名

第一步：找出所有的普通员工的最高薪水

```sql

select max(sal) from emp where empno not in(select mgr from emp where mgr is not null);

```

  

第二步：大于以上最高薪水的一定是要找的领导人。

  

```sql

select ename,sal from emp where sal > (select max(sal) from emp where empno not in(select mgr from emp where mgr is not null));

```

### 第10题

  

10. 取得薪水最高的前五名员工

```sql

select ename,sal from emp order by sal desc limit 5;

```

### 第11题

  

11. 取得薪水最高的第六到第十名员工

```sql

select ename,sal from emp order by sal desc limit 5, 5;

```

### 第12题

  

12. 取得最后入职的5名员工

```sql

select ename,sal,hiredate from emp order by hiredate desc limit 5;

```

  

### 第13题

  

13. 取得每个薪水等级有多少员工

  

第一步：找出每个员工的薪水等级

```sql

select e.ename,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;

```

  

第二步：基于以上的记录继续根据等级分组，count即可。

  

```sql

select s.grade,count(*) from emp e join salgrade s on e.sal between s.losal and s.hisal group by s.grade;

```

### 第14题

  

14. 列出所有员工及领导的姓名

```sql

select e.ename 员工名, l.ename 领导名 from emp e left join emp l on e.mgr = l.empno;

```

### 第15题

  

15. 列出受雇日期早于其直接上级的所有员工的编号,姓名,部门名称

```sql

select e.ename 员工名,e.hiredate, l.ename 领导名,l.hiredate,d.dname from emp e join emp l on e.mgr = l.empno join dept d on e.deptno = d.deptno where e.hiredate < l.hiredate;

```

  

### 第16题

  

16. 列出部门名称和这些部门的员工信息,同时列出那些没有员工的部门

```sql

select d.dname,e.ename,e.sal from dept d left join emp e on d.deptno = e.deptno;

```

### 第17题

  

17. 列出至少有5个员工的所有部门

```sql

select deptno, count(*) from emp group by deptno having count(*) >= 5;

```

### 第18题

  

18. 列出薪金比"SMITH"多的所有员工信息

```sql

select ename,sal from emp where sal > (select sal from emp where ename = 'SMITH');

```

  

### 第19题

  

19. 列出所有"CLERK"(办事员)的姓名及其部门名称,部门的人数

```sql

select t1.ename,t1.dname,t2.total from (select e.ename,d.dname,d.deptno from emp e join dept d on e.deptno = d.deptno where e.job = 'CLERK') t1 join (select count(*) as total,deptno from emp group by deptno) t2 on t1.deptno = t2.deptno;

```

### 第20题

  

20. 列出最低薪金大于1500的各种工作及从事此工作的全部雇员人数

```sql

select job,min(sal),count(*) from emp group by job having min(sal)>1500;

```

### 第21题

  

21. 列出在部门"SALES"<销售部>工作的员工的姓名,假定不知道销售部的部门编号

```sql

select e.ename,d.dname from emp e join dept d on e.deptno = d.deptno where d.dname='sales';

```

  

### 第22题

  

22. 列出薪金高于公司平均薪金的所有员工,所在部门,上级领导,雇员的工资等级

```sql

select e.ename 员工,l.ename 领导,d.dname,s.grade from

emp e left join emp l on e.mgr = l.empno

join dept d on e.deptno = d.deptno

join salgrade s on e.sal between s.losal and s.hisal

where e.sal > (select avg(sal) from emp);

```

### 第23题

  

23. 列出与"SCOTT"从事相同工作的所有员工及部门名称

```sql

select e.ename,d.dname,e.job from emp e join dept d on e.deptno=d.deptno where job=(select job from emp where ename ='scott');

```

### 第24题

  

24. 列出薪金等于部门30中员工的薪金的其他员工的姓名和薪金

```sql

select ename,sal,deptno from emp where sal in(select distinct sal from emp where deptno=30) and deptno <> 30;

```

  

### 第25题

  

25. 列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金.部门名称

```sql

select e.ename,e.sal,d.dname from emp e join dept d on e.deptno = d.deptno where sal > (select max(sal) from emp where deptno=30);

```

### 第26题

  

26. 列出在每个部门工作的员工数量,平均工资和平均服务期限

```sql

select avg(sal),count(*),deptno,avg(datediff(now(),hiredate)) as avgtime from emp group by deptno;

```

### 第27题

  

27. 列出所有员工的姓名、部门名称和工资

```sql

select e.ename,e.sal,d.dname from emp e join dept d on e.deptno = d.deptno;

```

  

### 第28题

  

28. 列出所有部门的详细信息和人数

```sql

select d.deptno,d.dname,d.loc,count(e.deptno) from emp e right join dept d on e.deptno=d.deptno group by d.deptno,d.dname,d.loc;

```

### 第29题

  

29. 列出各种工作的最低工资及从事此工作的雇员姓名

```sql

select t.job,t.minsal,e.ename from emp e join (select job,min(sal) as minsal from emp group by job) t on e.job=t.job and e.sal=t.minsal;

```

### 第30题

  

30. 列出各个部门的MANAGER(领导)的最低薪金

```sql

select deptno,min(sal) from emp where job='MANAGER' group by deptno

```

  

### 第31题

  

31. 列出所有员工的年工资,按年薪从低到高排序

```sql

select ename,(sal+ifnull(comm,0))*12 as yearsal from emp order by yearsal asc;

```

### 第32题

  

32. 求出员工领导的薪水超过3000的员工名称与领导名称

```sql

select e.ename 员工名, l.ename 领导名 from emp e join emp l on e.mgr = l.empno where l.sal>3000;

```

### 第33题

  

33. 求出部门名称中,带'S'字符的部门员工的工资合计、部门人数

```sql

select d.dname,ifnull(sum(sal),0) as sumsal,count(e.ename) from emp e right join dept d on e.deptno=d.deptno where d.dname like '%S%' group by d.dname;

```

### 第34题

  

34. 给任职日期超过30年的员工加薪10%

```sql

update emp set sal=sal*1.1 where datediff(now(),hiredate)/365 > 30;

```

  

### 第35题

  

35. 某公司面试题

  

有3个表S（学生表），C（课程表），SC（学生选课表）

S（SNO，SNAME）代表（学号，姓名）

C（CNO，CNAME，CTEACHER）代表（课号，课名，教师）

SC（SNO，CNO，SCGRADE）代表（学号，课号，成绩）

```sql

CREATE TABLE SC

(

SNO VARCHAR(200),

CNO VARCHAR(200),

SCGRADE VARCHAR(200)

);

  

CREATE TABLE S

(

SNO VARCHAR(200 ),

SNAME VARCHAR(200)

);

  

CREATE TABLE C

(

CNO VARCHAR(200),

CNAME VARCHAR(200),

CTEACHER VARCHAR(200)

);

  

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '1', '语文', '张');

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '2', '政治', '王');

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '3', '英语', '李');

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '4', '数学', '赵');

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '5', '物理', '黎明');

commit;

INSERT INTO S ( SNO, SNAME ) VALUES ( '1', '学生1');

INSERT INTO S ( SNO, SNAME ) VALUES ( '2', '学生2');

INSERT INTO S ( SNO, SNAME ) VALUES ( '3', '学生3');

INSERT INTO S ( SNO, SNAME ) VALUES ( '4', '学生4');

commit;

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '1', '40');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '2', '30');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '3', '20');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '4', '80');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '5', '60');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '1', '60');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '2', '60');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '3', '60');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '4', '60');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '5', '40');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '1', '60');

INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '3', '80');

commit;

```

问题：

1，找出没选过“黎明”老师的所有学生姓名。

```sql

select sname from s where sno not in(select sno from sc where cno=(select cno from c where cteacher='黎明'));

```

2，列出2门以上（含2门）不及格学生姓名及平均成绩。

```sql

select a.*,b.avgscore from (select s.sno,s.sname,count(sc.scgrade) as num from sc join s on sc.sno=s.sno where sc.scgrade < 60 group by s.sname,s.sno having count(sc.scgrade) >= 2) a join (select sno,avg(scgrade) avgscore from sc group by sno) b on a.sno = b.sno;

```

3，既学过1号课程又学过2号课所有学生的姓名。

```sql

select sc.sno,s.sname from sc join s on sc.sno=s.sno where sc.cno=1 and sc.sno in(select sno from sc where cno=2);

```
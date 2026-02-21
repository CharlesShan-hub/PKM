# DQL
> 数据查询语言（Data **Query** Language, DQL）是SQL语言中，负责进行数据查询而不会对数据本身进行修改的语句。查询是SQL语言的核心，用于表达SQL查询的`select`查询命令是功能最强也是最为复杂的SQL语句，它的作用就是从数据库中检索数据，并将查询结果返回给用户。 select语句由：select子句(查询内容)、from子句(查询对象)、where子句(查询条件)、order by子句(排序方式)、group by子句(分组方式)等组成。
> 本章案例的数据初始化：[powerpoint-init-data](../details/powerpoint-init-data.md)

---
## `SELECT`, `FROM`, `AS`

### 常量

```sql
select 常量;
```
* `select 1;`返回的就是1。

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

### 字段数学运算

在进行查询操作的时候，字段是可以参与数学运算的，例如**加减乘除**等。
```sql
-- 比如年薪 = 月薪 * 12
select ename, sal * 12 from emp;
```
* 完整案例：查询每个员工的年薪（月薪 * 12），月薪加1000之后的月薪，月薪加1000之后的年薪。[select-04](../details/select-04.md)
* 也可以返回运算后的内容，详见[function1](function1.md)

### 字段可取别名

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
* where后边不能用[分组函数](function2.md)
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
## `GROUP BY`, `HAVING`

### 分组

按照某个字段分组，或者按照某些字段联合分组。
```sql
group by 字段
group by 字段1,字段2,字段3....
```
* 不能在`where`使用分组函数（因为`group by`的执行是在`where`之后执行。）：[group-by-01](../details/group-by-01.md)
* 使用分组函数需要先分组，使用`group by`：[group-by-02](../details/group-by-02.md)
* 当`select`语句中有`group by`的话，`select`后面只能跟分组函数或参加分组的字段：[group-by-02](../details/group-by-02.md)
* 如果没有`group by`就默认整张表是一个分组


### 过滤

可以进一步在分组后进行过滤
```sql 
group by xxx having xxx
```
* having写在group by的后面，当你对分组之后的数据不满意，可以继续通过having对分组之后的数据进行过滤。
* where的过滤是在分组前进行过滤。
* 使用原则：**尽量在where中过滤**，实在不行，再使用having。越早过滤效率越高。
* 案例：[having](../details/having.md)，[having2](../details/having2.md)

---
## 组内排序

* substring_index
* group_concat
* 案例：[inner-order](../details/inner-order.md)

---

## 总结单表的DQL语句

select ...5

from ...1

where ...2

group by ...3

having ...4

order by ...6

重点掌握一个完整的DQL语句执行顺序。

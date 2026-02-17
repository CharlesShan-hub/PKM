# CRUD

## Create

1. 插入单条数据
	```sql
	INSERT INTO table_name (column1, column2, column3, ...)
	VALUES (value1, value2, value3, ...);
	```
2. 插入多条数据
	```sql
	INSERT INTO table_name (column1, column2, column3,...)
	VALUES (value1, value2, value3,...),
	(value1, value2, value3,...),
	(value1, value2, value3,...),
	...;   
	```
3. 插入数据并返回插入的ID
	```sql
	INSERT INTO table_name (column1, column2, column3,...)
	VALUES (value1, value2, value3,...)
	RETURNING id;
	```

细节
1. 整型字段插入字符串会报错吗？
	不一定，MySQL会自动转换为数字类型。
2. 长度80的字符串插入到长度为10的字符串字段会报错吗？
	会的，MySQL没有自动截断。
3. 插入空的方法：插入NULL
4. 添加所有列，可以不写列名，但是要保证列的顺序和表的顺序一致。
5. 不给定值的列，会插入默认值。（前边的列名没写，后边的值也没有，这样缺失的列会插入默认值）


## Update

```sql
UPDATE table_name
SET column1 = value1, column2 = value2,...
WHERE condition;
```

⚠️注意如果没有带条件，会更新所有行！！！

## Delete

```sql
DELETE FROM table_name
WHERE condition;
```
⚠️注意如果没有带条件，会删除所有行！！！



## Read

### 单表查询

```sql
SELECT [DISTINCT] column1, column2, ...
FROM table_name;
```
* DISTINCT 可以去重
* 可以指定列名，也可以指定*，表示所有列

比较运算符

|运算符|说明|示例|
|---|---|---|
|`>`, `<`, `<=`, `>=`|大于、小于、小于等于、大于等于|`WHERE salary > 5000`|
|`=`|等于|`WHERE name = '张三'`|
|`<>`, `!=`|不等于|`WHERE status <> 1`|
|`BETWEEN...AND...`|在某个区间范围内|`WHERE age BETWEEN 18 AND 30`|
|`IN(set)`|在指定值列表中|`WHERE id IN (1, 3, 5)`|
|`LIKE 'pattern'`|模糊匹配|`WHERE name LIKE '张%'`|
|`NOT LIKE`|不匹配模式|`WHERE name NOT LIKE '%测试%'`|
|`IS NULL`|判断是否为空|`WHERE email IS NULL`|
逻辑运算符

|运算符|说明|示例|
|---|---|---|
|`AND`|多个条件同时成立|`WHERE age > 18 AND gender = '男'`|
|`OR`|多个条件任一成立|`WHERE status = 1 OR status = 3`|
|`NOT`|条件不成立|`WHERE NOT(deleted = 1)`|

案例

```sql
CREATE TABLE student (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(20) NOT NULL DEFAULT '',
    chinese FLOAT NOT NULL DEFAULT 0.0,
    english FLOAT NOT NULL DEFAULT 0.0,
    math FLOAT NOT NULL DEFAULT 0.0
);

INSERT INTO student(id, name, chinese, english, math) VALUES
(1, '韩顺平', 89, 78, 90),
(2, '张飞', 67, 98, 56),
(3, '宋江', 87, 78, 77),
(4, '关羽', 88, 98, 90),
(5, '赵云', 82, 84, 67),
(6, '欧阳锋', 55, 85, 45),
(7, '黄蓉', 75, 65, 30);
```


```sql
-- 查询的时候可以进行运算
SELECT `name`, (english+chinese+math) FROM student;

-- 查询的时候可以给列名一个别名
SELECT `name` as `姓名`, (english+chinese+math) as `总分` FROM student;

-- 大于
SELECT `name` as `姓名`, (english+chinese+math) as `总分` 
	FROM student
	WHERE (english+chinese+math) > 250;

-- AND
SELECT `name` as `姓名`, (english+chinese+math) as `总分`
	FROM student
	WHERE chinese > 80 AND english > 60;

-- LIKE（比如名字以韩开头的）
SELECT `name` as `姓名`, (english+chinese+math) as `总分`
	FROM student
	WHERE `name` LIKE '韩%';

-- 在某个集合里边
SELECT `name` as `姓名`, (english+chinese+math) as `总分`
	FROM student
	WHERE english in (80, 82, 84);

-- 升序排序（默认）
SELECT `name`, `english`, `chinese`, `math`
	FROM student
	ORDER BY english 
	-- 或者 ORDER BY english ASC;   

-- 降序
SELECT `name`, `english`, `chinese`, `math`
	FROM student
	ORDER BY english DESC;
```

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



### 日期函数



### 多表查询

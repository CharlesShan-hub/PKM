# DDL
>    数据定义语言 (Data **Definition** Language, DDL) 是SQL语言集中，负责数据结构定义与数据库对象定义的语言，由CREATE、ALTER与DROP三个语法所组成，最早是由 Codasyl (Conference on Data Systems Languages) 数据模型开始，现在被纳入 SQL 指令中作为其中一个子集。

---
## 数据库表的概述

| name | age | gender |
| --- | --- | --- |
| 张三 | 20 | 男 |
| 李四 | 22 | 女 |

- 以上就是数据库表格的直观展示形式。
- 表格英文单词table。
- 表是数据库存储数据的基本单元，数据库存储数据的时候，是将数据存储在表对象当中的。为什么将数据存储在表中呢？因为表存储数据非常直观。
- 任何一张表都有行和列
	- 行：记录（一行就是一条数据）
	- 列：字段（name字段、age字段、gender字段）
- 每个字段包含以下属性
	- 字段名：name、age、gender都是字段的名字
	- 字段的数据类型：每个字段都有数据类型，比如：字符类型、数字类型、日期类型
	- 字段的数据长度：每个字段有可能会有长度的限制
	- 字段的约束：比如某些字段要求该字段下的数据不能重复、不能为空等，用来保证表格中数据合法有效

---
## 数据表操作

### 创建表

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ....
)CHARACTER SET utf8 COLLATE utf8_general_ci ENGINE=InnoDB;
```
* `CHARACTER SET utf8`：指定表的字符集为 utf8。
* `COLLATE utf8_general_ci`：指定表的排序规则为 utf8_general_ci。
* `ENGINE=InnoDB`：指定表的存储引擎为 InnoDB，这是 MySQL 的默认引擎。

### 删除表
```sql
DROP TABLE table_name;
```

### 查看数据库有哪些表
```sql
show tables;
```

### 查看表结构
```sql
DESC table_name;
```

### 修改表
1. 修改表名
	```sql
	ALTER TABLE old_table_name
	RENAME TO new_table_name;
	```

2. 添加列
	```sql
	ALTER TABLE table_name
	ADD COLUMN column_name data_type;
	```
	
3. 删除列
	```sql
	ALTER TABLE table_name
	DROP COLUMN column_name;
	```
	
4. 修改列
	```sql
	ALTER TABLE table_name
	MODIFY COLUMN column_name new_data_type;
	```

5. 修改列名
	```sql
	ALTER TABLE table_name
	CHANGE COLUMN old_column_name new_column_name data_type;
	```

6. 修改表字符集
	```sql
	ALTER TABLE table_name
	CONVERT TO CHARACTER SET charset_name;
	```

7. 案例：**员工表 emp 结构修改要求**
	1. 在表中增加一个 `image` 列，类型为 `VARCHAR`，位置在 `resume` 后面。
	2. 修改 `job` 列的长度为 60。
	3. 删除 `sex` 列。
	4. 将表名从 `emp` 改为 `employee`。
	5. 修改表的字符集为 `utf-8`。
	6. 将列名 `name` 修改为 `user_name`。

	```sql
	-- 1. 增加 image 列 
	ALTER TABLE emp 
		ADD COLUMN image VARCHAR(255) NOT NULL DEFAULT '' 
		AFTER resume;
	-- 2. 修改 job 列长度 
	ALTER TABLE emp 
		MODIFY COLUMN job VARCHAR(60) NOT NULL DEFAULT ''; 
	-- 3. 删除 sex 列 
	ALTER TABLE emp 
		DROP COLUMN sex;
	-- 4. 修改表名
	ALTER TABLE emp
		RENAME TO employee; 
	-- 5. 修改字符集 
	ALTER TABLE employee 
		CONVERT TO CHARACTER SET utf8; 
	-- 6. 修改列名 name → user_name 
	ALTER TABLE employee 
		CHANGE COLUMN name user_name VARCHAR(50) NOT NULL DEFAULT '';
	```

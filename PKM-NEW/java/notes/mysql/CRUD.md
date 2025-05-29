# CRUD

## 修改表

1. 添加列

	```sql
	ALTER TABLE table_name
	ADD COLUMN column_name data_type;
	```

2. 修改列

	```sql
	ALTER TABLE table_name
	MODIFY COLUMN column_name new_data_type;
	```
	
3. 删除列

	```sql
	ALTER TABLE table_name
	DROP COLUMN column_name;
	```
	
4. 修改表名

	```sql
	ALTER TABLE old_table_name
	RENAME TO new_table_name;
	```

5. 案例：**员工表 emp 结构修改要求：​**​
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

## 插入数据

1. 插入单条数据
	```sql
	INSERT INTO table_name (column1, column2, column3, ...)
	VALUES (value1, value2, value3, ...);
	```




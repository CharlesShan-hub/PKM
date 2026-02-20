# DML
> 数据操纵语言（Data **Manipulation** Language, DML）是SQL语言中，负责对数据库对象运行数据访问工作的指令集，以INSERT、UPDATE、DELETE三种指令为核心，分别代表插入、更新与删除。

---
## INSERT

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

---
## Update

```sql
UPDATE table_name
SET column1 = value1, column2 = value2,...
WHERE condition;
```

⚠️注意如果没有带条件，会更新所有行！！！

---
## Delete

```sql
DELETE FROM table_name
WHERE condition;
```
⚠️注意如果没有带条件，会删除所有行！！！

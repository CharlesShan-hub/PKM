# DML
> 数据操纵语言（Data **Manipulation** Language, DML）是SQL语言中，负责对数据库对象运行数据访问工作的指令集，以INSERT、UPDATE、DELETE三种指令为核心，分别代表插入、更新与删除。

---
## INSERT

1. 插入单条数据，一般为了可读性强，建议把字段名写上。
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

语法格式：
```sql
# 将所有记录全部删除
delete from 表名;

# 删除符合条件的记录
delete from 表名 where 条件;
```
以上的删除属于DML的方式删除，这种删除的数据是可以通过事务回滚的方式重新恢复的，但是删除的效率较低。（这种删除是支持事务的。）
另外还有一种删除表中数据的方式，但是这种方式不支持事务，不可以回滚，删了之后数据是永远也找不回来了。这种删除叫做：表被截断。
注意：这个语句删除效率非常高，巨大的表，瞬间干掉所有数据。但不可恢复。
```sql
truncate table 表名;
```

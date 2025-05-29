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


## Read


## Update


## Delete



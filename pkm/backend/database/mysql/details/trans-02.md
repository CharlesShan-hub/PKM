1. 初始化，设置隔离级别，开启事务
	```sql
	-- session1
	use bjpowernode;
	drop table if exists test_trans;
	create table test_trans(
		id int,
		name varchar(32)
	);
	set session transaction isolation level read committed;
	start transaction;
	```
	```sql
	-- session2
	use bjpowernode;
	set session transaction isolation level read committed;
	start transaction;
	```
2. 第二个事务进行insert，然后commit，第一个事务可以select到新纪录。
	```sql
	-- session1
	select * from test_trans; -- 这里可以看到什么都没有
	```
	```sql
	-- session2
	insert into test_trans values(1, 'trans2');
	commit; -- 多了这个
	```
	```sql
	-- session1
	select * from test_trans; -- 这里可以看到session2提交的数据
	```
	通过以上测试看出，1事务只能读取到2事务提交之后的数据。这种隔离级别解决了脏读问题，但肯定是存在不可重复读和幻读问题。因为只要事务2进行了增删改操作之后并提交了，事务1读取到的数据肯定是不同的。即：不可重复读和幻读都存在。
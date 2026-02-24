我们可以开启两个DOS命令窗口，模拟两个事务，演示一下这种隔离级别。三种现象中最严重的是脏读，我们只需要演示脏读问题即可，因为存在脏读的话，就一定存在不可重复读和幻读问题。
1. 初始化，设置隔离级别，开启事务
	```sql
	-- session1
	use bjpowernode;
	drop table if exists test_trans;
	create table test_trans(
		id int,
		name varchar(32)
	);
	set session transaction isolation level read uncommitted;
	start transaction;
	```
	```sql
	-- session2
	use bjpowernode;
	set session transaction isolation level read uncommitted;
	start transaction;
	```
2. 第二个事务进行insert，但是不commit，第一个事务可以select到新纪录。
	```sql
	-- session2
	insert into test_trans values(1, 'trans2');
	```
	```sql
	-- session1
	select * from test_trans; -- 这里可以看到session2提交的数据
	```
	通过以上测试，可以看到，1事务读取到了2事务还没有提交的数据。这种现象就是脏读。
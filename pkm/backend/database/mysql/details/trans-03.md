1. 初始化，设置隔离级别，开启事务
	```sql
	-- session1
	use bjpowernode;
	drop table if exists test_trans;
	create table test_trans(
		id int,
		name varchar(32)
	);
	set session transaction isolation level repeatable read;
	start transaction;
	```
	```sql
	-- session2
	use bjpowernode;
	set session transaction isolation level repeatable read;
	start transaction;
	```
2. 第二个事务进行insert，然后commit，第一个事务可以select不到新纪录，但是xxx
	```sql
	-- session1
	select * from test_trans; -- 这里可以看到什么都没有
	-- 必须要先select这一下，建立快照
	```
	```sql
	-- session2
	insert into test_trans values(1, 'trans2');
	commit; -- 多了这个
	```
	```sql
	-- session1
	select * from test_trans; -- 这里现在也是看不到内容了
	select * from test_trans for update; -- 幻读（能看到insert的内容）
	```
	通过以上测试得知：**当事务隔离级别设置为可重复读，MySQL会尽最大努力避免幻读问题，但这种隔离级别无法完全避免幻读问题。**
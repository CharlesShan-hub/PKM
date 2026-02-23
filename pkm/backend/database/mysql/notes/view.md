# 视图

1. 只能将select语句创建为视图。
2. 创建视图
	```sql
	create or replace view v_emp as select e.ename,d.dname from emp e join dept d on e.deptno = d.deptno;
	```
3. 视图作用
	1. 如果开发中有一条非常复杂的SQL，而这个SQL在多处使用，会给开发和维护带来成本。使用视图可以降低开发和维护的成本。
	2. 视图可以隐藏表的字段名。
4. 修改视图
	```sql
	alter view v_emp as select e.ename,d.dname,d.deptno from emp e join dept d on e.deptno = d.deptno;
	```
5. 删除视图：`drop view if exists v_emp;`
6. 对视图增删改（DML：insert delete update）可以影响到原表数据。


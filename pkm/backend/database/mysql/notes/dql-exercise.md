
## 35个DQL练手题

> 本章案例的数据初始化：[powerpoint-init-data](../details/powerpoint-init-data.md)

### 第1题

取得每个部门最高薪水的人员名称

1. 首先获得每个部门编号，作为临时表t
	```sql
	select deptno, max(sal) as maxsal from emp group by deptno;
	```
2. join 员工表
	```sql
	select 
		e.ename, e.sal, e.deptno
	from 
		emp e
	join
		(select deptno, max(sal) as maxsal from emp group by deptno) t 
	on
		e.deptno = t.deptno and e.sal = t.maxsal;
	```

### 第2题

哪些人的薪水在部门的平均薪水之上

1. 先获得每个部门平均薪水作为临时表t
	```sql
	select deptno, avg(sal) avgsal from emp group by deptno;
	```
2. join 员工表
	```sql
	select
		e.ename, sal, avgsal
	from
		emp e
	join
		(select deptno, avg(sal) avgsal from emp group by deptno) t
	where
		e.sal > t.avgsal and e.deptno = t.deptno;
	```

### 第3题

取得每个部门平均薪水的等级

1. 先获得每个部门平均薪水作为临时表t
	```sql
	select deptno, avg(sal) avgsal from emp group by deptno;
	```
2. join 薪水登记表
	```sql
	select
		t.*, s.grade
	from 
		salgrade s
	join
		(select deptno, avg(sal) avgsal from emp group by deptno) t
	where 
		t.avgsal between s.losal and s.hisal;
	```

### 第4题

取得部门中（所有人的）平均的薪水等级

1. 得到每个人的薪水等级
	```sql
	select e.ename, e.sal, s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;
	```
2. 在上面的查询结果当中继续按照部门编号进行分组，求平均值。（不需要将上面的查询结果当做临时表，继续基于它进行分组即可。）
	```sql
	select e.deptno, avg(s.grade) from emp e join salgrade s on e.sal between s.losal and s.hisal group by deptno;
	```

### 第5题

不准用组函数（Max），取得最高薪水（给出两种解决方案）

第一种方案：按照薪资降序排列，取第一个。
```sql
select ename,sal from emp order by sal desc limit 1;
```
第二种方案：采用表的自连接方式。（这种自连接方法在**小数据集**上可能还能接受，但在**生产环境或大数据集**中**绝对不要使用**。它只是为了展示“不用组函数”的一种思路，实际开发中应使用 `MAX()` 或 `ORDER BY ... LIMIT`。）
```sql
select ename,sal from emp where sal not in(select distinct a.sal from emp a join emp b on a.sal < b.sal);
```

### 第6题

取得平均薪水最高的部门的部门编号（至少给出两种解决方案）

第一种方案：降序排列取第一个
```sql
select
	deptno,avg(sal) as avgsal
from 
	emp
group by
	deptno
order by 
	avgsal desc
limit 1;
```
第二种方案：max函数
```sql
select
	deptno,avg(sal) as avgsal
from
	emp
group by
	deptno
having
	avg(sal)=(select max(t.avgsal) from (select avg(sal) as avgsal from emp group by deptno) t);
```

### 第7题

取得平均薪水最高的部门的部门名称

比上面的题目多一个表连接，和dept表连接，按照部门名称进行分组。

1. 每个部门的平均薪水
	```sql
	select avg(sal) avgsal from emp group by deptno;
	```
2. 取得平均薪水最高的部门
	```sql
	select 
		avg(sal) avgsal
	from
		emp
	group by
		deptno 
	order by
		avgsal desc
	limit 1;
	```
3. join部门表得到名称
	```sql
	select
		d.dname,avg(e.sal) as avgsal
	from
		emp e
	join
		dept d
	on
		e.deptno=d.deptno
	group by
		d.dname
	order by
		avgsal desc
	limit 1;
	```

### 第8题

求平均薪水的等级最低的部门的部门名称

1. 求每个部门的编号和平均薪水
```sql
select deptno, avg(sal) as avgsal from emp group by deptno;
```
2. 求每个部门的编号、平均薪水等级
```sql
select
	t.deptno, s.grade
from
	salgrade s
join
	(select deptno, avg(sal) as avgsal from emp group by deptno) t
on
	t.avgsal between s.losal and s.hisal;
```
3. 得到最小的等级(`min(s.grade)`)
```sql
select min(sp.grade) from salgrade sp join (select deptno, avg(sal) as avgsal from emp group by deptno) tp on tp.avgsal between sp.losal and sp.hisal;
```
4. 找等级相等的部门名称
```sql
select
	d.dname, s.grade
from
	salgrade s
join
	(select deptno, avg(sal) as avgsal from emp group by deptno) t
on
	t.avgsal between s.losal and s.hisal
join
	dept d
on
	d.deptno = t.deptno
where
	s.grade = (select min(sp.grade) from salgrade sp join (select deptno, avg(sal) as avgsal from emp group by deptno) tp on tp.avgsal between sp.losal and sp.hisal);
```

这个是他原来的写法，并不能处理并列倒数第一的情况
```sql
select t.*,s.grade from (select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname) t join salgrade s on t.avgsal between s.losal and s.hisal order by s.grade asc limit 1;
```

### 第9题

取得比普通员工(员工代码没有在mgr字段上出现的)的最高薪水还要高的领导人姓名

1. 所有普通员工的最高薪水
	```sql
	select max(sal) from emp where empno not in(select mgr from emp where mgr is not null);
	```
2. 大于以上最高薪水的一定是要找的领导人。
	```sql
	select ename,sal from emp where sal > (select max(sal) from emp where empno not in(select mgr from emp where mgr is not null));
	```

### 第10题

取得薪水最高的前五名员工

```sql
select ename,sal from emp order by sal desc limit 5;
```

### 第11题

取得薪水最高的**第六到第十名**员工

```sql
select ename,sal from emp order by sal desc limit 5, 5;
```

### 第12题

取得最后入职的5名员工

```sql
select ename,sal,hiredate from emp order by hiredate desc limit 5;
```

### 第13题

取得每个薪水等级有多少员工

1. 找出每个员工的薪水等级
	```sql
	select
		empno, grade
	from
		emp e
	join
		salgrade s
	on
		e.sal between s.losal and s.hisal;
	```
2. 每个薪水等级有多少员工
```sql
select
	count(*),grade
from
	emp e
join
	salgrade s
on
	e.sal between s.losal and s.hisal
group by
	grade;
```

### 第14题

列出所有员工及领导的姓名

```sql
select
	e1.ename worker, e2.ename leader
from
	emp e1
join
	emp e2
on 
	e1.mgr = e2.empno;
```

### 第15题

列出受雇日期早于其直接上级的所有员工的编号,姓名,部门名称

```sql
select
	e1.empno, e1.ename, d.dname
from
	emp e1
join
	emp e2
on 
	e1.hiredate < e2.hiredate and e1.mgr = e2.empno
join
	dept d
on
	e1.deptno = d.deptno;
```


### 第16题

列出部门名称和这些部门的员工信息,同时列出那些没有员工的部门

```sql
select
	dept.dname, emp.ename, emp.sal
from 
	dept
left join
	emp
on
	dept.deptno = emp.deptno;
```


### 第17题

列出至少有5个员工的所有部门

1. 每个部门有多少员工
```sql
select deptno, count(*) from emp group by deptno;
```
2. 员工数大于等于五
```sql
select deptno, count(*) from emp group by deptno having count(*) >= 5;
```

### 第18题

列出薪金比"SMITH"多的所有员工信息

1. "SMITH"的薪资
	```sql
	select sal from emp where ename = 'SMITH';
	```
2. 列出薪金比"SMITH"多的所有员工信息
```sql
select
	ename,sal
from 
	emp
where
	emp.sal > select sal from emp where ename = 'SMITH';
```
3. 换个方法，把smith的工资也列出来
```sql
select
	e.ename,e.sal,s.sal smith_sal
from 
	emp e
join
	(select sal from emp where ename = 'SMITH') s
where
	e.sal > s.sal;
```

### 第19题

列出所有"CLERK"(办事员)的姓名及其部门名称,部门的人数

1. 每个部门的人数和名称
```sql
select d.deptno, d.dname, t.dnum from (select deptno, count(*) dnum from emp group by deptno) t join dept d on d.deptno = t.deptno;
```
2. 列出所有"CLERK"(办事员)的姓名及其部门名称,部门的人数
```sql
select
	e.ename, p.dname, p.dnum
from
	emp e
join
	(select d.deptno, d.dname, t.dnum from (select deptno, count(*) dnum from emp group by deptno) t join dept d on d.deptno = t.deptno) p
on 
	p.deptno = e.deptno
where 
	job = 'CLERK';
```
3. 答案的方法
```sql
select 
	t1.ename,t1.dname,t2.total 
from
	(select e.ename,d.dname,d.deptno from emp e join dept d on e.deptno = d.deptno where e.job = 'CLERK') t1 
join
	(select count(*) as total,deptno from emp group by deptno) t2
on
	t1.deptno = t2.deptno;
```

### 第20题

列出最低薪金大于1500的各种工作及从事此工作的全部雇员人数

```sql
select job,min(sal),count(*) from emp group by job having min(sal)>1500;
```

### 第21题

列出在部门"SALES"<销售部>工作的员工的姓名,假定不知道销售部的部门编号

```sql
select e.ename,d.dname from emp e
join dept d on e.deptno = d.deptno
where d.dname='sales';
```

### 第22题

列出薪金高于公司平均薪金的所有员工,所在部门,上级领导,雇员的工资等级

```sql
select e.ename 员工,l.ename 领导,d.dname,s.grade from
emp e left join emp l on e.mgr = l.empno
join dept d on e.deptno = d.deptno
join salgrade s on e.sal between s.losal and s.hisal
where e.sal > (select avg(sal) from emp);
```

### 第23题

列出与"SCOTT"从事相同工作的所有员工及部门名称

```sql
select e.ename,d.dname,e.job from emp e join dept d on e.deptno=d.deptno
where job=(select job from emp where ename ='scott');
```

### 第24题

列出薪金等于部门号30中员工的薪金的其他员工的姓名和薪金（找出**其他部门**中，薪水与**部门30员工**相同的员工。）

```sql
select ename,sal,deptno from emp 
where sal in(select distinct sal from emp where deptno=30) and deptno <> 30;
```

### 第25题

列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金.部门名称

```sql
select e.ename,e.sal,d.dname from emp e 
join dept d on e.deptno = d.deptno 
where e.sal > (select max(sal) from emp where deptno=30);
```

### 第26题

列出在每个部门工作的员工数量,平均工资和平均服务期限

```sql
select avg(sal),count(*),deptno,avg(datediff(now(),hiredate)) as avgtime from emp group by deptno;
```

### 第27题

列出所有员工的姓名、部门名称和工资

```sql
select e.ename,e.sal,d.dname from emp e join dept d on e.deptno = d.deptno;
```

### 第28题

列出所有部门的详细信息和人数

> `group by`可以弄多个参数，比如`d.deptno,d.dname,d.loc`

```sql
select d.deptno,d.dname,d.loc,count(e.deptno) from emp e 
right join dept d on e.deptno=d.deptno 
group by d.deptno,d.dname,d.loc;
```

### 第29题

列出各种工作的最低工资及从事此工作的雇员姓名

1. 每个工作最低工资
```sql
select min(sal) min_sal, job from emp group by job;
```
2. 最低工资及从事此工作的雇员姓名
```sql
select
	e.ename, t.*
from
	emp e
join
	(select min(sal) min_sal, job from emp group by job) t
on
	t.job = e.job
where
	e.sal = t.min_sal;
```

### 第30题

列出各个部门的MANAGER(领导)的最低薪金

```sql
select deptno,min(sal) from emp where job='MANAGER' group by deptno
```

### 第31题

列出所有员工的年工资,按年薪从低到高排序

```sql
select ename,(sal+ifnull(comm,0))*12 as yearsal from emp order by yearsal asc;
```

### 第32题

求出员工领导的薪水超过3000的员工名称与领导名称

```sql

select e.ename 员工名, l.ename 领导名 from emp e join emp l on e.mgr = l.empno where l.sal>3000;

```

### 第33题

求出部门名称中,带'S'字符的部门员工的工资合计、部门人数

```sql
select 
	d.dname,ifnull(sum(sal),0) as sumsal,count(e.ename) 
from emp e 
right join dept d on e.deptno=d.deptno where d.dname like '%S%' 
group by d.dname;
```

### 第34题

给任职日期超过30年的员工加薪10%

```sql
update emp set sal=sal*1.1 where datediff(now(),hiredate)/365 > 30;
```


### 第35题

某公司面试题

有3个表S（学生表），C（课程表），SC（学生选课表）

S（SNO，SNAME）代表（学号，姓名）

C（CNO，CNAME，CTEACHER）代表（课号，课名，教师）

SC（SNO，CNO，SCGRADE）代表（学号，课号，成绩）

```sql
CREATE TABLE SC
(
	SNO VARCHAR(200),
	CNO VARCHAR(200),
	SCGRADE VARCHAR(200)
);

CREATE TABLE S
(
	SNO VARCHAR(200),
	SNAME VARCHAR(200)
);

CREATE TABLE C
(
	CNO VARCHAR(200),
	CNAME VARCHAR(200),
	CTEACHER VARCHAR(200)
);

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '1', '语文', '张');
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '2', '政治', '王');
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '3', '英语', '李');
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '4', '数学', '赵');
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '5', '物理', '黎明');
commit;
INSERT INTO S ( SNO, SNAME ) VALUES ( '1', '学生1');
INSERT INTO S ( SNO, SNAME ) VALUES ( '2', '学生2');
INSERT INTO S ( SNO, SNAME ) VALUES ( '3', '学生3');
INSERT INTO S ( SNO, SNAME ) VALUES ( '4', '学生4');
commit;
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '1', '40');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '2', '30');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '3', '20');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '4', '80');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '5', '60');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '1', '60');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '2', '60');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '3', '60');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '4', '60');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '5', '40');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '1', '60');
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '3', '80');
commit;
```

问题：

1，找出没选过“黎明”老师的所有学生姓名。


```sql
-- 1. 黎明老师的编号
select cno from c where cteacher='黎明';
-- 2. 选了黎明老师的课的编号
select sno from sc where cno=(select cno from c where cteacher='黎明');
-- 3. 没选他的课的学生姓名
select sname from s where sno not in(select sno from sc where cno=(select cno from c where cteacher='黎明'));
```

2，列出2门以上（含2门）不及格学生姓名及平均成绩。

```sql
-- 每个学生的平均成绩和姓名
select avg(sc.scgrade) avggrade from sc group by sno;
-- 每个学生的平均成绩和姓名
select 
	t.avggrade, s.sname
from
	(select avg(sc.scgrade) avggrade, sno from sc group by sno) t
join
	s
on
	s.sno = t.sno;
-- 大于两个不及格的人
select count(*) num, sno from sc where scgrade < 60 group by sno having num>2;
-- 合起来
select 
	t.avggrade, s.sname
from
	(select avg(sc.scgrade) avggrade, sno from sc group by sno) t
join
	s
on
	s.sno = t.sno
where
	s.sno in (select sno from sc where scgrade < 60 group by sno having count(*)>2);
	
-- 别人的答案
select a.*,b.avgscore from (select s.sno,s.sname,count(sc.scgrade) as num from sc join s on sc.sno=s.sno where sc.scgrade < 60 group by s.sname,s.sno having count(sc.scgrade) >= 2) a join (select sno,avg(scgrade) avgscore from sc group by sno) b on a.sno = b.sno;
```

3，既学过1号课程又学过2号课所有学生的姓名。

```sql
select sc.sno,s.sname from sc join s on sc.sno=s.sno where sc.cno=1 and sc.sno in(select sno from sc where cno=2);
```
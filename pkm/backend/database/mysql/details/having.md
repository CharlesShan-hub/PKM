
**找出除20部分之外，其它部门的平均薪资。**

```sql
select deptno,avg(sal) from emp where deptno<>20 group by deptno; -- 建议
select deptno,avg(sal) from emp group by deptno having deptno <> 20; -- 不建议
```

**查询每个部门平均薪资，找出平均薪资高于2000的。**
```sql
select deptno,avg(sal) from emp group by deptno having avg(sal) > 2000;
```
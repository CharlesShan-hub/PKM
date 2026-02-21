
# 分组函数

> 分组函数的执行原则：先分组，然后对每一组数据执行分组函数。如果没有分组语句group by的话，整张表的数据自成一组。
> 本章案例的数据初始化：[powerpoint-init-data](../details/powerpoint-init-data.md)

分组函数包括五个：
- max：最大值
- min：最小值
- avg：平均值
- sum：求和
- count：计数

---
## max

**找出员工的最高薪资**
```sql
select max(sal) from emp;
```

## min

**找出员工的最低工资**
```sql
select min(sal) from emp;
```

## avg

**计算员工的平均薪资**
```sql
select avg(sal) from emp;
```

## sum

**计算员工的工资和**
```sql
select sum(sal) from emp;
```

**计算员工的津贴之和**
```sql
select sum(comm) from emp;
```
重点：所有的分组函数都是自动忽略NULL的。

## count

**统计员工人数**
```sql
select count(ename) from emp;
select count(*) from emp;
select count(1) from emp;
```

`count(*)`和`count(1)`的效果一样，统计该组中总记录行数。
**count(ename)统计的是这个ename字段中不为NULL个数总和。**(面试题)

例如：count(comm) 结果是 4，而不是14
```sql
select count(comm) from emp;
```

**统计岗位数量**
```sql
select count(distinct job) from emp;
```

## 分组函数组合使用

```sql
select count(*),max(sal),min(sal),avg(sal),sum(sal) from emp;
```

## 分组函数注意事项

**分组函数不能直接使用在where子句当中**
`select ename,job from emp where sal > avg(sal);` 这个会报错的
原因：分组的行为是在where执行之后才开始的。

  

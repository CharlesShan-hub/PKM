
**找出每个岗位的平均薪资**

```sql
mysql> select job, avg(sal) from emp group by job;
+-----------+-------------+
| job       | avg(sal)    |
+-----------+-------------+
| CLERK     | 1037.500000 |
| SALESMAN  | 1400.000000 |
| MANAGER   | 2758.333333 |
| ANALYST   | 3000.000000 |
| PRESIDENT | 5000.000000 |
+-----------+-------------+
5 rows in set (0.001 sec)
```

**找出每个部门最高工资**

```sql
mysql> select deptno,max(sal) from emp group by deptno;
+--------+----------+
| deptno | max(sal) |
+--------+----------+
|     20 |  3000.00 |
|     30 |  2850.00 |
|     10 |  5000.00 |
+--------+----------+
3 rows in set (0.001 sec)
```

**找出每个部门不同岗位的平均薪资**

```sql
mysql> select deptno,job,avg(sal) from emp group by deptno,job;
+--------+-----------+-------------+
| deptno | job       | avg(sal)    |
+--------+-----------+-------------+
|     20 | CLERK     |  950.000000 |
|     30 | SALESMAN  | 1400.000000 |
|     20 | MANAGER   | 2975.000000 |
|     30 | MANAGER   | 2850.000000 |
|     10 | MANAGER   | 2450.000000 |
|     20 | ANALYST   | 3000.000000 |
|     10 | PRESIDENT | 5000.000000 |
|     30 | CLERK     |  950.000000 |
|     10 | CLERK     | 1300.000000 |
+--------+-----------+-------------+
9 rows in set (0.001 sec)
```

当`select`语句中有`group by`的话，`select`后面只能跟 **分组函数（比如sal）** 或 **参加分组的字段（比如deptno）**，其他的比如ename就不能写

```sql
select ename,deptno,avg(sal) from emp group by deptno; 
--这个SQL执行后会报错。
```

```shell
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'bjpowernode.emp.ENAME' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```


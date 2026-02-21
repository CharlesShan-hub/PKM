### case

**上面这个需求也可以使用：case.. when.. then.. when.. then.. else.. end来完成：**

```sql
select ename, job,
case job
when 'MANAGER' then sal*1.1
when 'SALESMAN' then sal*1.2
else sal
end as sal
from emp;
```

```sql
mysql> select ename, job,
    -> case job
    -> when 'MANAGER' then sal*1.1
    -> when 'SALESMAN' then sal*1.2
    -> else sal
    -> end as sal
    -> from emp;
+--------+-----------+---------+
| ename  | job       | sal     |
+--------+-----------+---------+
| SMITH  | CLERK     |  800.00 |
| ALLEN  | SALESMAN  | 1920.00 |
| WARD   | SALESMAN  | 1500.00 |
| JONES  | MANAGER   | 3272.50 |
| MARTIN | SALESMAN  | 1500.00 |
| BLAKE  | MANAGER   | 3135.00 |
| CLARK  | MANAGER   | 2695.00 |
| SCOTT  | ANALYST   | 3000.00 |
| KING   | PRESIDENT | 5000.00 |
| TURNER | SALESMAN  | 1800.00 |
| ADAMS  | CLERK     | 1100.00 |
| JAMES  | CLERK     |  950.00 |
| FORD   | ANALYST   | 3000.00 |
| MILLER | CLERK     | 1300.00 |
+--------+-----------+---------+
14 rows in set (0.001 sec)
```

  

  